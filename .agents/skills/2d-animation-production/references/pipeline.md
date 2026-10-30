# Production pipeline and artifact contracts

Package root convention: `production/<project-slug>/`. Keep planning documents under `planning/`, reusable character/environment art under `assets/`, per-scene renders under `scenes/`, narration under `audio/voice/`, sound under `audio/sfx/` and `audio/music/`, and final exports under `renders/`. Use stable IDs (`CHAR-01`, `ENV-01`, `SC-01`, `SH-01`, `VO-01`, `ASSET-01`) in filenames and documents.

## Run preflight

Before planning or resuming production, inspect the current files and re-check the tools/runtime/model/audio that the next stage needs. Compare that evidence with manifest and README status; correct stale `blocked`, `ready`, and output claims before making stage decisions. A prior TTS smoke-test file proves the engine/reference path can run, but it is not story narration unless its text maps to the current script line IDs.

| Stage | Input → work → output | Tools and quality gate | Depends on |
|---|---|---|---|
| 1. Topic and story development | Topic/rough plot → premise, audience, originality check, emotional question, beat arc → `planning/story.md` | Language model; ask only material choices. Clear hook, stakes, causality, ending. | None |
| 2. Script writing | Story → narration/dialogue, line IDs, caption text, pronunciation notes, delivery intention → `planning/script.md` | Language model; optional local word/timing counts. Review Vietnamese, tone marks, concise lines, no copied dialogue. | Story |
| 3. Scene breakdown | Script lines → purpose, location, characters, action/reveal, provisional duration, continuity → `planning/scene-plan.md` | Every line maps to scene IDs; each scene changes story information. | Script |
| 4. Storyboard | Scene plan → panels/shots with framing, composition, motion, captions, IDs, audio links → `planning/storyboard.md` and optional panels | Sketches/specs are preproduction only. Check hook, visual escalation, shot variety, phone readability, and caption-safe region. | Scene plan, script |
| 5. Character design | Roles/story → distinct silhouette, proportion/expression/costume/color rules → visual bible and a design sheet | Use an available image-generation/drawing tool for production artwork. Iterate one sheet until readable at target size; do not proceed with crude placeholder geometry unless explicitly requested. | Story, storyboard |
| 6. Environment/background design | Locations/visual bible → environment IDs, layer plan, palette/light/depth → visual bible and representative keyframe | Review focal point, negative space, lighting, character contrast, and phone size. Lock a keyframe with the character references before batching art. | Scene plan, character bible |
| 7. Visual asset generation | Approved design references → scene-specific poses/props/backgrounds; record source/version → `assets/` | Preserve character/style across shots. Keep captions editable and separate. Inspect a contact sheet and correct bad frames. If image tools are missing, stop at storyboard/animatic; do not turn primitive code art into a film by default. | Stages 5–6 approved |
| 8. VieNeu voice generation | Final sample script + fixed reference → verified SDK and heard test → measured VO WAVs | Follow `references/vieneu-tts.md`; setup/model downloads require approval. Listen to the test; verify pronunciation, reference suitability, artifacts, tone, and duration before fixing shot timing. | Script; rights and runtime/model available |
| 9. Sound design | Measured voice + scene timing → intentional music/ambience/SFX map and files | Use suitable existing, generated, or licensed sources. Procedural noise is not a substitute for designed cues unless requested. Listen to the mixed sample; keep dialogue intelligible. | Voice and rough cut |
| 10. Animation and scene assembly | Approved art + voice timing + motion plan → scene clips | Animate planned body/facial/prop/effect changes with available tools. A still with only pan/zoom can serve as an animatic or deliberate tableau, but is not character animation. Compare each shot with its board. | Assets and audio approved |
| 11. Video editing | Scene clips + measured audio → coherent timed edit with transitions/captions → review export | Fit shots to measured speech and holds. Add captions as overlays; verify they do not hide faces/action. Missing narration yields only a labeled silent preview, never a complete narrated sample. | Scene renders, audio plan |
| 12. Quality control | Review export + package → watch/listen, phone-size, continuity/ID/sync review → QC record | Watch the requested deliverable and hear its full mix. Check shot/pose variety, line/caption accuracy, pacing, artifacts, sync, ending, and decode. Fix defects, do not just log them. | Edit |
| 13. Final export | QC-passed timeline → requested export and record | Probe codec, dimensions, fps, duration, audio, and decode. State whether output is a storyboard, animatic, silent preview, sample, or finished animation. Technical validity is not artistic approval. | QC pass |

## Stop/go gates

1. **Visual proof:** do not create the full panel batch until one representative frame passes style, character, composition, and phone-size checks.
2. **Audio proof:** do not lock edit duration until a real voice sample has been generated, heard, and measured. If synthesis is blocked, report it; offer a silent animatic only if that still meets the request.
3. **Integrated proof:** for a sample request, deliver a short self-contained clip containing actual voice, chosen visual treatment, meaningful planned motion, captions, and mixed audio. If any element is absent, label the narrower deliverable and blocker.
4. **Scale/final:** expand to a full runtime only when requested; perform full playback/listening QC before calling it finished.

## Dependency and regeneration rules

- A changed script line traces through its scene IDs to storyboard panels, VO files, captions, and edit timestamps; regenerate only affected descendants.
- A character/environment change lists every dependent scene and rerenders those scenes.
- A changed VO segment is regenerated, remeasured, then its scene timing and downstream edit are updated.
- A scene render can be replaced and re-edited without rebuilding unrelated art when duration/audio are unchanged.
- Keep tool, prompt, version/seed if supplied, source/license, approval, and status with generated assets.
- Missing tools stop only dependent stages. Continue independent planning and report pending outputs.
