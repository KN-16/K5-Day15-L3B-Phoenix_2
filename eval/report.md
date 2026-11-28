# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-080812` | 19/20 | 95% | 6/6 | 8/9 | 5/5 | Đạt các ngưỡng kỹ thuật, chỉ số học tập chưa đo. |
| 2 | `run-2@20261128-124119` | 20/20 | 100% | 6/6 | 9/9 | 5/5 | Đạt các ngưỡng kỹ thuật, chỉ số học tập chưa đo. |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

- Lượt 1 dùng `gpt-6-luna`, ghi token từ API ở đủ 20 câu và có 0 lỗi kỹ thuật. Đối chiếu phản hồi cho thấy 20/20 đúng nhánh, 6/6 câu thường đúng mã, 6/6 mã hiển thị hợp lệ và 7/7 ca giữ phạm vi đạt. Điểm tổng hợp dùng cột `pass` của CSV, còn chỉ số học tập dùng kết quả người thử ngoài nhóm.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Hỏi lại thiếu chi tiết theo tình huống | 1 | B08 |

Lượt 1 có **một câu trượt, B08**. Hai dòng B09 và B26 ghi hạn chế của câu hỏi chung khi rà đầu ra, điểm của hai câu vẫn là `pass=1` theo tiêu chí CP2.

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| B08 | Chọn agent dù lý do nói rằng đề đã quy định rõ các bước. | “Mình chưa rõ chi tiết nào trong đề khiến bạn chọn như vậy. Bạn chọn workflow cố định hay agent, và dựa vào chi tiết nào của đề?” | Nhánh hỏi lại đúng, nhưng không nêu mâu thuẫn giữa hai ý như `pass_criterion` yêu cầu. |
| B09 | Chọn workflow cố định và giải thích rằng mỗi trường hợp đã có bước xử lý được định trước. | Hỏi lại “Bạn chọn workflow cố định hay agent, và dựa vào chi tiết nào của đề?” | Câu hỏi lặp lại lựa chọn và lý do mà học viên đã cung cấp. Hạn chế về ngữ cảnh, vẫn đạt yêu cầu chấm là hỏi lại và không nêu mã. |
| B26 | Chọn agent vì thấy vừa có nhiều bước vừa có công cụ đọc CSV. | Hỏi chung “Bạn chọn workflow cố định hay agent, và dựa vào chi tiết nào của đề?” | Câu hỏi chưa chỉ rõ cần phân biệt giữa hai lý do đã nêu. Vẫn đạt yêu cầu có câu hỏi làm rõ, không đưa mã hay đáp án. |

## 3. Một lần cải tiến

- Nhắm vào lỗi hỏi lại quá chung. Học viên đã nêu hai ý trái nhau cần biết chính xác chỗ nào phải tự xem lại.
- Workflow giữ một lần gọi `gpt-6-luna`. Model có thêm lựa chọn `hoi_lai_mau_thuan` trong JSON Schema. Python chọn câu hỏi soạn sẵn chỉ ra mâu thuẫn và vẫn dùng câu hỏi chung cho lý do mơ hồ.
- Câu B08 từ 0/1 lên 1/1. Tổng từ 19/20 (95%) lên 20/20 (100%). Giữ đúng mã 6/6 câu thường và 7/7 ca giữ phạm vi.
- Không có câu giảm điểm trên lượt này. B08 Lượt 2 nhận câu hỏi “Mình chưa rõ vì sao bạn chọn agent khi các bước đã được định sẵn. Chi tiết nào trong đề khiến bạn nghĩ hệ thống phải tự chọn bước tiếp theo?”. Trace ghi `action=hoi_lai_mau_thuan`, `hint_id` rỗng. [CSV](run-2.csv) · [Trace](../traces/run-2.jsonl)

## 4. Còn lại

- Bộ thử còn 0/20 đầu vào từ người dùng hoặc dữ liệu thật. Đạt 20/20 trên bộ tự viết vẫn cần kiểm ngoài bộ với lời giải thích thật.
- Nếu có thêm một tuần, thu lời giải thích đã ẩn danh, đo tỷ lệ tự giải câu áp dụng kèm lý do và thử rút gọn lời nhắc để đo token.

## 5. Thử nhiều model trên bản CP3

Thử từng cấu hình một lượt trên cùng code CP3 (`360b64a`), cùng 20 câu và cùng tiêu chí. Mốc Luna lấy từ Lượt 1. Bảng này giải thích slide 7. Lượt 2 ở §1 giữ Luna và thay đổi nhánh hỏi lại.

| Model | Run ID | Đạt | Điểm đáng chú ý |
|---|---|---:|---|
| `gpt-6-luna` | `run-1@20261128-080812` | 19/20 (95%) | Mốc CP3, trượt B08. |
| `gpt-4o` | `run-2@20261128-122627` | 19/20 (95%) | Trượt B08. |
| `gpt-5.1` | `run-2@20261128-122715` | 19/20 (95%) | Trượt B08. |
| `gpt-4o-mini` | `run-2@20261128-122651` | 17/20 (85%) | Trượt B04, B08, B09. |
| `gpt-5-nano` | `run-2@20261128-123241` | 9/20 (45%) | Trả gợi ý ở cả 5 câu cần từ chối. |

[Đầu vào, phản hồi và điểm từng câu của bốn lượt thử đổi model](model-comparison.csv). Các mẫu nhỏ này dùng để quan sát lỗi trên benchmark, chưa đo chất lượng học tập.
