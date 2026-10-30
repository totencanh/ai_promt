# VieNeu-TTS integration (official docs checked 2026-10-30)

## Official implementation and API

The official open-source repository identifies **VieNeu-TTS v3 Turbo** as its current open-source SDK. The official docs say cloning accepts a 3–8 second reference clip, automatically denoises/trims it to at most 8 seconds, and v3 does not require `ref_text` or fine-tuning. Documented Python interface:

```python
from vieneu import Vieneu

tts = Vieneu()  # v3 Turbo; backend auto-detects supported hardware
wave = tts.infer(
    text="Một câu thoại tiếng Việt.",
    ref_audio=str(reference_path),
    denoise=True,
)
tts.save(wave, str(output_path))
```

Use the same `reference_path` on every scene/segment. Do not pass `style`: official v3 docs say it is deprecated/ignored; the reference determines reading character. No transcript is required for the reference on v3. Generate one stable `VO-*` WAV per scene or coherent beat and map it to exact script line IDs. Review audio after each render; synthesis success is not a quality pass.

Official sources:

- SDK/repository: https://github.com/pnnbao97/VieNeu-TTS
- Voice cloning/clip requirements: https://docs.vieneu.io/docs/sdk/voice-cloning/
- Install and backend behavior: https://docs.vieneu.io/docs/sdk/standard-mode/

VieNeu’s docs say model weights download on first use and are cached under the Hugging Face cache. These files are not bundled with this Skill. If VieNeu or model weights are missing, report exact gaps and stop. Ask before packages, model downloads, or environment changes. Do not use the cloud/API as a silent fallback.

## Fixed reference audio

Canonical user reference: `/analysis/audio.wav`, relative to the active project root. Resolve it as:

```python
project_root = ...  # verify this is the user’s project root
reference_path = project_root / "analysis" / "audio.wav"
```

Do not pass a Windows-root `Path("/analysis/audio.wav")`; in the inspected project the resolved file is `<project-root>/analysis/audio.wav`. Do not overwrite, trim, replace, or silently create a substitute. Pass this exact existing source path as `ref_audio` and leave cleanup/trimming to the documented SDK. If it is missing/unreadable or VieNeu rejects its format/duration, stop and ask before preprocessing or using another file.

At Skill creation, the audio was verified as readable WAV, PCM signed 16-bit, stereo, 44.1 kHz, 135.978 s. It is longer than the recommended reference clip. Auto-trimming is documented, but the docs do not specify which section of a long recording is selected. Audition a synthesized test segment; if its voice is mixed, inconsistent, or unsuitable, stop and ask before selecting/cropping any segment. Prior analysis could not verify music, speaker changes, or all speech, so do not claim this is a clean single-speaker clip.

Only clone a voice the user is authorized to use. If the audio appears to belong to an identifiable third party and authorization is unclear, pause the voice stage for confirmation. Do not reuse the competitor’s dialogue or narration content.

## Segments and mapping

- Preserve Vietnamese diacritics and proper nouns. Normalize spoken numbers only with review.
- Keep each segment to a coherent scene/beat and sentence boundary.
- Name deterministically, e.g. `audio/voice/SC-01_VO-01.wav`.
- Record script line IDs, scene ID, exact text/version, reference path, SDK/backend version, output path, measured duration/sample rate, status, and review notes in audio plan/manifest.
- Listen to every segment for tones/pronunciation, names, rhythm, artifacts, clipping, unwanted pauses, and voice consistency. Regenerate only the affected segment and update measured edit timing.
- Do not persist cloned profiles outside the project unless the user explicitly authorizes that separate state change.

## Setup gate

Official docs describe a minimal CPU/ONNX install (`pip install vieneu`) and GPU/PyTorch options. The Windows CUDA instructions list pinned Torch/Torchaudio and Transformers versions; first use may fetch model weights. Before setup, re-check official docs and local Python/GPU/CUDA state, then present package names/versions, download/storage estimates when available, GPU use, model downloads, commands, and environment impact. Wait for explicit approval; this Skill never installs automatically.
