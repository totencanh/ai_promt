# VieNeu-TTS v3 Turbo integration notes

Read this only when the active project chooses VieNeu-TTS. Verify the current official documentation and actual local SDK/backend/model state before synthesis or setup; this note is not a guarantee that a particular machine is configured.

## Documented API

The official repository documents a Python v3 Turbo interface similar to:

```python
from vieneu import Vieneu

tts = Vieneu()  # backend selection depends on installed runtime/hardware
wave = tts.infer(
    text="Một câu thoại tiếng Việt.",
    ref_audio=str(approved_reference_path),
    denoise=True,
)
tts.save(wave, str(output_path))
```

The official v3 material describes voice cloning from a short reference and does not require a reference transcript or fine-tuning. Check the current clip requirements and API before use; do not assume automatic trimming selects a suitable part of long or mixed audio. Avoid deprecated or unsupported parameters.

Official sources:

- SDK/repository: https://github.com/pnnbao97/VieNeu-TTS
- Voice cloning: https://docs.vieneu.io/docs/sdk/voice-cloning/
- Install/backend modes: https://docs.vieneu.io/docs/sdk/standard-mode/

## Reference, rights, and setup gates

- Select a reference audio file for the active project; never assume `/analysis/audio.wav` or another path is universally valid.
- Check that the user has the right to use and clone the speaker's voice. If identity or authorization is unclear, stop the voice stage and request clarification.
- Inspect file format, duration, speech cleanliness, speaker consistency, and pronunciation before passing it to the SDK. Do not overwrite or preprocess the source without authorization.
- Verify the runtime, SDK, backend, and cached model locally. First use may download model weights.
- Before installing packages, downloading weights, changing the environment, or selecting a paid/cloud path, provide the user the requested scope, version, size estimates, hardware/backend, commands, and environment impact, then wait for explicit approval.
- Do not switch to an online API, different reference, or different voice without authorization.

## Segment and review workflow

- Generate one stable WAV per scene or coherent beat; map it to exact script line IDs and a text version.
- Preserve Vietnamese diacritics and proper nouns; add pronunciation notes for names and regional terms.
- Measure actual duration, sample rate, and channels. Replace estimated scene timing with measured VO timing during edit.
- Listen to every segment for tones, pronunciation, rhythm, consistency, artifacts, clipping, and unintended pauses. Regenerate only affected segments and update downstream timing.
- Keep source/license, engine version, backend/model, output path, and review status in the audio plan/manifest.
- Synthesis success is not listening approval. Do not mark a voice segment or mix approved until it has actually been heard and reviewed.
