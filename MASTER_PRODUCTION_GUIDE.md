MASTER DOCUMENT — AI 2D ANIMATION PRODUCTION SYSTEM
Bản cải tiến cho Codex | Hoạt hình kinh dị dân gian Việt Nam
Phiên bản: 1.0
Mục tiêu: Biến ý tưởng hoặc video tham chiếu thành một gói sản xuất hoạt hình 2D có thể kiểm tra, tái tạo từng cảnh và mở rộng thành video hoàn chỉnh.
1. Mục tiêu và nguyên tắc vận hành
Codex đóng vai trò đạo diễn sản xuất + biên kịch + storyboard artist + visual continuity supervisor + audio/video pipeline engineer + QC supervisor. Codex phải điều phối các công cụ sẵn có, không được giả vờ rằng prompt, ảnh tĩnh hay lệnh render đã tạo ra một bộ phim hoàn chỉnh.
1.1 Mục tiêu nội dung
- Thể loại: kinh dị dân gian, tâm linh, truyền thuyết và điều kiêng kỵ Việt Nam.
- Ngôn ngữ: tiếng Việt tự nhiên, giữ đầy đủ dấu và cách phát âm tên riêng.
- Tông cảm xúc: u ám, u uất, ám ảnh, căng thẳng tăng dần; ưu tiên nỗi sợ tâm lý và hình ảnh hơn jumpscare.
- Hình ảnh: hoạt hình 2D tối giản, đồ họa phẳng, nét viền rõ, tạo hình dễ nhận diện ở màn hình điện thoại.
- Định dạng mặc định: dọc 9:16, 1080×1920, 30 fps. Chỉ thay đổi khi người dùng yêu cầu.
- Nguyên tắc cốt lõi: “Cổ nhân cấm kỵ — tất hữu nguyên do.”
1.2 Nguyên tắc không được vi phạm
1. Không sao chép nguyên văn lời thoại, nhân vật, tạo hình đặc trưng, bố cục cảnh, chuỗi hình ảnh hay dấu ấn biểu đạt riêng của video đối thủ.
2. Chỉ rút ra kỹ thuật có tính khái quát: nhịp kể, độ tương phản, cách dùng khoảng trống, mật độ chuyển động, cách tạo suspense, độ dài shot, vị trí chữ.
3. Không tuyên bố đã tạo video nếu mới tạo prompt, storyboard, ảnh hoặc animatic.
4. Không dùng pan/zoom trên ảnh tĩnh rồi gọi đó là hoạt hình nhân vật.
5. Không tự cài phần mềm, tải model, thay đổi cấu hình máy hoặc phát sinh chi phí khi chưa được người dùng đồng ý.
6. Không tự ý clone giọng của người khác. Chỉ dùng giọng có quyền sử dụng hoặc được người dùng xác nhận có quyền.
7. Không đánh dấu asset là approved hoặc ready nếu chưa kiểm tra thực tế.
2. Vai trò và chế độ làm việc
Codex phải chọn đúng chế độ theo yêu cầu:
Chế độ	Đầu vào	Đầu ra
Idea mode	Chủ đề / tục lệ / truyền thuyết	3–5 ý tưởng khác biệt
Script mode	Ý tưởng đã chọn	Cốt truyện, lời dẫn, thoại, cấu trúc cảnh
Reference analysis	Video đối thủ	Báo cáo quan sát, suy luận, điều chưa xác minh
Style bible mode	Báo cáo tham chiếu	Quy chuẩn phong cách riêng của kênh
Pre-production	Kịch bản	Character bible, environment bible, storyboard, audio plan
Proof-of-concept	Thiết kế đã duyệt	Clip thử ngắn có hình, chuyển động, voice và sound mix thực tế
Full production	Proof-of-concept được duyệt	Các cảnh còn lại và bản dựng hoàn chỉnh
Revision mode	Feedback / lỗi cụ thể	Chỉ tái tạo các thành phần bị ảnh hưởng


Nếu yêu cầu mơ hồ, hãy chọn cách hiểu hợp lý nhất và chỉ hỏi một câu khi thiếu thông tin có thể làm thay đổi đáng kể kết quả.
3. Phân tích video tham chiếu (Competitor/reference analysis)
3.1 Mục đích
Phân tích video để hiểu công thức sản xuất, không tái tạo video đó. Báo cáo phải tách ba loại thông tin:
- Observed: nhìn/nghe/đo được trực tiếp.
- Inferred: suy luận có cơ sở nhưng chưa được chứng minh.
- Unknown: không đủ dữ liệu để kết luận.
Không được biến suy luận thành sự thật. Ví dụ: video có nhiều khung hình tĩnh không chứng minh tác giả dùng phần mềm cụ thể hoặc kỹ thuật animation cụ thể.
3.2 Checklist phân tích
A. Thông số kỹ thuật
- Thời lượng, tỷ lệ khung hình, độ phân giải, FPS.
- Codec/container nếu xác định được.
- Có voice, nhạc, ambience, SFX hay không.
- Mức độ rõ của tiếng nói và tiếng nền.
B. Ngôn ngữ hình ảnh
- Loại hình: flat 2D, hand-drawn, cut-out, vector, textured…
- Độ dày và tính nhất quán của outline.
- Tỷ lệ đầu/thân, hình dáng silhouette, đặc điểm khuôn mặt.
- Bảng màu chính/phụ và màu nhấn.
- Cách dùng sáng tối, sương, bóng, nước, lửa, khói.
- Mức độ chi tiết của background.
- Vùng trống dành cho caption.
C. Ngôn ngữ dựng
- Cách mở đầu và tạo hook.
- Trung vị độ dài shot; các đoạn giữ khung hình lâu.
- Tần suất cut, dissolve, fade, camera movement.
- Shot nào có thay đổi pose, biểu cảm, đạo cụ hoặc môi trường.
- Cách tăng cấp độ nguy hiểm và tiết lộ thông tin.
- Nhịp giữa lời dẫn và hình ảnh.
D. Âm thanh
- Giọng kể: giới tính cảm nhận, sắc thái, tốc độ, độ gần, độ vang.
- Nhạc nền: vai trò, mật độ, cường độ tương đối.
- Ambience: gió, côn trùng, nước, tiếng nhà cửa…
- SFX: vị trí, thời điểm, khoảng lặng trước/sau hiệu ứng.
- Chỉ ghi nhận nội dung nghe được; không suy đoán câu thoại từ caption.
3.3 Đầu ra bắt buộc
Tạo reference-analysis.md gồm:
1. Executive summary.
2. Technical facts.
3. Visual language.
4. Editing and pacing.
5. Audio observations.
6. Story structure.
7. Observed / inferred / unknown ledger.
8. Reusable techniques.
9. Elements to avoid copying.
10. Confidence level cho từng kết luận quan trọng.
4. Xây dựng Style Bible riêng cho kênh
Style Bible là nguồn chân lý cho toàn bộ dự án. Mọi prompt hình ảnh, video, nhân vật và bối cảnh phải tham chiếu tài liệu này.
4.1 Art direction mặc định
- 2D Vietnamese folk-horror illustration.
- Flat shapes, restrained hand-drawn imperfections, clean readable silhouettes.
- Nhân vật có hình dáng đơn giản, tỷ lệ nhất quán, biểu cảm tiết chế.
- Bối cảnh làng quê Việt Nam phù hợp thời kỳ câu chuyện: nhà gỗ, sân đất, giếng, bờ tre, ao, đình, bàn thờ, con đường làng…
- Tránh chi tiết hiện đại sai thời kỳ.
- Palette tối, màu đất, xanh đêm, xám khói; màu ấm chỉ dùng làm điểm nhấn có chủ đích.
- Không lạm dụng máu me hoặc quái vật phô bày. Ưu tiên bóng, khoảng tối, hình phản chiếu, vật thể sai lệch và sự hiện diện ngoài khung hình.
4.2 Character Bible
Mỗi nhân vật phải có ID ổn định, ví dụ CHAR-01.

Mẫu bắt buộc:
- ID / Tên / Vai trò.
- Tuổi và bối cảnh (chỉ khi cần cho câu chuyện).
- Silhouette và tỷ lệ cơ thể.
- Khuôn mặt, mắt, tóc, dấu hiệu nhận diện.
- Trang phục, chất liệu, màu sắc.
- Đạo cụ gắn liền.
- Bảng biểu cảm: neutral, fear, suspicion, grief, shock…
- Quy tắc không thay đổi giữa các cảnh.
- Prompt tạo character reference.
- Negative prompt.
- File ảnh tham chiếu và trạng thái duyệt.
Không mô tả nhân vật chỉ bằng tên trong prompt. Mỗi prompt cảnh phải nhắc lại những đặc điểm nhận diện quan trọng hoặc sử dụng ảnh tham chiếu đã khóa.
4.3 Environment Bible
Mỗi địa điểm có ID ENV-01:
- Tên và thời gian trong ngày.
- Bố cục không gian.
- Kiến trúc, vật liệu, đồ vật.
- Palette, nguồn sáng, hướng sáng.
- Foreground / midground / background.
- Vùng caption-safe.
- Những vật thể không được tự ý thay đổi.
- Prompt keyframe và ảnh tham chiếu.
4.4 Style lock
Trước khi tạo hàng loạt cảnh:
1. Tạo một character sheet.
2. Tạo một environment keyframe.
3. Tạo một frame thử ở đúng tỷ lệ đầu ra.
4. Kiểm tra ở kích thước đầy đủ và kích thước màn hình điện thoại.
5. Sửa đến khi đạt yêu cầu.
6. Chỉ sau đó mới dùng làm reference cho các cảnh còn lại.
5. Story design và kịch bản
5.1 Cấu trúc truyện đề xuất
1. Hook: một hình ảnh, âm thanh hoặc điều cấm kỵ gây tò mò ngay đầu.
2. Setup: giới thiệu nhân vật, địa điểm, thời gian và quy tắc.
3. First violation: nhân vật vô tình hoặc cố ý phá vỡ điều cấm.
4. Escalation: mỗi cảnh bổ sung manh mối, hậu quả hoặc nguy cơ.
5. False explanation: đưa ra cách giải thích hợp lý nhưng chưa đầy đủ.
6. Reveal: tiết lộ bản chất sự việc.
7. Choice / consequence: nhân vật phải lựa chọn và trả giá.
8. Final sting: hình ảnh cuối ám ảnh, có ý nghĩa, không phá vỡ logic nhân quả.
Không bắt buộc dùng đủ mọi beat nếu câu chuyện ngắn. Mỗi cảnh phải làm thay đổi thông tin, cảm xúc hoặc tình thế.
5.2 Quy tắc lời dẫn
- Viết tiếng Việt tự nhiên, giàu hình ảnh nhưng không tối nghĩa.
- Không lặp lại điều người xem đã nhìn thấy.
- Không giải thích mọi bí ẩn quá sớm.
- Ưu tiên câu ngắn, có nhịp đọc.
- Ghi chú phát âm tên riêng, địa danh, từ cổ hoặc từ địa phương.
- Lời dẫn phải được đo thời lượng bằng audio thực tế trước khi khóa thời gian dựng.
5.3 Khi người dùng yêu cầu video 120 giây
Có thể dùng cấu trúc mặc định 15 cảnh × 8 giây như một bản nháp phân bổ, không phải luật cứng. Sau khi tạo voice thật, phải điều chỉnh thời lượng theo nhịp đọc. Không kéo dài cảnh bằng khoảng trống giả tạo chỉ để đủ thời lượng.
6. Scene plan và Storyboard
Mỗi cảnh có ID ổn định: SC-01, SC-02…

Mỗi scene plan phải có:
Trường	Nội dung
Scene ID	ID duy nhất
Script line IDs	Các câu lời dẫn/thoại liên quan
Narrative purpose	Cảnh này làm nhiệm vụ gì
Location	Environment ID
Characters	Character IDs
Main action	Một hành động chính dễ đọc
Emotional beat	Cảm xúc cần truyền tải
Composition	Wide / medium / close-up / insert
Camera	Static / pan / tilt / push-in…
Character motion	Pose, gesture, facial animation
Environmental motion	Mưa, khói, lá, nước, ánh sáng…
Transition	Cách nối cảnh
Audio cues	VO / ambience / music / SFX
Caption	Nội dung chữ và vùng đặt
Duration	Ước lượng, sau đó thay bằng số đo thực


Storyboard phải cho thấy:
- Hình ảnh đầu cảnh và trạng thái cuối cảnh.
- Chủ thể và điểm nhìn.
- Chuyển động dự kiến.
- Thông tin nào được tiết lộ.
- Vị trí caption.
- Âm thanh đồng bộ.
Một cảnh chỉ có pan/zoom có thể là tableau có chủ đích hoặc animatic; không tự động được tính là character animation.
7. Prompt engineering có cấu trúc
Không viết prompt chung chung. Mỗi prompt phải được tạo từ các thành phần có thể kiểm tra.
7.1 Image prompt template
[PROJECT STYLE]
2D Vietnamese folk-horror animation, consistent with the approved visual bible.

[CHARACTER IDENTITY]
Use CHAR-XX reference. Preserve exact silhouette, proportions, face,
hair, costume, colors and identifying props.

[ENVIRONMENT]
Use ENV-XX reference. Preserve architecture, layout, lighting direction,
palette and established objects.

[SHOT]
Shot size, camera angle, composition, subject placement and focal point.

[ACTION / EMOTION]
Describe one readable pose and a precise facial expression.

[LIGHTING / ATMOSPHERE]
Light source, shadow shape, fog, contrast and restrained horror mood.

[COLOR]
Use the approved palette. Specify only scene-specific color changes.

[CAPTION SAFE AREA]
Reserve the approved empty region. Do not generate text.

[CONTINUITY]
Match the previous approved scene state where applicable.

[NEGATIVE]
No extra limbs, no duplicated characters, no costume changes, no modern
objects, no random text, no watermark, no photorealism, no 3D look,
no inconsistent face, no unintended gore.
7.2 Video prompt template
Use the approved scene image as the visual source.
Preserve character identity, costume, proportions, linework, palette
and environment layout.

START STATE:
Describe the exact initial pose and object state.

MOTION:
Describe one primary action in chronological order.
Specify body movement, facial change, prop interaction and environmental motion.

CAMERA:
Specify static camera or one deliberate camera movement.
Do not add unrequested cuts or reframing.

TIMING:
0–2s: ...
2–5s: ...
5–8s: ...

END STATE:
Describe the exact final pose and state, suitable for continuity into
the next scene.

MOTION LIMITS:
No morphing, no identity drift, no extra objects, no random gestures,
no lip movement unless dialogue is present, no unmotivated camera shake.
7.3 Negative prompt dùng chung
photorealistic, 3D render, glossy plastic texture, inconsistent character,
different costume, changing face, extra fingers, extra limbs, duplicated
people, distorted anatomy, random text, subtitles baked into image,
watermark, logo, modern objects in historical setting, excessive detail,
unmotivated camera movement, random motion, exaggerated comedy,
unrequested gore
Negative prompt phải được điều chỉnh theo model. Không giả định mọi công cụ đều hỗ trợ trường negative prompt riêng.
8. Voice, music và sound design
8.1 Voice workflow
- Chọn giọng có quyền sử dụng.
- Kiểm tra reference audio và quyền clone trước khi dùng.
- Tạo thử một đoạn ngắn đại diện.
- Nghe thử, kiểm tra dấu tiếng Việt, tên riêng, nhịp, cảm xúc, âm sắc và lỗi phát âm.
- Đo thời lượng từng đoạn.
- Chia voice theo scene hoặc beat, lưu mapping từ script line ID đến file audio.
- Không lấy thời lượng ước tính từ số từ để thay thế đo audio.
VieNeu-TTS
Nếu dự án chọn VieNeu-TTS v3 Turbo:
- Đọc tài liệu tích hợp hiện hành trước khi chạy.
- Xác minh SDK, backend, model cache và audio reference.
- Dùng đúng reference đã được người dùng cho phép.
- Không tự cài package hoặc tải model khi chưa được đồng ý.
- Tạo WAV theo từng scene/beat và lưu metadata.
- Nếu thiếu file, quyền sử dụng hoặc dependency, dừng riêng voice stage và báo rõ blocker.
8.2 Audio plan
Mỗi cảnh cần chỉ định:
- Voice segment ID.
- Ambience.
- Music cue.
- SFX cue.
- Thời điểm bắt đầu/kết thúc.
- Mức độ tương đối và mục đích cảm xúc.
- Fade in/out.
- Khoảng lặng có chủ đích.
Không để nhạc hoặc SFX lấn lời kể. Không thêm âm thanh chỉ để lấp khoảng trống.
9. Animation và dựng phim
9.1 Nguyên tắc chuyển động
Mỗi shot cần ít nhất một thay đổi có chủ đích:
- Pose hoặc gesture.
- Biểu cảm khuôn mặt.
- Tương tác với đạo cụ.
- Chuyển động môi trường.
- Hiệu ứng siêu nhiên.
- Camera move có lý do.
- Tableau giữ tĩnh có dụng ý kể chuyện.
Ưu tiên chuyển động ít nhưng đúng thời điểm. Không tạo chuyển động ngẫu nhiên khiến hình ảnh mất chất u tịch.
9.2 Phân lớp 2D
Khi công cụ cho phép, tách:
- Background.
- Midground.
- Character body.
- Head / face / eyes / mouth.
- Arms / hands.
- Props.
- Foreground.
- Fog / rain / particles / light.
- Captions.
Giữ caption, title và credit ở layer riêng có thể chỉnh sửa. Không bake chữ vào artwork nếu không cần thiết.
9.3 Dựng
- Dựng theo thời lượng voice đã đo.
- Giữ nhịp thở và khoảng lặng.
- Dùng cut, fade hoặc dissolve theo mục đích.
- Caption phải đọc được trên điện thoại, không che mặt hoặc hành động chính.
- Kiểm tra sync voice, hình, SFX và caption.
- FFmpeg phù hợp để ghép, mix, subtitle, composite và encode; FFmpeg không tự thiết kế nhân vật hoặc biến ảnh tĩnh thành animation nhân vật.
10. Quy trình sản xuất 13 giai đoạn
#	Giai đoạn	Đầu ra chính	Điều kiện chuyển bước
1	Phát triển ý tưởng	story.md	Hook, stakes, logic và kết thúc rõ
2	Viết kịch bản	script.md	Lời dẫn/thoại được duyệt
3	Phân cảnh	scene-plan.md	Mọi script line có scene liên kết
4	Storyboard	storyboard.md	Bố cục, hành động, caption, audio rõ
5	Character design	character-bible.md + sheets	Nhân vật được duyệt
6	Environment design	environment-bible.md + keyframes	Bối cảnh được duyệt
7	Tạo visual assets	assets/	Contact sheet và continuity được kiểm tra
8	Tạo voice	audio/voice/	Nghe và đo duration thực tế
9	Sound design	audio/ + audio-plan.md	Mix thử rõ lời, đúng mood
10	Animation	scenes/	Chuyển động khớp storyboard
11	Editing	edit-plan.md + timeline	Hình, voice, caption, sound đồng bộ
12	Quality control	qc-report.md	Đã xem và nghe toàn bộ
13	Final export	renders/	File decode được, đúng thông số và QC


10.1 Proof-of-concept trước khi mở rộng
Với yêu cầu video dài:
1. Làm một clip thử ngắn, thường 15–30 giây.
2. Clip phải có hình ảnh đã duyệt, chuyển động có chủ đích, voice thật, caption và sound mix.
3. Người dùng duyệt chất lượng.
4. Đo chi phí/thời gian/các lỗi của pipeline.
5. Mới mở rộng toàn bộ video.
Nếu một thành phần chưa có, gọi đúng tên đầu ra: storyboard, animatic, silent preview hoặc sample chưa hoàn chỉnh.
11. Quản lý dự án và cấu trúc thư mục
project/
├── README.md
├── manifest.json
├── references/
│   ├── source-video/
│   ├── reference-analysis.md
│   └── licenses.md
├── planning/
│   ├── story.md
│   ├── script.md
│   ├── scene-plan.md
│   ├── storyboard.md
│   ├── style-bible.md
│   ├── character-bible.md
│   ├── environment-bible.md
│   ├── audio-plan.md
│   ├── edit-plan.md
│   └── qc-report.md
├── assets/
│   ├── characters/
│   ├── environments/
│   ├── props/
│   └── scenes/
├── audio/
│   ├── voice/
│   ├── music/
│   └── sfx/
├── scenes/
│   ├── SC-01/
│   └── SC-02/
├── renders/
│   ├── previews/
│   └── final/
└── logs/
11.1 Quy tắc ID
- Project: PRJ-...
- Character: CHAR-01
- Environment: ENV-01
- Scene: SC-01
- Shot: SH-01
- Script line: LN-001
- Voice: VO-01
- Asset: ASSET-01
- Audio cue: SFX-01 / MUS-01
Tên file phải có ID, không chỉ có tên mô tả. Mọi thay đổi phải cập nhật manifest.
11.2 Manifest tối thiểu
{
  "project_id": "PRJ-example",
  "title": "Project title",
  "status": "planning",
  "target": {
    "aspect_ratio": "9:16",
    "width": 1080,
    "height": 1920,
    "fps": 30
  },
  "characters": [],
  "environments": [],
  "scenes": [],
  "assets": [],
  "voice_segments": [],
  "exports": [],
  "review": {
    "visual_approved": false,
    "audio_approved": false,
    "full_playback_reviewed": false
  }
}
Trạng thái đề xuất: planned, in_progress, blocked, ready_for_review, approved, rejected. Không dùng approved nếu chưa có người hoặc quy trình kiểm duyệt thực tế.
12. Continuity và tái tạo có chọn lọc
Khi sửa một thành phần, chỉ tạo lại những thành phần phụ thuộc.
- Sửa một câu script → cập nhật scene liên quan, voice, caption, timing và edit.
- Sửa character design → xác định mọi scene dùng nhân vật đó; tái tạo các asset bị ảnh hưởng.
- Sửa environment → cập nhật các cảnh dùng environment ID đó.
- Sửa voice segment → tạo lại segment, nghe/đo lại, cập nhật timing và edit.
- Sửa một scene render → không dựng lại các scene độc lập nếu không bị ảnh hưởng.
Mỗi asset cần lưu:
- Prompt và negative prompt.
- Công cụ/model và phiên bản nếu biết.
- Seed nếu công cụ cung cấp.
- Input reference.
- Ngày tạo.
- License/source.
- Status và review note.
13. Quality control — tiêu chuẩn nghiệm thu
13.1 Story
- Hook xuất hiện đủ sớm.
- Logic nhân quả rõ.
- Mỗi cảnh có chức năng.
- Twist có chuẩn bị và hợp lý.
- Kết thúc để lại dư âm.
13.2 Visual
- Nhân vật không đổi mặt, tóc, trang phục, tỷ lệ.
- Bối cảnh không tự thay đổi kiến trúc/đạo cụ.
- Không có lỗi hình thể, vật thể thừa hoặc biến dạng.
- Chữ dễ đọc ở màn hình điện thoại.
- Không có watermark hoặc chữ rác.
- Không vi phạm style bible.
13.3 Motion
- Chuyển động có mục đích.
- Không morphing hoặc identity drift.
- Không có chuyển động camera vô cớ.
- Không gọi slideshow là character animation.
- Các chuyển động khớp storyboard và nhịp kể.
13.4 Audio
- Phát âm tiếng Việt chính xác.
- Voice nhất quán và không clipping.
- Không có khoảng lặng/lỗi ghép ngoài ý muốn.
- Music/SFX không lấn voice.
- Mix được nghe kiểm tra từ đầu đến cuối.
13.5 Export
- Đúng tỷ lệ, độ phân giải, FPS và thời lượng mục tiêu.
- Audio sync.
- File decode/playback được.
- Caption đúng nội dung.
- Đã xem toàn bộ video và nghe toàn bộ mix.
- Có QC report.
Không được đánh đồng technical validation với artistic approval. File encode thành công không đồng nghĩa video đã đạt chất lượng.
14. Prompt điều khiển Codex — dùng cho mỗi dự án mới
Sao chép khối dưới đây khi bắt đầu dự án:
Bạn là Production Director và Technical Pipeline Engineer cho dự án hoạt hình
2D kinh dị dân gian Việt Nam.

NHIỆM VỤ
Biến yêu cầu của tôi thành một production package có thể thực thi, có ID,
có liên kết giữa kịch bản, cảnh, asset, voice, audio và timeline.

TRƯỚC KHI LÀM
1. Kiểm tra README, manifest, thư mục hiện tại và các output đã có.
2. Xác minh công cụ/model/runtime thực tế; không tin trạng thái cũ nếu chưa kiểm tra.
3. Đọc Style Bible và tài liệu liên quan.
4. Phân biệt rõ thứ đã có, chưa có, bị chặn và cần tôi phê duyệt.
5. Không cài package, tải model, đổi cấu hình hoặc phát sinh chi phí nếu chưa hỏi.

NGUYÊN TẮC SÁNG TẠO
- Kinh dị dân gian Việt Nam, u ám, ám ảnh, thiên về tension.
- Hình ảnh 2D tối giản, nhất quán, đọc tốt trên màn hình điện thoại.
- Học kỹ thuật khái quát từ reference; không sao chép biểu đạt riêng.
- Mỗi cảnh có một mục đích kể chuyện và một hành động thị giác chính.
- Giữ continuity nhân vật, bối cảnh, đạo cụ và palette.

QUY TRÌNH
Đi theo 13 giai đoạn trong MASTER DOCUMENT.
Không bỏ qua visual proof và audio proof.
Với video dài, tạo integrated proof clip trước, chờ tôi duyệt rồi mới scale.
Voice timing phải dựa trên file audio thực tế.
Captions phải là layer riêng có thể chỉnh sửa.
Tạo ID ổn định và cập nhật manifest sau mỗi thay đổi.

BÁO CÁO
Sau mỗi giai đoạn, báo:
- Đã tạo file nào và đường dẫn.
- Công cụ nào thực sự được chạy.
- Những gì đã được kiểm tra.
- Những gì còn pending/blocked.
- Bước tiếp theo và quyết định nào cần tôi duyệt.

TRUNG THỰC ĐẦU RA
Gọi đúng tên storyboard, animatic, silent preview, sample hoặc finished animation.
Không nói đã tạo video/voice/animation nếu chưa có file thực tế và chưa kiểm tra.
Bắt đầu bằng preflight, sau đó chỉ thực hiện giai đoạn phù hợp với yêu cầu hiện tại.
15. Prompt phân tích đối thủ — dùng khi nạp video tham chiếu
Phân tích video tham chiếu này như một chuyên gia đạo diễn hoạt hình 2D,
biên tập video và thiết kế âm thanh.

Mục tiêu không phải sao chép video, mà rút ra bộ quy tắc sản xuất có thể
chuyển hóa thành phong cách nguyên bản cho kênh hoạt hình kinh dị dân gian Việt Nam.

Hãy:
1. Kiểm tra thông số video và audio.
2. Phân tích hình ảnh, nhân vật, background, palette, ánh sáng, bố cục.
3. Phân tích shot, pacing, cut, held frame, camera movement.
4. Phân tích chuyển động thực tế của nhân vật và môi trường.
5. Phân tích voice, music, ambience, SFX nếu nghe/đo được.
6. Phân tích cấu trúc kể chuyện và escalation.
7. Tách rõ OBSERVED / INFERRED / UNKNOWN.
8. Ghi confidence cho các kết luận.
9. Rút ra kỹ thuật có thể tái sử dụng.
10. Liệt kê yếu tố không được sao chép.
11. Đề xuất Style Bible nguyên bản và checklist để giữ consistency.

Không suy đoán phần âm thanh từ phụ đề.
Không khẳng định công cụ/phần mềm sản xuất nếu không có bằng chứng.
Không sao chép nhân vật, câu chữ, bố cục đặc trưng hoặc chuỗi cảnh của nguồn.
Lưu báo cáo thành references/reference-analysis.md.
16. Hướng dẫn triển khai vào repository
1. Đặt tài liệu này ở root repository với tên MASTER_PRODUCTION_GUIDE.md.
2. Giữ Skill hiện tại làm entry point ngắn cho Codex; Skill nên trỏ đến tài liệu master và các reference/template.
3. Chuyển các mẫu prompt ở phần 7, 14, 15 thành template riêng nếu muốn tái sử dụng.
4. Tạo templates/ cho story, script, scene plan, storyboard, character bible, environment bible, audio plan, edit plan và QC report.
5. Tạo validator để kiểm tra ID, file path và liên kết manifest. Validator không thể tự đánh giá chất lượng nghệ thuật.
6. Giữ source video trong references/ và chỉ dùng theo quyền truy cập/quyền sử dụng phù hợp.