# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-080812` | 19/20 | 95% | 6/6 | 8/9 | 5/5 | Đạt các ngưỡng kỹ thuật, chỉ số học tập chưa đo. |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

- Lượt 1 dùng `gpt-6-luna`, ghi token từ API ở đủ 20 câu và có 0 lỗi kỹ thuật. Đối chiếu phản hồi cho thấy 20/20 đúng nhánh, 6/6 câu thường đúng mã, 6/6 mã hiển thị hợp lệ và 7/7 ca giữ phạm vi đạt. Điểm tổng hợp dùng cột `pass` của CSV, còn chỉ số học tập dùng kết quả người thử ngoài nhóm.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Hỏi lại thiếu chi tiết theo tình huống | 1 | B08 |

**Lỗi cụ thể:** B08 thiếu chi tiết mà điều kiện chấm yêu cầu.

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B08 | Chọn agent dù lý do nói rằng đề đã quy định rõ các bước. | “Mình chưa rõ chi tiết nào trong đề khiến bạn chọn như vậy. Bạn chọn workflow cố định hay agent, và dựa vào chi tiết nào của đề?” | Nhánh hỏi lại đúng, nhưng không nêu mâu thuẫn giữa hai ý như `pass_criterion` yêu cầu. |

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
