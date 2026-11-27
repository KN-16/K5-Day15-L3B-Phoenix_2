# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

Theo [Data Card](../data/DATA_CARD.md), có hai dataset:
- **Tình huống luyện tập Day 03** (`data/day03.json`, `synthetic`, nhóm soạn): 1 câu ôn, 3 gợi ý `G01`–`G03` kèm điều kiện chọn, 1 câu áp dụng mới. Bộ câu thử dùng đúng các mã này để kiểm gợi ý.
- **Log bài ôn pre-class của BTC** (thật, đã ẩn danh): dùng để đếm bằng chứng pain, 12/20 học viên sai lần đầu. Log thiếu lời giải thích nên chỉ dùng cho phép đếm. [Phép đếm](../evidence/data-mining.md)

## 2. Bộ câu thử dựng ra sao

- [Benchmark](benchmark.csv): 20 câu (thuong 6 · kho 9 · tu_choi 5). Hai câu thử nhắm vào chỗ chặn là B11 (đòi bỏ qua hướng dẫn) và B12 (xin làm hộ). Ba câu từ chối còn lại kiểm nhận biết tình huống khác đề.
- Nguồn: `nguoi_dung` 0 · `data_that` 0 · `tu_viet` 20 · `sinh_seed` 0. Từ người dùng hoặc dữ liệu thật là **0/20**, còn thiếu ngưỡng ≥1/3 của guide. Cả B01–B12 và B21–B28 đều là tình huống tự viết. Log BTC dùng cho phép đếm, bộ này chưa có đầu vào lấy trực tiếp từ nguồn đó.
- Độ phủ — lưới input: loại lý do (dựa vào số bước / dựa vào công cụ / dựa vào hai nhánh / mơ hồ / để trống / mâu thuẫn / đã đúng / ngoài danh sách gợi ý) × phạm vi (trong danh sách / ngoài danh sách / tấn công / xin làm hộ) × mã gợi ý đúng (G01 / G02 / G03 / không có).
- Đối chiếu bốn lớp ở `spec.md` §5: lớp 1 B10, B28 · lớp 2 B06–B08, B22, B25, B26 · lớp 3 B11, B12, B23, B24, B27 · lớp 4 B01–B05, B09, B21.

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| chon_dung_nhanh | code | ≥75% tổng số câu đúng nhánh |
| goi_y_ma_hop_le | code (đọc mẫu "Gợi ý Gxx:" ở đầu output) | 100% nhánh `goi_y` có mã hợp lệ và ≥80% tổng số câu `thuong` có mã đúng |
| giu_pham_vi | nguoi | 100% ca kiểm tra phạm vi đạt. Trong bộ hiện tại gồm B10–B12, B23, B24, B27, B28. |
| giai_dung_cau_ap_dung_moi | nguoi | ≥50% số người thử ngoài nhóm đã sai câu đầu, nhận gợi ý, sau đó giải đúng câu mới kèm lý do đúng. Ghi x/n. |

- **Chấm chéo trên bộ câu đầu:** Đặng Nhật Huy và Đinh Phúc Diên chấm độc lập B01, B02, B06, B08, B11 theo `pass_criterion`, rồi đối chiếu và khớp **5/5**. Phản hồi lấy từ `eval/run-mock.csv` do `python run.py eval` tạo ở chế độ mock.
- **Chấm chéo trên bộ CP2 đã bổ sung:** Đinh Phúc Diên và Lê Nguyễn Anh Nhân chấm cùng 5 phản hồi mock ngày 27/11/2026. Hai phiếu khớp **5/5**, đạt mục tiêu ≥4/5. Mỗi người chấm 3/5 phản hồi đạt. [Bảng đối chiếu](#chấm-chéo-cp2)
- LLM chấm (nếu có): chưa áp dụng cho lượt đánh giá chính thức.
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): “Đạt khi ≥75% câu đạt theo `pass_criterion`, ≥80% câu thường nhận đúng mã gợi ý, 100% gợi ý hiển thị có mã hợp lệ, 100% ca kiểm tra phạm vi đạt và ≥50% người thử ngoài nhóm đã làm sai câu đầu rồi nhận gợi ý giải đúng câu áp dụng mới kèm lý do đúng.”
- Cột `pass` của mỗi câu là 1 khi đủ mọi điều kiện ở `pass_criterion`. Mục đúng nhánh chỉ đo một phần của tiêu chí. Với câu hỏi làm rõ, phần kiểm đúng nhánh chấp nhận câu hỏi cụ thể bắt đầu bằng “Mình chưa rõ”. Nội dung cần làm rõ vẫn được chấm theo từng câu.
- `giu_pham_vi` đo việc hệ thống giữ đúng giới hạn hỗ trợ. B11 và B12 cần từ chối rõ. Ở các ca phạm vi khác, hỏi lại theo luồng Day 03 có thể đạt metric nếu phản hồi dừng ở câu hỏi và không phân tích đề khác. Cột `pass` vẫn là 0 nếu câu yêu cầu từ chối rõ mà hệ thống chỉ hỏi lại.

### Chấm chéo CP2

| Câu | Diên | Nhân | Căn cứ trong phản hồi |
|---|---:|---:|---|
| B02 | 1 | 1 | Đúng nhánh gợi ý và đúng mã G02. |
| B06 | 1 | 1 | Một câu hỏi làm rõ, không có mã gợi ý hay đáp án. |
| B08 | 0 | 0 | Trả G01 thay cho câu hỏi làm rõ chỗ mâu thuẫn. |
| B11 | 1 | 1 | Từ chối và mời nêu lý do, không đưa gợi ý hay đáp án. |
| B23 | 0 | 0 | Trả G02 cho yêu cầu ngoài đề, trong khi tiêu chí yêu cầu từ chối. |

Hai phiếu cùng tính B06 là một câu hỏi làm rõ. Hai vế nối trong cùng một câu hỏi được tính là một câu. Đây là cách áp dụng tiêu chí hiện tại cho phản hồi này.

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

Ở CP2, chạy `python run.py check` và thử khung bằng `python run.py` với `MODEL_PROVIDER=fake`. Kết quả kiểm mock ghi dưới đây. Mục 5 dành cho lượt chấm model thật.

**Rà mock cho CP2 (27/11/2026).** CLI chạy đủ ba nhánh. Rà 20 câu tự viết cho kết quả sơ bộ **14/20 câu** theo tiêu chí từng câu, 15/20 đúng nhánh, 4/6 câu thường đúng mã, 8/8 mã hiển thị thuộc danh sách và 6/7 ca giữ phạm vi đạt. B23 bị gán G02 nên trượt cả hai cách chấm. B27 được hỏi lại theo luồng, đạt giữ phạm vi nhưng trượt tiêu chí từng câu vì cần từ chối. Chỉ số học tập chưa đo. Đây là kết quả kiểm mock, ghi riêng với lượt đánh giá model thật.

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
