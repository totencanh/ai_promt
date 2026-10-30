# Production formula derived from the reference research

## Evidence ledger

### Verified observations

- The source was a 135.98 s, 576×1024, 9:16, 30 fps H.264 video with stereo HE-AAC audio. Its shot design uses vertically framed, sparse 2D tableaux and Vietnamese captions.
- Visuals favor flat outlined forms, simplified robe-like figures, pale expressive faces, sparse symbolic sets, dark night fields, muted blue water, and a few warm/color accents. Large upper negative space holds captions.
- 136 frames sampled across the full runtime and 18 before/after checks show abrupt cuts between many held compositions. FFmpeg found 29 low-change intervals longer than one second (median 3.2 s). This supports economical held-pose staging, not a claim about the original software or drawing cadence.
- The story visually progresses through premise, setting, threat, consequence, remedy, and a final water-side tag. Some narration was recognized by Vietnamese ASR, but long intervals were unreliable.

### Uncertain or unknown

- Exact audio wording is unresolved in significant intervals. Music, sound effects, narrator identity/accent, exact delivery, and word-level sync were not verified. Do not turn captions into claims about audible speech.
- The export does not establish the source software, rigging, layer count, camera workflow, or animation-on-ones/twos.
- The reference’s 2:16 runtime and observed shot lengths are examples, not required targets for every new story.

## Reusable creative formula

1. **Premise and hook:** start with a strong image or unanswered question; name the central problem early.
2. **Orientation:** establish who/where/what matters with a small number of readable visual cues.
3. **Escalation:** each beat adds a clue, threat, cost, or consequence. Avoid explanatory lines that do not change the viewer’s understanding.
4. **Reveal and response:** delay one key piece of information, show its consequence, then let the protagonist make a credible choice.
5. **Payoff:** resolve the central question. Add a short final image only if it deepens the meaning without undoing causal clarity.
6. **Visual economy:** plan one primary action per shot. Use held frames for reading and tension; spend motion on a gesture, facial change, prop state, or reveal.
7. **Mobile composition:** choose the target aspect ratio early; protect caption-safe space; keep silhouettes and focal props readable at phone size.
8. **Pacing:** time narration first, then fit shots to spoken phrases and visual holds. Treat any target duration as a draft until the generated audio and edit are measured.
9. **Audio:** produce clean, consistent narration first. Add music/effects only when available and intentionally selected; confirm by listening. The reference does not verify a specific music or SFX formula.
10. **Originality:** create a fresh premise, dialogue, character silhouettes, palette logic, props, environments, and sequence. Abstract technique can transfer; protected expression cannot.

## Production constraints for the new package

- Use scene/script IDs rather than matching files by title or order alone.
- Character and environment bibles are the source of truth for all scenes.
- Lock a narration segment to its script line IDs, scene ID, and audio filename before editing.
- Estimate scene durations initially; replace estimates with measured voice/render durations during edit.
- If tools are missing, deliver the completed upstream planning artifacts and label downstream media as pending. Never imply that a prompt is a generated asset.
