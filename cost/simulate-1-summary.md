# Tóm tắt mô phỏng simulate-1@20261128-124424

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 32 | 1 | 562 | 57 | 1.0 | 1.4 |
| dung_vua | 16 | 2 | 1129 | 113 | 2.0 | 2.4 |
| dung_nhieu | 2 | 3 | 1704 | 172 | 3.0 | 4.5 |

Tỉ lệ đạt dùng để tính: 20/20 (100%) — lượt run-2@20261128-124119

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (350 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-6-luna (vào 0.1 · ra 0.5 $/1M) | $0.00012 | $0.00012 | $0.000085 | $0.0803 | $0.1605 | $0.2293 | $0.00023 |
| gpt-6.2-sol (vào 2.0 · ra 10.0 $/1M) | $0.0024 | $0.0024 | $0.0017 | $1.61 | $3.21 | $4.59 | $0.0046 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (1.4) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-6-luna. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
