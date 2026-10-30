# Video metadata

## Source and verification

- Requested path `reference/competitor_sample.mp4` was absent because the project directory contains `references/` (plural). The readable source used was `references/competitor_sample.mp4` (2,128,642 bytes). The source was preserved.
- Container: MP4 / ISO Base Media (`isom` family), probe score 100.
- Duration: 135.978 s (about 2:15.98); video stream duration 135.933 s.
- Frame size: 576 × 1024 pixels; square pixels; portrait 9:16.
- Frame rate: 30/1 fps, progressive.
- Video: H.264/AVC High, `yuv420p`, reported video bitrate about 86.5 kb/s.
- Audio: AAC HE-AACv2, 44.1 kHz, 2 channels, stereo, reported bitrate about 32.1 kb/s.
- Container bitrate: about 125.2 kb/s.
- FFprobe reports 4,078 video frames and 2,932 audio frames. Stream frame counts need not be comparable because audio frames represent codec packets.

## Workflow and artifacts

FFmpeg/FFprobe 9.0.2 were available; Python 3.11.8 had Pillow, NumPy, SciPy, and Matplotlib. OpenCV, librosa, and soundfile were unavailable and were not installed. FFmpeg produced 45 frames at 3-second intervals, a scene-change candidate set, and `audio.wav` (44.1 kHz stereo PCM). `analysis/frames/` contains labeled contact sheets and frame extracts. The scene filter emitted candidates at approximately 5.23, 15.33, 23.37, 31.67, 35.70, 92.47, and 99.30 s. These mark large image changes, not guaranteed editorial cuts.

The sampled frames are representative, not a frame-by-frame audit. A 3-second interval can miss brief gestures, mouth changes, or effects. Playback/audio listening and Vietnamese ASR were unavailable in this workflow; audio-specific claims below are intentionally limited to the stream and signal measurements.

## Extended follow-up

The approved Whisper model `models/ggml-large-v3-turbo-q5_0.bin` (574,041,195 bytes) was downloaded and used through the FFmpeg Whisper filter already present in the build; no Python packages or other software were installed. A 12-second queue produced the review transcript in `TRANSCRIPT_retry.json`; see `TRANSCRIPT.md` for reliability limitations. Scene review was extended to 136 frames at 1 fps, 18 before/after checks, FFmpeg `scdet` at thresholds 4 and 8, and `freezedetect` across all 30 fps frames.
