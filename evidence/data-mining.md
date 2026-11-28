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

**Số so sánh cho hướng A1 trong `spec.md` §2.** Video `Day01/d01-r1-v02.txt` có 115 lượt hỏi từ 34 học viên phân biệt. Số này đo lượt hỏi dưới video. Thời gian học viên mất để tìm đoạn cần xem vẫn chưa đo.

```powershell
$chatPath = '../K5-L3-Day15-AI-Product-Hackathon/data/preclass/chat.csv'
$questions = @(Import-Csv -LiteralPath $chatPath -Encoding UTF8 | Where-Object {
    $_.channel -eq 'video_question' -and $_.transcript -eq 'Day01/d01-r1-v02.txt'
})
[pscustomobject]@{ LuotHoi = $questions.Count; HocVien = @($questions | Group-Object hv).Count }
```

## 4. ≥5 ví dụ cụ thể (mã dòng / mã đã ẩn danh, không đoán ai là ai)

Năm dòng đầu khi sắp xếp theo mã trong tập sai. Mỗi dòng đều có `lan_thu = 1` và `was_correct = False`.

1. `A00117`
2. `A00653`
3. `A00945`
4. `A00948`
5. `A00950`

## 5. Giới hạn của data

Data cho biết người ta **làm gì**, không cho biết **vì sao**. Log lưu kết quả nhưng thiếu nội dung câu hỏi, đáp án được chọn và lời giải thích. Tỷ lệ 60% chỉ mô tả 20 học viên trong mẫu lọc.

→ Hồ sơ CP2 dùng phép đếm log này. Cần thêm nguồn độc lập để kiểm lý do chọn đáp án và thời gian xem lại. [Tổng hợp và tiến độ](summary.md)

## 6. Phép đếm bổ sung CP3 — học viên làm gì sau khi sai

Huy đếm ngày 28/11/2026, có Claude hỗ trợ viết script. Câu hỏi: sau khi trả lời sai và đã thấy đáp án, học viên có quay lại bài hay hỏi trợ giảng không?

**Cách đếm — viết trước khi chạy**

- Data: `answers.csv`, `events.csv`, `chat.csv` của gói pre-class BTC (log kết thúc 25/11/2026 09:58 UTC).
- Mẫu chính: cùng 20 học viên ở mục 1 (`agentic_fit_scoring_decision`, `pre_post_post`, `lan_thu = 1`). Mốc là `answers.created_at`; chỉ giữ học viên có đủ 24 giờ sau mốc (cả 20 đều đủ).
- "Mở lại bài": `events.csv` có `type` là `lecture_opened` hoặc `video_opened`, cùng `lesson_id`, sau mốc.
- "Hỏi trợ giảng về Day 03": `chat.csv` có `transcript` bắt đầu `Day03`, `asked_at` sau mốc.
- "Có xem lại": mở lại bài hoặc hỏi trợ giảng về Day 03, bất kỳ lúc nào sau mốc. Mẫu số: số học viên của từng nhóm sai / đúng.
- Phép đếm phụ (kiểm độ vững): lượt sai đầu tiên của mỗi học viên ở **mọi câu** trong bài ôn cuối Day 03.
- Script: [dem_sau_khi_sai.py](dem_sau_khi_sai.py). Chạy từ gốc repo, repo đề BTC đặt cùng cấp: `python evidence/dem_sau_khi_sai.py ../K5-L3-Day15-AI-Product-Hackathon/data/preclass`

**Kết quả**

| Đếm gì | Nhóm sai | Nhóm đúng |
|---|---|---|
| Đã thấy đáp án ngay sau khi trả lời (`co_feedback = True`) | 12/12 | 8/8 |
| Mở lại bài hoặc video Day 03 trong 24 giờ | 2/12 (17%) | 3/8 (38%) |
| Hỏi trợ giảng AI về Day 03 sau mốc | 3/12 (25%) | 3/8 (38%) |
| **Không xem lại** (không mở lại bài, không hỏi về Day 03) | **9/12 (75%)** | 2/8 (25%) |

Phép đếm phụ, mọi câu ôn Day 03: **10/22 (45%)** học viên sai không xem lại; nhóm đúng có 13/23 (57%) xem lại.

Ví dụ nhóm sai không xem lại (mã lượt, `lan_thu = 1`, `was_correct = False`, `co_feedback = True`): `A00653`, `A00945`, `A00950`, `A01935`, `A02946`.

**Đọc kết quả:** ở câu workflow/agent, 9/12 học viên sai đã thấy đáp án rồi không quay lại bài hay hỏi trợ giảng về Day 03, dù phần lớn vẫn hoạt động nhiều trên trang trong 24 giờ sau. Mở rộng ra mọi câu Day 03, tỉ lệ là gần một nửa (10/22), và nhóm sai với nhóm đúng xem lại với tỉ lệ gần nhau (12/22 so với 13/23), nên **không kết luận** được người sai xem lại ít hơn người đúng nói chung.

**Giới hạn:** n nhỏ; chỉ thấy hành vi, không thấy lý do (có thể đã hiểu nhờ đáp án, vội, hoặc không biết xem lại chỗ nào); "mở lại bài" không phân biệt xem lại có chủ đích hay học tiếp; câu hỏi `Day03` không chắc về đúng câu này.

## 7. Khôi kiểm lại mốc nộp bài và cửa sổ 24 giờ

Ngày 28/11/2026, Khôi ghi quy tắc trước khi chạy phép kiểm bổ sung. Codex hỗ trợ viết và chạy lại công thức. Phép kiểm này nối `answers.id` với `events.ref_id` và cùng `hv` để lấy thời điểm `answer_submitted` sớm nhất theo `occurred_at`. Mẫu gồm học viên sai lần đầu ở mục đã lọc, có mốc nộp ghép được và đủ 24 giờ trước bản ghi cuối của `events.csv`. Mỗi học viên được tính một lần. Sự kiện mở bài hoặc video phải thuộc Day 03 và xảy ra sau mốc nộp, tối đa 24 giờ.

**Kết quả:** 12/12 lượt sai ghép được mốc nộp và cả 12 học viên có đủ cửa sổ. Có **2/12 (16,7%)** học viên có sự kiện mở bài hoặc video Day 03 trong 24 giờ. Với **10/12 (83,3%)** còn lại, log không ghi nhận hai loại sự kiện này trong khoảng đo.

| Mã lượt sai | `lan_thu` | `was_correct` | Có sự kiện mở Day 03 trong 24 giờ |
|---|---|---|---|
| `A00117` | `1` | `False` | Có |
| `A00653` | `1` | `False` | Không ghi nhận |
| `A00945` | `1` | `False` | Không ghi nhận |
| `A00948` | `1` | `False` | Có |
| `A00950` | `1` | `False` | Không ghi nhận |

Chạy từ gốc repo Phoenix trong PowerShell, với repo BTC đặt cùng cấp. Lệnh chỉ in số tổng hợp và mã lượt đã ẩn danh.

```powershell
$dataPath = '../K5-L3-Day15-AI-Product-Hackathon/data/preclass'
$lesson = 'program-day03:chatbot-to-agentic-agent'
$wrong = @(Import-Csv "$dataPath/answers.csv" -Encoding UTF8 | Where-Object {
    $_.lesson_id -eq $lesson -and $_.kc_code -eq 'agentic_fit_scoring_decision' -and
    $_.nguon -eq 'pre_post_post' -and $_.lan_thu -eq '1' -and $_.was_correct -eq 'False'
})
$wrongByRef = @{}
foreach ($row in $wrong) { $wrongByRef[$row.id] = $row.hv }
$submittedByRef = @{}
$openedByLearner = @{}
$end = [DateTimeOffset]::MinValue
foreach ($event in (Import-Csv "$dataPath/events.csv" -Encoding UTF8)) {
    if (-not $event.occurred_at) { continue }
    $time = [DateTimeOffset]::Parse($event.occurred_at)
    if ($time -gt $end) { $end = $time }
    $ref = $event.ref_id
    $learner = $event.hv
    if ($event.type -eq 'answer_submitted' -and $wrongByRef.ContainsKey($ref) -and $wrongByRef[$ref] -eq $learner) {
        if (-not $submittedByRef.ContainsKey($ref) -or $time -lt $submittedByRef[$ref]) {
            $submittedByRef[$ref] = $time
        }
    }
    if ($event.lesson_id -eq $lesson -and $event.type -in @('lecture_opened', 'video_opened')) {
        if (-not $openedByLearner.ContainsKey($learner)) {
            $openedByLearner[$learner] = [Collections.Generic.List[DateTimeOffset]]::new()
        }
        $openedByLearner[$learner].Add($time)
    }
}
$sample = @(foreach ($group in ($wrong | Group-Object hv)) {
    $first = $group.Group | Where-Object { $submittedByRef.ContainsKey($_.id) } |
        Sort-Object @{Expression = {$submittedByRef[$_.id]}}, id | Select-Object -First 1
    if ($null -eq $first) { continue }
    $start = $submittedByRef[$first.id]
    $limit = $start.AddHours(24)
    if ($limit -gt $end) { continue }
    $opened = @($openedByLearner[$first.hv] | Where-Object { $_ -gt $start -and $_ -le $limit }).Count -gt 0
    [pscustomobject]@{ id = $first.id; MoLai24h = $opened }
})
if ($sample.Count -eq 0) { throw 'Không có học viên đủ cửa sổ quan sát.' }
$count = @($sample | Where-Object MoLai24h).Count
[pscustomobject]@{ GhepDuoc = $submittedByRef.Count; LuotSai = $wrong.Count; MoLai = $count; Mau = $sample.Count; PhanTram = [math]::Round(100 * $count / $sample.Count, 2) }
$sample | Sort-Object id | Select-Object -First 5
```

Mục 6 dùng `answers.created_at` và chỉ số **9/12** kết hợp mở bài hoặc hỏi trợ giảng cho tới cuối log. Mục 7 chỉ đếm hai loại mở bài trong 24 giờ tính từ sự kiện nộp. Hai chỉ số bổ sung góc nhìn về cùng nguồn log BTC. Dữ liệu chưa cho biết học viên mở lại để sửa đúng câu nào, lý do họ chọn sai hay thời gian tốn để ôn lại. Chạy mục 7 không cần cài `pandas`.
