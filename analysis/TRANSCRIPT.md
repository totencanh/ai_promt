# Vietnamese audio transcript — ASR pass

## Method and confidence

Source: `audio.wav`, transcribed locally with the FFmpeg 9.0.2 `whisper` audio filter (already bundled), Vietnamese forced language, model `large-v3-turbo-q5_0` (547 MiB). Timestamps below are the filter’s millisecond timestamps converted to `mm:ss.mmm`. A 3 s queue produced severe repeated phrases and overlapping long segments; that pass is retained as `TRANSCRIPT_raw.json` for traceability but is not treated as a valid transcript. The reviewed pass used a 12 s queue and is stored as `TRANSCRIPT_retry.json`.

The longer-queue pass still repeats “Hãy subscribe cho kênh Ghiền Mì Gõ để không bỏ lỡ những video hấp dẫn” over intervals where the burned-in Vietnamese captions visibly show unrelated narration. Those spans are marked **ASR unreliable** and omitted from the clean transcript. This repeated phrase may be a model hallucination, but without direct listening it cannot be ruled out as actual audio. Other lines have likely errors, especially names and regional terms. Confidence labels mean agreement between ASR and on-screen text/timing, not human listening verification.

## Transcript excerpts with timestamps

| Time | ASR text | Confidence / note |
|---|---|---|
| 00:00.000–00:02.980 | Có một con ma mà người ta không gọi là ma, gọi bằng tên. | Medium-high: clear ASR and opening caption agree. |
| 00:02.971–00:03.411 | Tên người. | Medium-high: ASR and caption agree. |
| 00:04.311–00:04.811 | Phạm Nhan. | Medium: name is visible in caption; ASR spelling likely. |
| 00:05.943–00:47.925 | **Unresolved.** ASR repeats a subscribe phrase across this span. | Low: conflicts with changing story captions; do not use repeated phrase as verified dialogue. |
| 00:47.925–00:52.525 | Phải bôi vôi với phân gà và bồ hóng lên lưỡi gươm thì gươm mới chém được. | Medium: ASR heard “bổ hóng”; visible caption supports “bồ hóng”. |
| 00:52.525–00:55.525 | Đức Thánh Trần làm theo: “Chém được!” | Medium-high; caption and visual sequence agree. |
| 00:55.525–00:59.905 | Trước khi chém, người ta kể Ngài hỏi nó: “Mày muốn ăn gì?” | Medium-high; timing matches the held confrontation tableau. |
| 00:59.907–01:04.907 | Nó đáp: “Máu đàn bà đẻ.” | Medium; model output has a homophone error (“ba đẻ”); visible caption supports “bà đẻ”. |
| 01:04.907–01:13.548 | Ngài phán: “Vậy thì cho mày ăn thứ ấy.” Nói rồi ngài chém nó thành ba khúc, ném xuống sông cho trôi ba ngả. Câu đáp ấy thành cái án của nó. Chết rồi thì hồn đi ăn đúng thứ nó xin. | Medium; broad wording agrees with visible captions; exact spelling/name capitalization not human-checked. |
| 01:14.388–01:22.628 | Từ đó dân gian tin đàn bà mới đẻ mà xanh sao, sốt, mê sảng, da máu không cầm là bị Phạm Nhan. Bệnh ấy người ta cũng gọi luôn là bệnh Phạm Nhan. | Medium; transcript broadly agrees with captions. Some medical/folk terms may be mistranscribed. |
| 01:23.388–01:35.851 | **Unresolved.** ASR has short uncertain words followed by repeated subscribe text. | Low; captions visible during this interval describe the spirit and protective customs, but that is visual text evidence, not verified audio transcript. |
| 01:35.851–01:47.811 | Đền thờ Đức Thánh Trần xin một cái chiếu cũ. Đem về trải lén dưới chỗ bà đẻ nằm, đừng cho ai biết. Thêm nắm tro hương của đền, hòa nước cho uống. | Medium-high: ASR and captions mostly agree; normalize “nắm tro hương” from context and the on-screen wording. |
| 01:47.832–02:11.795 | **Unresolved.** ASR again repeats the same subscribe phrase over multiple caption changes. | Low; captions at 01:49–02:11 describe the remedy’s rationale and shrine, but the words were not reliably recognized from audio. |
| 02:11.795–02:12.275 | ASR: “Nằm chết.” | Low; incomplete fragment only. |
| 02:12.275–02:15.055 | Và có một câu nó tự nói ra trước lúc mất đầu. | Medium; ASR and final caption agree on the sentence; preceding clause remains unresolved. |

## Narration, dialogue and performance

- **Verified/strongly supported:** one continuous Vietnamese narration is the apparent format; quoted exchanges around 00:55–01:13 are embedded in the storyteller’s account. The transcript alone does not establish separate recorded character voices or diarization.
- **Voice quality, accent, speaking rate:** not reliably assessed because direct playback was unavailable. Some ASR segments are well aligned, but unreliable gaps prevent a defensible whole-video words-per-minute measure.
- **Silences:** FFmpeg `silencedetect` at −35 dBFS found brief low-level intervals at 01:02.061–01:02.491 and 01:32.061–01:32.491 (about 0.43 s each). These are signal-threshold pauses, not proof of absolute silence.
- **Music and sound effects:** unknown. Codec metadata, RMS, and silence detection cannot identify musical beds or discrete effects. No claims about suspense scoring are made without listening.

## How to use this transcript

Use the timestamps and medium-confidence text to align broad beats. Keep unresolved stretches explicitly unresolved; do not treat burned-in captions as proof that the same words are audible. A final human listening pass is still needed to settle the suspect repeated phrase, correct names, estimate narration pace, and inventory music/effects.
