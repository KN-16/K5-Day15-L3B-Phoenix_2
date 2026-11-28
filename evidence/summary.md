# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | Phép đếm ban đầu là thăm dò CP1. CP3 có thêm phép kiểm ghi quy tắc trước, chạy được lại và có 5 ví dụ từ log đã ẩn danh. | [evidence/data-mining.md](data-mining.md) |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ Chưa dùng nguồn phỏng vấn trong bộ CP2. | [Mẫu phỏng vấn](interviews/TEMPLATE.md) |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ Chưa triển khai. | `evidence/survey/` |

## 2. Số chính

- Đào data: **12/20 (60%)** học viên sai lần đầu ở mục `agentic_fit_scoring_decision` thuộc bài ôn cuối Day 03. Mẫu gồm 20 học viên có kết quả đúng hoặc sai cho lần trả lời đầu.
- Đào data, sau khi sai (CP3): phép của Huy ghi **9/12 (75%)** lượt sai có `co_feedback = True` và không có sự kiện mở bài hoặc hỏi trợ giảng về Day 03 từ mốc trả lời đến hết log. Phép mở rộng cho mọi câu ôn Day 03 ghi **10/22 (45%)**. [Cách đếm của Huy](data-mining.md)
- Kiểm cửa sổ 24 giờ (CP3): Khôi ghép được cả **12/12** lượt sai với sự kiện nộp bài. Có **2/12 (16,7%)** học viên mở lại bài hoặc video Day 03 trong 24 giờ. [Cách đếm và bản ghi đối chiếu](data-mining.md#7-khôi-kiểm-lại-mốc-nộp-bài-và-cửa-sổ-24-giờ)
- Phỏng vấn: chưa có số người gặp, số lần mỗi tháng hoặc số phút mỗi lần *(n nhỏ không ghi %)*.
- Khảo sát: chưa có số liệu.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung.

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |
| P3 | | | | | |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

Năm bản ghi nguồn dưới đây đều có `lan_thu = 1` và `was_correct = False`. Đây là ví dụ nguyên văn từ trường dữ liệu của log, ghi theo mã lượt đã ẩn danh. Trạng thái mở lại do phép kiểm CP3 tính ra.

1. `A00117` — có sự kiện mở lại trong 24 giờ.
2. `A00653` — chưa ghi nhận sự kiện mở lại trong 24 giờ.
3. `A00945` — chưa ghi nhận sự kiện mở lại trong 24 giờ.
4. `A00948` — có sự kiện mở lại trong 24 giờ.
5. `A00950` — chưa ghi nhận sự kiện mở lại trong 24 giờ.

## 4. Các nguồn có khớp nhau không

Cả hai phép CP3 dùng cùng nguồn log BTC. Tỷ lệ **2/12** đo mở bài hoặc video trong 24 giờ. Tỷ lệ **9/12** đo thiếu cả hai nhóm tín hiệu mở bài hoặc hỏi trợ giảng đến cuối log. Hồ sơ hiện có một nguồn bằng chứng.

## 5. Kết luận

Giả thuyết ở [evidence/hypothesis.md](hypothesis.md): phép đếm xác nhận có học viên sai lần đầu và ít sự kiện mở lại được ghi nhận trong cửa sổ 24 giờ. Chưa đủ căn cứ kết luận họ gặp khó khi tự tìm chi tiết quyết định đáp án. Số phút xem lại và tần suất mỗi tháng vẫn chưa đo, nên `spec.md` §2 tiếp tục là kịch bản ước tính.

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Học viên L3 ngoài nhóm đã tự ôn Day 03 | Chưa dùng lịch hẹn trong bộ CP2 | Chưa ghi nhận làm bằng chứng ở CP2 |
