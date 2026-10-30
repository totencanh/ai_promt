# Final competitor video research

## Scope and evidence labels

Reference inspected: `references/competitor_sample.mp4` (the requested singular `reference/` folder did not exist; the readable file is in `references/`). Source video was preserved. Findings combine FFprobe metadata, FFmpeg whole-stream scene/freeze/silence analysis, 136 timeline frames at 1 fps, 18 before/after transition checks, and Vietnamese ASR. **Verified** means directly measurable/visible or supported by the model output; **Hypothesis** means plausible interpretation; **Unknown** means evidence is insufficient. See `SCENE_BREAKDOWN.md`, `TRANSCRIPT.md`, and `AUDIO_ANALYSIS.md` for detailed evidence and caveats.

## 1. Video metadata — Verified

- MP4/ISO Base Media; duration 135.978 s (2:15.98).
- 576×1024, square pixels, 9:16 portrait, progressive, 30 fps.
- H.264/AVC High, yuv420p; AAC HE-AACv2, 44.1 kHz stereo.
- Original source size 2,128,642 bytes. FFmpeg/FFprobe 9.0.2 and Python 3.11.8 were available.

## 2. Story structure — Verified visually / partially ASR-supported

- **Hook, 00:00–00:15:** night bedroom and brief premise/name caption; then a dark figure and ominous hanging doorway detail.
- **Context, 00:15–00:44:** village/river, red building and night water tableaux establish setting and exposition.
- **Threat, 00:44–01:14:** stall confrontation, blade, implied strike and a face in water. Recognized audio 00:55–01:13 contains a question/answer and attack account.
- **Consequence, 01:14–01:32:** return to bed and illness imagery, then a ritual-like doorway tableau.
- **Remedy/climax, 01:32–02:01:** temple exterior, remedy preparation, water/sword, symbolic figure and shrine statue.
- **Outcome/tag, 02:01–02:15.98:** riverside aftermath followed by close-up of a child in water and final facial change.

The central story appears to concern Phạm Nhan and a folk belief/ritual. Full story wording is not certified because ASR misses long intervals.

## 3. Storytelling formula — Verified technique; original story should not be copied

Open with an emotionally charged image, name the premise, add place/context, present a threat, show consequence, reveal a remedy, then end on a short reaction/tag. Suspense is created with sparse information, a held image, a prop reveal (blade), and delayed cut to water/illness imagery. Reuse that abstract progression only; do not reuse names, lines, characters, or this scene sequence.

## 4. Visual style — Verified

Flat, sparse 2D shapes with dark heavy outlines, restrained shading, large negative-space caption zone, a dark navy/green/brown night palette, muted blue water, dusty daylight, and isolated accent colors (red architecture, purple bedding). Local lamp halos and oval ground shadows are visible (e.g., 00:00–00:05; 01:23–01:32). The frame is vertical and mostly locked. See `VISUAL_STYLE_ANALYSIS.md`.

## 5. Character design — Verified

Compact simplified bodies, robe/costume blocks, oversized pale oval faces, large black eyes, small mouth marks, and little facial detail (e.g., bed figure at 00:00; striped figure at 00:55; water face at 01:09 and 02:09). A small pose/expression change carries much of the emotion. Exact character identities beyond captioned names/roles are not always distinguishable.

## 6. Environment design — Verified

Sets reduce to a few readable symbols: bed/window/lamp (00:00), doorway/hanging shape (00:05, 01:23), houses/river/boats (00:15), red building (00:23), stall/shore (00:44), temple façade (01:32), canopy/well (01:39), statue pedestal (01:53), hut/river (02:01). Strong horizontal water/shore bands anchor compositions.

## 7. Scene construction — Verified with approximate times

Whole-video 30 fps `scdet` and 1 fps review locate the major hard-cut windows at 05.23, 15.33, 23.37, 31.67, 35.70, 44.17, 55.73, 62.27, 69.33, 74.23, 83.13, 92.47, 99.30, 106.00, about 108.30 (visual check), 113.03, 121.60, and about 128.70 (visual check). Several are shot/beat changes within one location, not new scenes. 18 before/after frame checks are in `frames/cutchecks/`. No dissolve/fade was seen at the checked transitions.

## 8. Animation techniques — Verified and hypothesis separated

- **Verified:** 29 low-change intervals longer than 1 s at `freezedetect n=-48 d=1`, median 3.2 s; examples include 44.37–52.20 (7.83 s) and 86.30–91.67 (5.37 s). Frames predominantly hold, then switch pose/prop/composition. No evident camera move or parallax at 1 fps sampling.
- **Hypothesis:** likely limited animation / held artwork with pose swaps and editorial cuts. The H.264 export cannot identify software, rigs, layer structure, or drawing cadence. Small motion can be missed by sample rate/freeze threshold.

## 9. Audio and narration — Partly verified; important unknowns remain

FFmpeg Whisper filter was already available. With the approved `large-v3-turbo-q5_0` model and 12 s queue, ASR yielded coherent Vietnamese in portions: opening (00:00–00:04.8), confrontation/question/answer (00:47.9–01:13.5), illness (01:14.4–01:22.6), remedy (01:35.9–01:47.8), and final line (02:12.3–02:15.1). It repeatedly emitted a subscribe phrase across intervals that conflict with visible captions; these are marked unreliable in `TRANSCRIPT.md`. Other names/terms may be wrong.

Measured signal: mean −22.4 dBFS, peak −3.3 dBFS. Two brief below-threshold intervals near 01:02.06 and 01:32.06, each about 0.43 s. Speaker identity/accent, accurate whole-video speech rate, music, ambience and effects are unknown because the WAV was not directly auditioned and ASR is incomplete. Dialogue quotes appear embedded in narration; separate voice acting is unverified.

## 10. Editing and pacing — Verified

Shot holds run for several seconds, with 29 low-change intervals detected (median 3.2 s). Change tends to be a hard cut between a held tableau and a new image/prop state. Two short low-level audio gaps near 01:02 and 01:32 align approximately with a weapon/river beat and the daylight temple change, but exact suspense intent cannot be confirmed. The 30 fps file is an export rate, not proof of animation on ones.

## 11. Audio-visual synchronization — Partial

- Opening speech and opening caption agree at 00:00–00:04.8.
- Recognized question/answer and sword narrative around 00:55–01:13 align broadly with the face-off, blade change and water close-up.
- Recognized illness passage 01:14–01:23 aligns with the bed image; remedy passage 01:35–01:48 aligns with temple/canopy/water visuals.
- The ASR failure spans 00:05.9–00:47.9, 01:23.4–01:35.9 and about 01:47.8–02:11.8. Captions in those ranges describe exposition/remedy rationale, but captions alone do not verify audio wording. Word-level sync and pause intent remain unknown.

## 12. Reusable production formula

1. Build a short original premise around one question/threat.
2. Write narration in short clauses, each introducing one fact or consequence.
3. Break script into 12–20 phone-readable visual beats.
4. Board mostly locked, sparse tableaux; reserve close-ups for clues and reactions.
5. Use held poses; animate only gestures, expression, prop state, or one atmospheric loop that advances the story.
6. Keep captions large, brief, high contrast and within a safe upper band.
7. Delay the key reveal, show consequence, and make the remedy/outcome causally clear.
8. Use hard cuts for meaningful location/action changes; use fades only when time passage or mood actually calls for them.
9. Design a fresh palette, character silhouette, symbols and sets for every story.
10. Record/ASR-check narration, manually correct names, listen through the entire audio, and mix music/effects only after verifying synchronization.

## 13. Recommended technical workflow for new videos

- Probe source/script assets and lock a vertical 9:16 target before storyboarding.
- Make a timestamped script/shot map; reserve the caption region in each storyboard panel.
- Create original character/environment style sheets and export simple layers.
- Animate selectively with key poses, holds and restrained camera moves; keep an edit decision list with planned shot times.
- Record Vietnamese narration; run local ASR to draft timestamps, manually listen and correct the transcript.
- Mix voice first, then purposeful ambience/music/SFX; check levels and scene cuts by listening.
- Export and inspect full-resolution frames at every cut plus timeline samples; run scene-change/freeze checks as aids, not authoritative labels.
- Verify title/captions, phone-size legibility, spelling, audio sync and final close before delivery.

## 14. Unverified points / limitations

- Exact transcript over the ASR-failure intervals; human listening and manual correction still required.
- Music, sound effects, ambience, voice identity/accent, multiple speakers, and detailed speech pacing.
- Exact frame-accurate boundaries for unscored cuts and any subtle dissolve/fade between unreviewed frames.
- Micro-motion between 1 fps samples; freeze detector can miss very subtle movement.
- Specific animation software, rigging method, asset layering, and source artwork cadence.
- Historical accuracy of the narrated legend.

## Artifacts

- Detailed analysis: `VIDEO_METADATA.md`, `SCENE_BREAKDOWN.md`, `STORYTELLING_ANALYSIS.md`, `VISUAL_STYLE_ANALYSIS.md`, `ANIMATION_ANALYSIS.md`, `AUDIO_ANALYSIS.md`, `TRANSCRIPT.md`.
- Frame evidence: 45 earlier 3 s samples, 136 1 s samples, dense contact sheets, scene/freeze logs, and before/after checks under `frames/`.
- Local model: `models/ggml-large-v3-turbo-q5_0.bin` (574,041,195 bytes; SHA-256 `394221709CD5AD1F40C46E6031CA61BCE88931E6E088C188294C6D5A55FFA7E2`).
- Audio: `audio.wav`; ASR raw/review outputs: `TRANSCRIPT_raw.json`, `TRANSCRIPT_raw.srt`, `TRANSCRIPT_retry.json`, `TRANSCRIPT_retry.srt`.
