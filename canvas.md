# Canvas — Phoenix_2 · Track A

> Điền ở guide bước 1.4. CP1 17:00 Thứ Sáu 27/11: nộp bản đầu, đủ 7 dòng (dòng 4 được ghi giả thuyết + nguồn sẽ kiểm).
> CP2 19:30 Thứ Sáu 27/11: cập nhật (số bằng chứng đầu, lát cắt đã chốt) và điền dòng "Đã đổi gì so với CP1".
> Track F: chép thêm thẻ đề của nhóm (khung trong file track F) xuống dưới bảng này.

| # | Dòng | Nhóm điền |
|---|---|---|
| 1 | Track + lát cắt dự kiến | **A · EdTech (A4)** - Gợi ý sửa lỗi chọn workflow hay agent ở Day 03 |
| 2 | Người dùng chính (một vai cụ thể — không phải "học viên nói chung") | Học viên L3 đang tự ôn Day 03 trên pre-class, vừa làm sai câu về khi nào nên dùng workflow cố định hay agent |
| 3 | Pain một câu: ai — đang làm gì — vướng đâu — hậu quả | Khi chọn sai giữa workflow cố định và agent trong bài ôn Day 03, học viên L3 có thể chưa biết cần xem lại chi tiết nào trong đề để sửa cách chọn ở câu tương tự|
| 4 | Bằng chứng đầu — CP1: giả thuyết + nguồn sẽ kiểm · CP2: số đầu tiên + 1 trích dẫn | Log BTC ghi **12/20 học viên (60%) sai lần đầu** ở mục `agentic_fit_scoring_decision` của Day 03. Một bản ghi ẩn danh trong mẫu là `A00117`, có `lan_thu = 1` và `was_correct = False`. Log chưa cho biết lý do học viên chọn sai. [Phép đếm và ví dụ](evidence/data-mining.md) |
| 5 | **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả) | Một học viên vừa làm sai câu ôn Day 03 nêu lý do chọn workflow hay agent, rồi nhận một gợi ý do AI chọn từ bộ gợi ý đã soạn để tự giải một câu tương tự. |
| 6 | AI tự làm đến đâu + 1 dòng lý do: sai thì ai chịu gì | Luồng thiết kế chọn một mã gợi ý, hỏi lại khi lý do còn mơ hồ, hoặc nhắc phạm vi khi đầu vào lệch đề. Gợi ý lệch có thể củng cố cách hiểu sai, nên hệ thống kiểm mã và lấy nội dung phản hồi từ dữ liệu đã soạn. CP2 dùng mock ở bước chọn phản hồi. |
| 7 | Phân công có tên | **Lê Nguyễn Anh Khôi** — Tổng hợp bằng chứng, soạn dữ liệu mock, tính impact và nộp checkpoint.<br>**Đinh Phúc Diên** — Xây luồng chọn gợi ý theo lời giải thích của học viên và tích hợp OpenAI.<br>**Đặng Nhật Huy** — Xây bộ câu thử, metric và hồ sơ đánh giá.<br>**Lê Nguyễn Anh Nhân** — Tổng hợp spec và Canvas, phụ trách mô phỏng chi phí. |
| — | *(CP2)* Đã đổi gì so với CP1 | Đã ghi phép đếm log để kiểm lại số 12/20 và thu hẹp bản chạy thử vào một câu ôn CSV với ba mã gợi ý. Đã chạy luồng mock và soạn bộ câu thử cho các nhánh gợi ý, hỏi lại và từ chối. |
