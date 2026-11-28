# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code | Hỗ trợ viết luồng và nhánh OpenAI, viết kiểm thử transport giả lập | Diên đọc diff, duyệt trước khi commit và kiểm CLI, eval thử, simulate thử | Diên |
| Prompt / thiết kế lời gọi mô hình | Claude Code | Hỗ trợ soạn hướng dẫn chọn phản hồi và JSON Schema | Diên duyệt quy tắc chọn dựa trên các kịch bản trong spec | Diên |
| Đào data (viết script đếm, gợi ý nhãn) | Codex | Viết công thức lọc và tổng hợp log BTC | Chạy lại phép đếm, đối chiếu mẫu số và 5 mã lượt | Khôi |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Codex | Soạn thêm tám tình huống B21–B28 để kiểm gợi ý, hỏi lại, giữ phạm vi | Ghi `tu_viet`, giữ nguyên B01–B12 và kiểm output mock | Nhóm Phoenix_2 |
| Sinh data `synthetic` (nếu có) | Codex | Soạn câu ôn CSV, gợi ý và câu áp dụng | Kiểm cấu trúc 5 mục và chạy CLI. Seed không áp dụng với bản soạn theo từng mục. | Khôi |
| Chấm cột `pass` bằng LLM (nếu có) | Codex | Hỗ trợ đối chiếu 20 phản hồi với `pass_criterion`, ghi điểm theo ủy quyền của Nhân và kiểm lại bằng `run.py score` | Nhân phụ trách kết quả đánh giá Lượt 1 và giao Codex đối chiếu theo tiêu chí đã chốt ở CP2 | Nhân |
| Slide, văn bản | Codex | Hỗ trợ soạn Canvas và spec, đối chiếu phiên bản CP1–CP2 | Giữ đúng phạm vi từ CP1, đối chiếu bằng chứng log và rà chuẩn ở §7 | Nhóm Phoenix_2 |
| Tích hợp CP3 | Codex | Hỗ trợ kiểm local, chạy lệnh đánh giá, đối chiếu hồ sơ và dựng video từ phản hồi CLI thật | Nhân phụ trách tích hợp CP3, đánh giá Lượt 1 và chuẩn bị demo | Nhân |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
