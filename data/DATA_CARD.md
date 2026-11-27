# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · Tình huống luyện tập Day 03 cho bản mock

| | |
|---|---|
| Dùng để làm gì | Nguồn cho luồng mock chọn gợi ý và đưa câu áp dụng mới. Tệp [day03.json](day03.json) có `question`, `hints` (`id`, `when`, `text`) và `follow_up_question`. |
| Từ đâu | Tình huống và gợi ý do Codex soạn cho bản nháp, dựa trên phần mô tả workflow cố định và agent trong [guide BTC §2.2](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/b568b951dfc0342e84c357bd09405d8e7040ebb6/02-guide.md#b2-2). |
| Xử lý những bước gì | Soạn hai tình huống, mô tả ba lỗi suy luận dự kiến và gán mã `G01`–`G03`. Tệp chỉ chứa dữ liệu soạn mới. Đã kiểm cấu trúc của cả 5 mục, phần nội dung chờ Khôi duyệt. |
| Số dòng / số đoạn | 1 câu ôn, 3 gợi ý kèm điều kiện chọn, 1 câu áp dụng. |
| Phiên bản / ngày lấy | Bản nháp CP2 `v0.1` ngày 27/11/2026. |
| Nhãn | `synthetic` · soạn theo từng mục, seed không áp dụng. |
| Giới hạn | Phạm vi là một kỹ năng Day 03, hai tình huống có các bước xử lý đã định sẵn. Cần đối chiếu với phần bài Day 03 được phép dùng và lời giải thích thật trước khi chốt rubric. |

**Data `synthetic` (nhóm tự sinh):** ghi cách sinh (prompt / script), seed, người kiểm, số dòng đã kiểm tay. Data tự dựng **không phải bằng chứng pain**.

## Dataset 2 · Log trả lời bài ôn pre-class của BTC

| | |
|---|---|
| Dùng để làm gì | Đào bằng chứng về lỗi sai ở lần đầu trong bài ôn Day 03. |
| Từ đâu | `data/preclass/answers.csv` trong [gói pre-class của BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/tree/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass). |
| Xử lý những bước gì | Lọc mục `agentic_fit_scoring_decision` thuộc Day 03, nguồn `pre_post_post`, lần thử đầu và kết quả đúng/sai. Đếm học viên phân biệt. Lưu số tổng hợp và năm mã lượt đã ẩn danh. [Cách đếm và kết quả](../evidence/data-mining.md). |
| Số dòng / số đoạn | 3.776 bản ghi nguồn. Mẫu đã lọc có 20 bản ghi của 20 học viên, trong đó 12 lượt sai (60%). |
| Phiên bản / ngày lấy | Gói BTC 05/11–25/11/2026 theo UTC, commit `b568b95`. Chạy lại phép đếm ngày 27/11/2026. |
| Nhãn | Thật · log hành vi đã được BTC ẩn danh. |
| Giới hạn | Có kết quả đúng/sai, thiếu nội dung câu hỏi và lý do chọn đáp án. Số 60% áp dụng cho mẫu đã lọc. |
