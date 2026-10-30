---
name: 2d-animation-production
description: Turn a topic, short story, or rough idea into a linked, original 2D animation production package and, when available tools support it, a rendered video. Use for end-to-end story, storyboard, visual asset, Vietnamese voice, animation, and edit workflows; never copy a reference video’s protected expression.
---

# 2D Animation Production

Build one coherent production package from the user’s topic or idea. Make reasonable creative decisions without waiting for details that can be inferred. Ask only for a choice that materially changes the result or for permission that is required to use a tool, voice, model, or asset.

## Choose the deliverable before production

- If the user asks for a **sample video**, make a short, self-contained proof clip (normally 15–30 seconds) that demonstrates the story hook, approved visual treatment, actual voice, meaningful motion, captions, and sound mix. Do not silently expand this to a full-length film.
- If the user asks for a **full video**, make a short integrated proof clip first, then use the accepted design and measured voice timing to scale the remaining scenes. Do not render a full-length placeholder while key media is blocked.
- Call an output a **storyboard** when it is panels/specs, an **animatic** when it is timed stills with scratch audio, a **silent preview** when narration is absent, and a **finished animation** only when approved artwork, intended motion, final voice, mix, and edit are present and reviewed. State which one was actually made.

## Quality gates

- Before generating a scene batch, create and inspect one representative character design and one representative environment/keyframe at final aspect ratio. Use an available image-generation or drawing tool for production artwork. Procedural/code-native geometry is allowed for layout sketches or when the user explicitly requests that visual style; never substitute it for production character art by default.
- Lock a coherent character sheet and environment keyframe before generating scene art. Reuse those visual references; do not independently redraw the character in each panel. Iterate the proof frame until it meets the visual bible at full size and at phone-preview size.
- Keep captions, titles, and credits as editable overlay layers, not baked into generated artwork. Check that they do not cover faces, focal props, or story action.
- Time the script, generate and listen to a real narration test, and measure its duration before fixing shot timing. Never fill missing narration with extra holds and present the result as a complete sample.
- Every shot needs an intentional visual change (pose, expression, prop, effect, camera move, or a deliberate held tableau with a clear reason). A slow pan/zoom across a still can be a valid edit, but by itself is not character animation. If available tools cannot provide the requested visual quality or motion, stop at a clearly labeled storyboard/animatic and report the blocker.
- A render is not approved by successful encoding or manifest validation. Watch the full requested clip, listen to its full mix, check key images at phone size, and compare the result with the approved storyboard and quality target. Fix visible defects before delivery; do not call a technically valid but visually unreviewed export finished.

## Working rules

- At the start of each run, reconcile the manifest/README against the current filesystem and re-check relevant tools, runtime, model cache, and outputs. Treat previous `blocked`/`ready` labels as claims to verify, not current truth. Update stale status before deciding whether a production stage can run.
- Read [the production formula](references/production-formula.md) before developing a story. It separates observed reference traits, uncertain claims, and reusable technique.
- Keep the new plot, wording, character designs, props, locations, and shot sequence original. Reuse production principles such as mobile-readable compositions, sparse visual beats, held poses, and deliberate reveals—not the competitor’s expression.
- Inspect the project and available tools before production. Use image-generation, drawing, animation, and audio capabilities for their actual strengths. FFmpeg can edit, composite, and encode; it does not make designed character artwork or animate a character from a still. Do not claim an unavailable or unperformed stage.
- Use available tools under their own permission rules. Do not install packages, download models, or change system configuration without explicit user approval. If VieNeu-TTS is absent or unconfigured, report the exact missing pieces and stop before setup or model downloads.
- Preserve user assets. Re-render only the affected scene when an input changes; propagate its scene ID to storyboard, assets, voice segment, and edit plan.

## End-to-end workflow

Follow the 13 linked stages in [the pipeline guide](references/pipeline.md), including its stop/go review gates. Keep stable IDs for project, character, environment, scene, shot, script line, narration segment, and asset. Update the manifest whenever an ID or file changes. Use the matching template in `templates/` at each stage; `scripts/validate_manifest.py` checks structural links and file presence only. It does not judge artwork, animation, story, audio, or whether anyone reviewed the export.

At minimum, create a package under `production/<project-slug>/` with a manifest, story, script, scene plan, storyboard, visual bible, audio plan, and edit plan. Add production assets only when a suitable tool can create them and they pass the visual/audio review gate. Keep per-scene voice and render outputs addressable so a scene can be regenerated independently. Never mark a placeholder or planned file `ready`.

## VieNeu voice requirement

VieNeu-TTS v3 Turbo is the required voice workflow. Before synthesis, read [the VieNeu integration guide](references/vieneu-tts.md), verify the fixed reference file, user authorization to clone that speaker, installed SDK/backend, and the available model/cache. Use the reference path exactly as documented there; do not substitute another recording or modify the reference. If the file, permission, or dependency check fails, stop the voice stage and report the blocker. Do not install or download anything without approval.

Generate narration by scene/segment, save a mapping from script line IDs to audio file paths, and review pronunciation, Vietnamese tone marks, consistency, pacing, clipping, and alignment. Do not mark audio as approved just because synthesis succeeded.

## Finish criteria

Run the manifest validator and inspect all linked deliverables. Confirm IDs and paths agree, audio segments map to script lines and scenes, each rendered scene uses the approved assets, and export dimensions/frame rate/audio sync match the measured edit plan. Watch the requested clip from start to finish and listen to the mix; review captions and focal action at phone size. Mark unavailable or unverified stages clearly. A written storyboard is not animation, a pan/zoom slideshow is not character animation, and a no-narration preview is not a complete narrated sample.
