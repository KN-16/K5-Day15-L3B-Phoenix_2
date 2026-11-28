# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): ít/vừa/nhiều lần lượt 60%/30%/10%, 1/2/3 phiên mỗi tháng và 1/2/3 lượt hỏi mỗi phiên. Các tỷ trọng và tần suất là tự ước tính.
- **Quy mô giả định** thấp 350 · cơ sở 700 · cao 1.000 người hoạt động. Tham chiếu quy mô L3 trên 700 học viên và toàn khóa trên 1.000 theo guide BTC §4.2.
- **Đơn giá USD trên 1 triệu token** từ bảng BTC ngày 25/11/2026. `gpt-6-luna` vào 0,10, ra 0,50. `gpt-6.2-sol` vào 2,00, ra 10,00. [Giá OpenAI](https://developers.openai.com/api/docs/pricing)
- **Tỉ lệ đạt** dùng để tính là 20/20 (100%) từ `run-2@20261128-124119`, cùng model Luna.
- Token đo trên `gpt-6-luna`. Hàng `gpt-6.2-sol` lấy token và tỷ lệ Luna để so mức giá.

## 2. Kết quả mô phỏng

Lượt mô phỏng [simulate-1.csv](simulate-1.csv) · `simulate-1@20261128-124424` · 50 phiên, 0 lỗi · seed 42. [Tóm tắt từ runner](simulate-1-summary.md)

*(dán bảng từ `cost/simulate-N-summary.md`)*

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp | / tháng — cơ sở | / tháng — cao | / người / tháng (cơ sở) |
|---|---|---|---|---|---|---|
| `gpt-6-luna` | $0.00012 | $0.00012 | $0.0803 | $0.1605 | $0.2293 | $0.00023 |
| `gpt-6.2-sol` (áp giá lên token Luna) | $0.0024 | $0.0024 | $1.61 | $3.21 | $4.59 | $0.0046 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

## 3. So với impact

- Impact tiềm năng là 5 phút/người/tháng theo giả định minh họa ở `spec.md` §2. Thời gian tiết kiệm thực tế chưa đo.
- Chi phí model `gpt-6-luna` ở kịch bản cơ sở là $0.00023/người/tháng, khoảng $0.1605/tháng cho 700 người hoạt động.
- **Kết luận:** Chi phí model đủ thấp để thử trong một nhóm nhỏ. Quyết định triển khai rộng cần số đo thời gian và khả năng áp dụng sau khi nhận gợi ý.

## 4. *(Muốn sâu hơn, không bắt buộc)*

- Bảng độ nhạy: model rẻ hơn · cache · cắt ngữ cảnh · giới hạn bước — mỗi cần gạt đổi chi phí bao nhiêu
- Chi phí ngoài model: hosting, lưu trữ, giờ công người duyệt
- Quy mô nào thì bài toán còn đáng làm
