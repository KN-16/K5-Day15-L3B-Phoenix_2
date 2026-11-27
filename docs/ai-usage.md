# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Codex | Viết công thức lọc và tổng hợp log BTC | Chạy lại phép đếm, đối chiếu mẫu số và 5 mã lượt | Khôi |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Codex | Soạn thêm tám tình huống B21–B28 để kiểm gợi ý, hỏi lại, giữ phạm vi | Ghi `tu_viet`, giữ nguyên B01–B12 và kiểm output mock | Nhóm Phoenix |
| Sinh data `synthetic` (nếu có) | Codex | Soạn câu ôn CSV, gợi ý và câu áp dụng | Kiểm cấu trúc 5 mục và chạy CLI. Seed không áp dụng với bản soạn theo từng mục. | Khôi |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Codex | Soạn nháp Canvas và spec, đối chiếu phiên bản CP1–CP2 | Giữ đúng phạm vi từ CP1, đối chiếu bằng chứng log và rà chuẩn ở §7 | Nhóm Phoenix |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
