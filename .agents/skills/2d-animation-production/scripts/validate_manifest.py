#!/usr/bin/env python3
"""Check manifest structure, safe relative paths, and scene/artifact links.

This validator checks technical consistency only. It cannot judge creative
quality, actual playback/listening, rights, or whether a human approved media.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path, PurePosixPath

BASE_ARTIFACTS = ("story", "script", "scene_plan", "storyboard", "visual_bible", "audio_plan", "edit_plan")
OPTIONAL_ARTIFACTS = ("character_bible", "environment_bible", "qc_report")
STATUSES = {"planned", "in_progress", "blocked", "ready_for_review", "approved", "rejected"}
LEGACY_STATUSES = {"ready", "locked"}  # Accepted for older manifests; use ready_for_review/approved in new work.
FILE_STATUSES = {"ready_for_review", "approved", "ready", "locked"}


class Check:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, message: str) -> None:
        self.errors.append(message)

    def warn(self, message: str) -> None:
        self.warnings.append(message)


def relpath(value: object, label: str, check: Check) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        check.error(f"{label}: expected a non-empty package-relative path")
        return None
    path = PurePosixPath(value.replace("\\", "/"))
    if path.is_absolute() or any(part in ("", ".", "..") for part in path.parts):
        check.error(f"{label}: path must stay inside its declared root: {value}")
        return None
    return Path(*path.parts)


def validate(data: dict, package_root: Path, workspace_override: Path | None, check_files: bool) -> Check:
    check = Check()
    if data.get("schema_version") not in (1, 2):
        check.error("schema_version must be 1 or 2")
    if not data.get("project_id") or not data.get("title"):
        check.error("project_id and title are required")
    status = data.get("status")
    if status not in STATUSES | LEGACY_STATUSES:
        check.error(f"status must be one of {sorted(STATUSES)}")

    target = data.get("target", data.get("format", {}))
    for key in ("width", "height", "fps"):
        if not isinstance(target.get(key), (int, float)) or target[key] <= 0:
            check.error(f"target.{key} must be positive")
    if not isinstance(target.get("aspect_ratio"), str) or ":" not in target["aspect_ratio"]:
        check.error("target.aspect_ratio is required, e.g. 9:16")

    if workspace_override:
        workspace = workspace_override.resolve()
    else:
        workspace = (package_root / data.get("workspace_root", "..")).resolve()
    if not workspace.is_dir():
        check.error(f"workspace root does not exist: {workspace}")

    voice = data.get("voice", {})
    if isinstance(voice, dict):
        reference = voice.get("reference_audio_path")
        if reference is not None:
            reference_path = relpath(reference, "voice.reference_audio_path", check)
            if check_files and reference_path and not (workspace / reference_path).is_file():
                check.error(f"voice reference file is missing: {workspace / reference_path}")
        if voice.get("method") not in (None, "", "undecided") and not voice.get("rights_confirmed", False):
            check.warn("voice method is selected but rights_confirmed is not true; do not synthesize/clone until rights are confirmed")

    artifacts = data.get("artifacts", {})
    artifact_paths: dict[str, Path] = {}
    for key in BASE_ARTIFACTS + OPTIONAL_ARTIFACTS:
        item = artifacts.get(key)
        if item is None and key in OPTIONAL_ARTIFACTS and data.get("schema_version") == 1:
            continue
        if not isinstance(item, dict):
            check.error(f"artifacts.{key} is required")
            continue
        path = relpath(item.get("path"), f"artifacts.{key}.path", check)
        item_status = item.get("status")
        if path:
            artifact_paths[key] = path
        if item_status not in STATUSES | LEGACY_STATUSES:
            check.error(f"artifacts.{key}.status must be one of {sorted(STATUSES)}")
        elif path and check_files and item_status in FILE_STATUSES and not (package_root / path).is_file():
            check.error(f"artifact marked {item_status} but file missing: {path}")
        elif path and check_files and item_status in {"planned", "in_progress", "blocked"} and not (package_root / path).exists():
            check.warn(f"artifact pending ({item_status}): {path}")

    scenes = data.get("scenes")
    if not isinstance(scenes, list) or not scenes:
        check.error("scenes must contain at least one scene")
        scenes = []
    scene_ids: set[str] = set()
    line_ids: set[str] = set()
    panel_ids: set[str] = set()
    voice_ids: set[str] = set()
    for index, scene in enumerate(scenes):
        label = f"scenes[{index}]"
        if not isinstance(scene, dict):
            check.error(f"{label} must be an object")
            continue
        scene_id = scene.get("id")
        if not isinstance(scene_id, str) or not scene_id:
            check.error(f"{label}.id is required")
        elif scene_id in scene_ids:
            check.error(f"duplicate scene id: {scene_id}")
        else:
            scene_ids.add(scene_id)
        duration = scene.get("duration_s")
        if duration is not None and (not isinstance(duration, (int, float)) or duration <= 0):
            check.error(f"{label}.duration_s must be positive or null while provisional")
        scene_status = scene.get("status")
        if scene_status not in STATUSES | LEGACY_STATUSES:
            check.error(f"{label}.status must be one of {sorted(STATUSES)}")

        scene_line_ids = scene.get("script_line_ids")
        panel_list = scene.get("storyboard_panel_ids")
        for field, values, collected in (("script_line_ids", scene_line_ids, line_ids), ("storyboard_panel_ids", panel_list, panel_ids)):
            if not isinstance(values, list) or any(not isinstance(value, str) or not value for value in values):
                check.error(f"{label}.{field} must be a list of non-empty IDs")
                continue
            for value in values:
                if value in collected:
                    check.error(f"duplicate {field} value: {value}")
                collected.add(value)
        if not isinstance(scene.get("character_ids"), list):
            check.error(f"{label}.character_ids must be a list")
        if scene.get("environment_id") is not None and not isinstance(scene.get("environment_id"), str):
            check.error(f"{label}.environment_id must be a string or null")

        segments = scene.get("voice_segments", [])
        if not isinstance(segments, list):
            check.error(f"{label}.voice_segments must be a list")
            segments = []
        for index_voice, segment in enumerate(segments):
            vlabel = f"{label}.voice_segments[{index_voice}]"
            if not isinstance(segment, dict):
                check.error(f"{vlabel} must be an object")
                continue
            voice_id = segment.get("id")
            if not isinstance(voice_id, str) or not voice_id:
                check.error(f"{vlabel}.id is required")
            elif voice_id in voice_ids:
                check.error(f"duplicate voice segment id: {voice_id}")
            else:
                voice_ids.add(voice_id)
            linked_lines = segment.get("script_line_ids")
            if not isinstance(linked_lines, list) or not linked_lines:
                check.error(f"{vlabel}.script_line_ids must link to at least one script line")
            elif not set(linked_lines).issubset(set(scene_line_ids or [])):
                check.error(f"{vlabel}.script_line_ids must belong to scene {scene_id}")
            audio_path = relpath(segment.get("path"), f"{vlabel}.path", check)
            if audio_path and audio_path.suffix.lower() not in (".wav", ".mp3", ".flac", ".m4a", ".ogg"):
                check.error(f"{vlabel}.path must use a supported audio extension")
            voice_status = segment.get("status", scene_status)
            if voice_status not in STATUSES | LEGACY_STATUSES:
                check.error(f"{vlabel}.status must be one of {sorted(STATUSES)}")
            elif check_files and voice_status in FILE_STATUSES and audio_path and not (package_root / audio_path).is_file():
                check.error(f"voice marked {voice_status} but file missing: {audio_path}")

        assets = scene.get("assets", [])
        if not isinstance(assets, list):
            check.error(f"{label}.assets must be a list")
            assets = []
        for asset_index, asset in enumerate(assets):
            alabel = f"{label}.assets[{asset_index}]"
            if not isinstance(asset, dict):
                check.error(f"{alabel} must be an object")
                continue
            asset_path = relpath(asset.get("path"), f"{alabel}.path", check)
            asset_status = asset.get("status", scene_status)
            if asset_status not in STATUSES | LEGACY_STATUSES:
                check.error(f"{alabel}.status must be one of {sorted(STATUSES)}")
            elif check_files and asset_status in FILE_STATUSES and asset_path and not (package_root / asset_path).is_file():
                check.error(f"asset marked {asset_status} but file missing: {asset_path}")

        render = relpath(scene.get("render_path"), f"{label}.render_path", check)
        if check_files and scene_status in FILE_STATUSES and render and not (package_root / render).is_file():
            check.error(f"scene marked {scene_status} but render missing: {render}")

    if check_files:
        for key, ids in (("script", line_ids), ("storyboard", panel_ids), ("scene_plan", scene_ids)):
            item = artifacts.get(key, {})
            path = artifact_paths.get(key)
            if path and item.get("status") in FILE_STATUSES and (package_root / path).is_file():
                content = (package_root / path).read_text(encoding="utf-8", errors="replace")
                missing = [value for value in ids if not re.search(r"(?<![\w-])" + re.escape(value) + r"(?![\w-])", content)]
                if missing:
                    check.error(f"artifacts.{key} is missing linked ID(s): {', '.join(sorted(missing))}")

    review = data.get("review", {})
    if isinstance(review, dict) and status == "approved" and not review.get("full_playback_reviewed", False):
        check.warn("project status is approved but full_playback_reviewed is not true; confirm QC evidence")
    if data.get("schema_version") == 1:
        check.warn("schema_version 1 is legacy; new projects should use schema_version 2")
    return check


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only production manifest consistency checker")
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--check-files", action="store_true")
    parser.add_argument("--workspace-root", type=Path, help="Override workspace root when validating a copied template")
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: cannot read manifest: {error}", file=sys.stderr)
        return 2
    if not isinstance(data, dict):
        print("ERROR: manifest root must be a JSON object", file=sys.stderr)
        return 2
    result = validate(data, args.manifest.parent.resolve(), args.workspace_root, args.check_files)
    for warning in result.warnings:
        print(f"WARN: {warning}")
    for error in result.errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if result.errors:
        print(f"FAILED: {len(result.errors)} error(s), {len(result.warnings)} warning(s)")
        return 1
    print(f"OK: manifest links are consistent ({len(data['scenes'])} scene(s), {len(result.warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
