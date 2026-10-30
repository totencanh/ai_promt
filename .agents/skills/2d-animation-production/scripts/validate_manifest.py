#!/usr/bin/env python3
"""Read-only checks for scene, audio, and artifact links in a production manifest."""
from __future__ import annotations
import argparse, json, re, sys, wave
from pathlib import Path, PurePosixPath

ARTIFACT_KEYS=("story","script","scene_plan","storyboard","visual_bible","audio_plan","edit_plan")
STATUSES={"planned","in_progress","ready","locked"}
class Check:
    def __init__(self): self.errors=[]; self.warnings=[]
    def error(self,msg): self.errors.append(msg)
    def warn(self,msg): self.warnings.append(msg)
def relpath(value,label,c):
    if not isinstance(value,str) or not value.strip(): c.error(f"{label}: expected a non-empty relative path"); return None
    path=PurePosixPath(value.replace("\\","/"))
    if path.is_absolute() or any(part in ("",".","..") for part in path.parts): c.error(f"{label}: path must stay inside package: {value}"); return None
    return Path(*path.parts)
def validate(data,package_root,workspace_override,check_files):
    c=Check()
    if data.get("schema_version")!=1: c.error("schema_version must be 1")
    if not data.get("project_id") or not data.get("title"): c.error("project_id and title are required")
    fmt=data.get("format",{})
    for k in ("width","height","fps"):
        if not isinstance(fmt.get(k),(int,float)) or fmt[k]<=0: c.error(f"format.{k} must be positive")
    if not isinstance(fmt.get("aspect_ratio"),str) or ":" not in fmt["aspect_ratio"]: c.error("format.aspect_ratio is required, e.g. 9:16")
    root=workspace_override.resolve() if workspace_override else (package_root/data.get("workspace_root","..")).resolve()
    if not root.is_dir(): c.error(f"workspace root does not exist: {root}")
    ref=data.get("voice_reference",{})
    if ref.get("canonical_path")!="/analysis/audio.wav": c.error("voice_reference.canonical_path must remain exactly /analysis/audio.wav")
    if ref.get("workspace_relative_path")!="analysis/audio.wav": c.error("voice_reference.workspace_relative_path must resolve the fixed file from workspace root")
    if check_files and root.is_dir():
        audio=root/'analysis'/'audio.wav'
        if not audio.is_file(): c.error(f"fixed voice reference is missing: {audio}")
        else:
            try:
                with wave.open(str(audio),'rb') as w:
                    if not w.getnframes() or not w.getframerate(): c.error(f"fixed reference is empty/invalid: {audio}")
                    else: c.warn(f"fixed reference readable: {w.getnchannels()} ch, {w.getframerate()} Hz, {w.getnframes()/w.getframerate():.2f} s; SDK may trim to <=8 s")
            except (wave.Error,OSError) as e: c.error(f"fixed reference is not a readable WAV: {e}")
    artifacts=data.get('artifacts',{})
    artifact_paths={}
    for k in ARTIFACT_KEYS:
        item=artifacts.get(k)
        if not isinstance(item,dict): c.error(f"artifacts.{k} is required"); continue
        path=relpath(item.get('path'),f"artifacts.{k}.path",c); status=item.get('status')
        if path: artifact_paths[k]=path
        if status not in STATUSES: c.error(f"artifacts.{k}.status must be one of {sorted(STATUSES)}")
        elif path and check_files and status in {'ready','locked'} and not (package_root/path).is_file(): c.error(f"artifact marked {status} but file missing: {path}")
        elif path and check_files and status in {'planned','in_progress'} and not (package_root/path).exists(): c.warn(f"artifact pending ({status}): {path}")
    scenes=data.get('scenes')
    if not isinstance(scenes,list) or not scenes: c.error("scenes must contain at least one scene"); scenes=[]
    scene_ids=set(); line_ids=set(); panel_ids=set(); voice_ids=set()
    for i,s in enumerate(scenes):
        label=f"scenes[{i}]"; sid=s.get('id')
        if not isinstance(sid,str) or not sid: c.error(f"{label}.id is required")
        elif sid in scene_ids: c.error(f"duplicate scene id: {sid}")
        else: scene_ids.add(sid)
        if not isinstance(s.get('duration_s'),(int,float)) or s['duration_s']<=0: c.error(f"{label}.duration_s must be positive")
        status=s.get('status')
        if status not in STATUSES: c.error(f"{label}.status must be one of {sorted(STATUSES)}")
        for field,seen in (("script_line_ids",line_ids),("storyboard_panel_ids",panel_ids)):
            ids=s.get(field)
            if not isinstance(ids,list) or not ids or any(not isinstance(x,str) or not x for x in ids): c.error(f"{label}.{field} must be a non-empty ID list"); continue
            for value in ids:
                if value in seen: c.error(f"duplicate {field} value: {value}")
                seen.add(value)
        if not isinstance(s.get('character_ids'),list) or not s.get('environment_id'): c.error(f"{label} must link character_ids and environment_id")
        segments=s.get('voice_segments')
        if not isinstance(segments,list) or not segments: c.error(f"{label}.voice_segments must contain a segment"); segments=[]
        scene_lines=set(s.get('script_line_ids',[]))
        for j,v in enumerate(segments):
            vl=f"{label}.voice_segments[{j}]"; vid=v.get('id')
            if not isinstance(vid,str) or not vid: c.error(f"{vl}.id is required")
            elif vid in voice_ids: c.error(f"duplicate voice segment id: {vid}")
            else: voice_ids.add(vid)
            links=v.get('script_line_ids')
            if not isinstance(links,list) or not links: c.error(f"{vl}.script_line_ids must link to script lines")
            elif not set(links).issubset(scene_lines): c.error(f"{vl}.script_line_ids must belong to scene {sid}")
            ap=relpath(v.get('path'),f"{vl}.path",c)
            if ap and ap.suffix.lower()!='.wav': c.error(f"{vl}.path must use .wav for VieNeu output")
            vs=v.get('status',status)
            if vs not in STATUSES: c.error(f"{vl}.status must be one of {sorted(STATUSES)}")
            elif check_files and vs in {'ready','locked'} and ap and not (package_root/ap).is_file(): c.error(f"voice marked {vs} but file missing: {ap}")
        for j,a in enumerate(s.get('assets',[])):
            if not isinstance(a,dict): c.error(f"{label}.assets[{j}] must be an object")
            else:
                apath=relpath(a.get('path'),f"{label}.assets[{j}].path",c)
                astatus=a.get('status',status)
                if astatus not in STATUSES: c.error(f"{label}.assets[{j}].status must be one of {sorted(STATUSES)}")
                elif check_files and astatus in {'ready','locked'} and apath and not (package_root/apath).is_file(): c.error(f"asset marked {astatus} but file missing: {apath}")
        render=relpath(s.get('render_path'),f"{label}.render_path",c)
        if check_files and status in {'ready','locked'} and render and not (package_root/render).is_file(): c.error(f"scene marked {status} but render missing: {render}")
    if check_files:
        for key, ids in (("script", line_ids), ("storyboard", panel_ids), ("scene_plan", scene_ids)):
            item=artifacts.get(key, {})
            path=artifact_paths.get(key)
            if path and item.get("status") in {"ready", "locked"} and (package_root/path).is_file():
                content=(package_root/path).read_text(encoding="utf-8", errors="replace")
                missing=[value for value in ids if not re.search(r"(?<![\w-])"+re.escape(value)+r"(?![\w-])", content)]
                if missing: c.error(f"artifacts.{key} is missing linked ID(s): {', '.join(sorted(missing))}")
    return c
def main():
    ap=argparse.ArgumentParser(description="Read-only production manifest consistency checker")
    ap.add_argument('manifest',type=Path); ap.add_argument('--check-files',action='store_true')
    ap.add_argument('--workspace-root',type=Path,help='Override root when validating a copied template')
    a=ap.parse_args()
    try: data=json.loads(a.manifest.read_text(encoding='utf-8'))
    except (OSError,json.JSONDecodeError) as e: print(f"ERROR: cannot read manifest: {e}",file=sys.stderr); return 2
    c=validate(data,a.manifest.parent.resolve(),a.workspace_root,a.check_files)
    for x in c.warnings: print(f"WARN: {x}")
    for x in c.errors: print(f"ERROR: {x}",file=sys.stderr)
    if c.errors: print(f"FAILED: {len(c.errors)} error(s), {len(c.warnings)} warning(s)"); return 1
    print(f"OK: manifest links are consistent ({len(data['scenes'])} scene(s), {len(c.warnings)} warning(s))"); return 0
if __name__=='__main__': raise SystemExit(main())
