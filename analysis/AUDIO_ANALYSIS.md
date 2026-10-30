# Audio analysis

## Verified signal and ASR

- Source audio: AAC HE-AACv2, 44.1 kHz, stereo, about 32.1 kb/s; duration 135.978 s. Extracted to `audio.wav` (stereo, 44.1 kHz, signed 16-bit PCM).
- FFmpeg `volumedetect`: mean −22.4 dBFS; peak −3.3 dBFS. The RMS plot is `frames/audio_waveform.png`.
- Vietnamese ASR was run locally using the pre-existing FFmpeg 9.0.2 Whisper filter and approved model `models/ggml-large-v3-turbo-q5_0.bin`. It completed on the entire 135.98 s track. JSON output and transcript interpretation: `TRANSCRIPT_retry.json`, `TRANSCRIPT_retry.srt`, and `TRANSCRIPT.md`.
- A 3 s ASR queue caused repeated/overlapping text (`TRANSCRIPT_raw.json`). A 12 s queue reduced overlap and produced meaningful text around 00:00–00:04.8, 00:47.9–01:22.6, 01:35.9–01:47.8, and 02:12.3–02:15.1. It still repeated a subscribe phrase over long stretches that conflict with the on-screen captions. Those intervals remain unresolved, not verified dialogue.
- `silencedetect=noise=-35dB:d=0.4` marked 01:02.061–01:02.491 and 01:32.061–01:32.491 (about 0.43 s each). This threshold catches near-silence only; quieter ambience may remain.

## Narration and pacing

The recognized opening at 00:00–00:04.8 introduces the premise and Phạm Nhan. Recognized narrative around 00:47.9–01:22.6 covers a sword/ritual setup, a quoted question and answer, an attack, and the folk illness explanation. At 01:35.9–01:47.8 the recognized narration gives a remedy. These spans correspond broadly to the river confrontation, face-in-water/bed imagery, and well/temple tableaux (see `SCENE_BREAKDOWN.md`).

Because the ASR misses or corrupts substantial intervals, speaking rate, pause pattern beyond the two thresholded pauses, and exact synchronization cannot be measured reliably. The captions suggest near-continuous explanatory narration, but that is visual evidence and does not prove verbatim speech. The quoted question and answer appear as reported speech; no reliable diarization supports a second voice.

## Music, effects and sound transitions

Unknown: this analysis did not audition the WAV. Codec, channel count, amplitude and silence statistics cannot prove the presence or absence of music, ambience, or sound effects. No specific sound-to-image synchronization or suspense cue is asserted without listening. A final listening pass should annotate narrator onset/offset, breaths, pauses, music bed, foley/effects, and any gain or edit at scene changes.

## Reliability

- **Verified:** stream metadata, extraction, amplitude measurements, two thresholded low-level intervals, and model-generated text/timestamps.
- **Medium-confidence:** transcript phrases that broadly agree with visible captions and their time ranges.
- **Unknown:** repeated subscribe spans, verbatim wording during those spans, speaker identity/accent, music, effects, and precise voice/visual sync.
