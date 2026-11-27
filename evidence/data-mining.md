# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Ôn lại: ngày 2, ngày 6 · lab ngày 2, lab ngày 6.
> Không đào data thì xoá file này. Script / công thức đếm để trong repo (vd `evidence/count.py` hoặc ghi công thức Sheets ngay dưới), người khác chạy lại phải ra cùng số.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ — không chép lại nguyên file data.

## 1. Cách đếm — viết TRƯỚC khi chạy

Quy tắc bên dưới ghi lại phép đếm thăm dò đã dùng ở CP1. Nhóm chạy lại cho CP2 để kiểm tra kết quả.

- Data dùng: `data/preclass/answers.csv` của BTC, từ 05/11 đến 25/11/2026 theo UTC, trong [gói dữ liệu pre-class](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/tree/b568b951dfc0342e84c357bd09405d8e7040ebb6/data/preclass).
- Đếm gì: học viên trả lời sai lần đầu ở mục `agentic_fit_scoring_decision`. Lọc `lesson_id = program-day03:chatbot-to-agentic-agent`, `nguon = pre_post_post`, `lan_thu = 1` và `was_correct` là `True` hoặc `False`.
- **Mẫu số là gì:** số học viên phân biệt (`hv`) có lần trả lời đầu với kết quả đúng hoặc sai trong mục đã lọc. Mẫu này có đúng một bản ghi cho mỗi học viên.
- Script / công thức: chạy đoạn PowerShell sau từ thư mục gốc repo Phoenix, với repo BTC đặt cùng cấp.

```powershell
$answersPath = '../K5-L3-Day15-AI-Product-Hackathon/data/preclass/answers.csv'
$sample = @(Import-Csv -LiteralPath $answersPath -Encoding UTF8 | Where-Object {
    $_.lesson_id -eq 'program-day03:chatbot-to-agentic-agent' -and
    $_.kc_code -eq 'agentic_fit_scoring_decision' -and
    $_.nguon -eq 'pre_post_post' -and $_.lan_thu -eq '1' -and
    $_.was_correct -in @('True', 'False')
})
$total = @($sample | Group-Object hv).Count
if ($total -eq 0 -or $total -ne $sample.Count) {
    throw 'Kiểm tra lại bộ lọc và số dòng trên mỗi học viên.'
}
$wrong = @($sample | Where-Object was_correct -eq 'False').Count
[pscustomobject]@{ Sai = $wrong; Dung = $total - $wrong; Tong = $total; PhanTramSai = 100 * $wrong / $total }
$sample | Where-Object was_correct -eq 'False' | Sort-Object id | Select-Object -First 5 id, lan_thu, was_correct
```

## 2. Đọc trước, đếm sau

Khi rà lại phép đếm CP1, đã đọc 40 dòng đầu và đối chiếu `column_dictionary.csv`. Các *kiểu* hành vi thấy được:
- 26 dòng nhắn trợ giảng (`chat`) và 12 dòng làm bước thực hành (`thuc_hanh`). Hai nguồn này được lọc ra khi đếm kết quả bài ôn cuối ngày.
- 2 dòng bài ôn cuối ngày (`pre_post_post`). Các trường `lan_thu` và `was_correct` dùng để lấy lần trả lời đầu có kết quả đúng hoặc sai.

## 3. Kết quả

| Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|
| Học viên trả lời sai lần đầu | 12 / 20 | 60% | Chỉ mục `agentic_fit_scoring_decision` của Day 03. |
| Học viên trả lời đúng lần đầu | 8 / 20 | 40% | Cùng mẫu ở trên. Các bản ghi trong mẫu trải từ 10/11 đến 24/11/2026 theo UTC. |

Ghi dạng "x/N (y%)". "Nhiều bạn…" không phải số.

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

Năm dòng đầu khi sắp xếp theo mã trong tập sai. Mỗi dòng đều có `lan_thu = 1` và `was_correct = False`.

1. `A00117`
2. `A00653`
3. `A00945`
4. `A00948`
5. `A00950`

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Log lưu kết quả nhưng thiếu nội dung câu hỏi, đáp án được chọn và lời giải thích. Tỷ lệ 60% chỉ mô tả 20 học viên trong mẫu lọc.

→ Dự kiến hỏi ít nhất ba học viên ngoài nhóm đã làm bài ôn Day 03 về lựa chọn của họ, chi tiết họ xem lại sau khi biết kết quả và việc họ đã làm tiếp. Chưa có ghi chép cuộc phỏng vấn để đối chiếu.
