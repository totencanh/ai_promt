---
name: 2d-animation-production
description: Develop original Vietnamese folk-horror 2D animation projects from an idea or reference through planning, visual/audio proof, production, editing, and quality review. Use when the user requests animation production or reference analysis; do not copy protected expression from source videos.
---

# 2D Animation Production

Use this skill to make production work concrete, traceable, and honest about what has actually been created. Start by inspecting the project, existing outputs, manifest, and only the tools needed for the requested stage. Preserve existing user assets and respect approval gates for software, models, system changes, voices, and licensed media.

## Route by request

- **Idea, story, script, or preproduction:** read [the master guide](../../../MASTER_PRODUCTION_GUIDE.md) and use only the templates needed for the requested deliverable.
- **Reference-video analysis:** read the master guide's reference-analysis section and [the evidence-based production formula](references/production-formula.md). Record observed, inferred, and unknown claims separately; include timestamps and confidence.
- **Style/design/scene planning:** use the master guide and story, scene, storyboard, visual, character, and environment templates as applicable. Lock representative visual proof before batching assets.
- **Sample video:** make a short integrated proof of concept, normally 15–30 seconds, containing actual approved visuals, intentional motion, real voice, captions, and sound mix. If a component is blocked or absent, label the narrower result (such as storyboard, animatic, or silent preview); do not call it a finished animation.
- **Full production:** make and review an integrated proof clip first. Expand only after the user accepts the proof and requests the full production.
- **Revision:** inspect the dependency links and regenerate only artifacts affected by the requested change.
- **VieNeu voice stage:** read [the VieNeu integration notes](references/vieneu-tts.md) only when VieNeu is selected for the active project. Confirm the reference, rights, runtime, backend, and model state; stop for approval before installs or model downloads.

## Core operating rules

- The root [MASTER_PRODUCTION_GUIDE.md](../../../MASTER_PRODUCTION_GUIDE.md) is the system source of truth for creative direction, artifact contracts, workflow, and QC. Do not duplicate or quietly contradict it in the skill.
- Keep stable project, character, environment, scene, shot, script-line, voice, asset, and audio-cue IDs. Keep script, visuals, voice, captions, and edit linked through the scene plan and manifest.
- Treat target runtime and scene durations as estimates until actual voice and render timing are measured. Do not pad with empty holds to hit a duration.
- A prompt is not an asset; a still with pan/zoom alone is not character animation; successful encoding or manifest validation is not artistic approval. Use the precise name for the deliverable actually inspected.
- Learn abstract production methods from references, not their dialogue, characters, distinctive designs, compositions, props, or shot sequence. Do not infer audible words from captions.
- Use available tools for their actual capabilities. FFmpeg edits, composites, mixes, and encodes; it does not design original character art or animate characters from a still. Never claim to have run an unavailable or unperformed stage.
- Before external or environment-changing actions, follow the user's authorization rules. Do not install, download models, change system configuration, incur cost, or clone a voice without the required approval and rights.
- Record asset source/license, tool/model/version and prompt/seed when available, status, and review notes. Use `planned`, `in_progress`, `blocked`, `ready_for_review`, `approved`, or `rejected`; only a real review may change an artifact to `approved`.
- Technical validation and artistic approval are separate. Watch and listen to the whole requested export, check phone-size readability and continuity, and record QC before calling an export finished.

## Stage completion

At each meaningful stage, state what was created, what was actually run and checked, what is pending or blocked, and the next decision needed. Update the manifest when artifact paths, IDs, or statuses change. Use `scripts/validate_manifest.py` for structural/path checks; it cannot judge story, visual quality, audio, animation, or approval.
