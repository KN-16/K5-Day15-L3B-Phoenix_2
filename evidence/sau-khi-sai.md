# Bằng chứng từ log — học viên làm gì sau khi sai câu ôn Day 03

> Huy đếm ngày 28/11/2026 (có Claude hỗ trợ viết script). Khôi tổng hợp vào `evidence/data-mining.md` và `evidence/summary.md`.
> Script: [dem_sau_khi_sai.py](dem_sau_khi_sai.py). Data: `data/preclass/` trong repo đề BTC, đặt cạnh repo Phoenix, không commit vào repo nhóm.
> Chạy lại từ thư mục gốc repo Phoenix: `python evidence/dem_sau_khi_sai.py ../K5-L3-Day15-AI-Product-Hackathon/data/preclass`

## 1. Cách đếm — viết trước khi chạy

- **Data:** `answers.csv`, `events.csv`, `chat.csv` của gói pre-class BTC (05/11–25/11/2026, UTC). Log kết thúc 25/11/2026 09:58 UTC.
- **Mẫu chính:** `lesson_id = program-day03:chatbot-to-agentic-agent`, `kc_code = agentic_fit_scoring_decision`, `nguon = pre_post_post`, `lan_thu = 1`, `was_correct` là True/False. Mỗi học viên 1 dòng (20 học viên).
- **Mốc:** `answers.created_at` của lượt trả lời đó. Chỉ giữ học viên có đủ 24 giờ sau mốc trước khi log kết thúc (cả 20 đều đủ).
- **"Mở lại bài":** `events.csv` có `type` là `lecture_opened` hoặc `video_opened`, cùng `lesson_id`, sau mốc.
- **"Hỏi trợ giảng về Day 03":** `chat.csv` có `transcript` bắt đầu `Day03`, `asked_at` sau mốc.
- **"Có xem lại":** mở lại bài hoặc hỏi trợ giảng về Day 03, bất kỳ lúc nào sau mốc.
- **Mẫu số:** số học viên trong nhóm sai (hoặc đúng) của mẫu chính.
- **Phép đếm phụ (kiểm độ vững):** cùng định nghĩa, nhưng lấy lượt sai đầu tiên của mỗi học viên ở **mọi câu** trong bài ôn cuối Day 03.

## 2. Kết quả

| Đếm gì | Nhóm sai | Nhóm đúng | Ghi chú |
|---|---|---|---|
| Đã thấy đáp án ngay sau khi trả lời (`co_feedback = True`) | 12/12 | 8/8 | Cả hai nhóm đều được xem đáp án |
| Mở lại bài hoặc video Day 03 trong 24 giờ | **2/12 (17%)** | 3/8 (38%) | |
| Hỏi trợ giảng AI về Day 03 sau mốc | 3/12 (25%) | 3/8 (38%) | Tính mọi câu hỏi dưới video Day 03 |
| **Có xem lại theo bất kỳ cách nào** | **3/12 (25%)** | 6/8 (75%) | |
| **Không xem lại** | **9/12 (75%)** | 2/8 (25%) | |

**Phép đếm phụ — mọi câu ôn Day 03:** 22 học viên sai ít nhất 1 câu; **10/22 (45%) không xem lại**, 6/22 (27%) mở lại bài trong 24 giờ. Nhóm làm đúng: 13/23 (57%) có xem lại.

## 3. Ví dụ (mã lượt đã ẩn danh, nhóm sai không xem lại)

`A00653`, `A00945`, `A00950`, `A01935`, `A02946` — mỗi dòng: `lan_thu = 1`, `was_correct = False`, `co_feedback = True`, không có `lecture_opened`/`video_opened` Day 03 và không có chat `Day03` sau mốc.

## 4. Đọc kết quả thế nào

- Ở câu workflow/agent: **9/12 học viên sai, đã thấy đáp án, rồi không quay lại bài hay hỏi trợ giảng về Day 03**, dù phần lớn vẫn hoạt động nhiều trên trang trong 24 giờ sau.
- Mở rộng ra mọi câu ôn Day 03, tỉ lệ thấp hơn: **gần một nửa (10/22)** học viên sai không xem lại. Ở mẫu rộng, nhóm sai và nhóm đúng xem lại với tỉ lệ gần nhau (12/22 so với 13/23), nên **không kết luận** được "người sai xem lại ít hơn người đúng" nói chung. Khác biệt rõ chỉ thấy ở câu workflow/agent, với n nhỏ.

## 5. Giới hạn

- n nhỏ (12 người sai ở mẫu chính).
- Chỉ thấy **hành vi**, không thấy **lý do**: không xem lại có thể do đã hiểu nhờ đáp án, vội, hoặc không biết xem lại chỗ nào → cần phỏng vấn để kiểm.
- "Mở lại bài" không phân biệt xem lại có chủ đích hay tình cờ học tiếp. "Hỏi trợ giảng về Day 03" không chắc là về đúng câu này.
- Log chỉ có đến 25/11; hành vi sau đó không thấy.
