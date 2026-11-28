# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Tình huống luyện tập Day 03

| | |
|---|---|
| Dùng để làm gì | Nguồn cho `get_lesson()` và `check_hint()` để chọn gợi ý và đưa câu áp dụng mới, từ mock CP2 đến model thật CP3. Tệp [day03.json](day03.json) có `question`, `hints` (`id`, `when`, `text`) và `follow_up_question`. |
| Từ đâu | Tình huống và gợi ý tự soạn với hỗ trợ của Codex, dựa trên phần mô tả workflow cố định và agent trong [guide BTC §2.2](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/02-guide.md#b2-2). |
| Xử lý những bước gì | Soạn hai tình huống, mô tả ba lỗi suy luận dự kiến và gán mã `G01`–`G03`. Kiểm cấu trúc cả 5 mục và dùng cùng dữ liệu để chạy thử mock CP2 và OpenAI CP3. |
| Số dòng / số đoạn | 1 câu ôn, 3 gợi ý kèm điều kiện chọn, 1 câu áp dụng. |
| Phiên bản / ngày lấy | Bản CP2 `v0.1` ngày 27/11/2026, dùng tiếp ở CP3. |
| Nhãn | `synthetic` · soạn theo từng mục, seed không áp dụng. |
| Giới hạn | Phạm vi là một kỹ năng Day 03, hai tình huống có các bước xử lý đã định sẵn. Các lỗi suy luận dự kiến chưa được kiểm chứng bằng lời giải thích gốc của học viên. |

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Log pre-class của BTC

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng lỗi sai lần đầu và kiểm hành vi ghi nhận sau khi trả lời ở Day 03. |
| Từ đâu | `answers.csv`, `events.csv` và `chat.csv` trong [gói pre-class của BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/tree/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass). |
| Xử lý những bước gì | Lọc mục `agentic_fit_scoring_decision` ở lần thử đầu và đếm theo học viên. Phép CP3 nối mốc nộp bài và kiểm sự kiện mở lại trong 24 giờ. Phép đo riêng có thêm tín hiệu hỏi trợ giảng đến hết log. Repo lưu số tổng hợp và ví dụ ẩn danh. [Cách đếm và kết quả](../evidence/data-mining.md) |
| Số dòng / số đoạn | `answers.csv` có 3.776 bản ghi. Mẫu CP2 có 20 học viên, trong đó 12 sai lần đầu (60%). Mẫu sai của phép kiểm CP3 có đủ 12 lượt ghép được mốc nộp. |
| Phiên bản / ngày lấy | Gói BTC 05/11–25/11/2026 theo UTC, commit `b568b95`. Chạy lại phép đếm ngày 27/11 ở CP2 và kiểm thêm ngày 28/11 ở CP3. |
| Nhãn | Thật · log hành vi đã được BTC ẩn danh. |
| Giới hạn | Log ghi kết quả và sự kiện, thiếu nội dung câu hỏi và lý do chọn đáp án. Sự kiện mở lại không đo được mục đích hay số phút ôn lại. Số 60% áp dụng cho mẫu đã lọc. |
