> Đây là khung repo nộp bài. Điền mọi chỗ `____`, giữ nguyên tên các mục. **Mục 0 xoá đi sau khi tạo repo xong.**
> Giờ, mốc, luật, rubric: xem `README.md`, `02-guide.md`, `03-rubric.md` trong repo đề (bộ đề BTC phát).

# Phoenix_2 — Gợi ý sửa lỗi chọn workflow hay agent ở Day 03

**Thành viên, lớp, track:** xem [TEAMS.md](TEAMS.md). **Điền TEAMS.md đúng format**: khi chấm và đánh giá, BTC quét file này để ghép điểm cho từng người.

*Lát cắt = phần nhỏ nhất làm xong được trong hackathon: một người dùng · một việc · một quyết định AI · một kết quả.*

---

## Nhóm làm gì, khung làm gì

| Nhóm quyết định và viết | Khung làm sẵn (không cần sửa) |
|---|---|
| Người dùng, pain, bằng chứng, impact (`evidence/`, `spec.md` §1–§2) | — |
| Hình dạng giải pháp, công cụ, prompt, luồng (`spec.md` §4, `codebase/agent.py`, `tools.py`, `ai.py`) | Ghi mọi lần gọi model / công cụ vào trace, cộng token (`codebase/tracing.py`) |
| Bộ câu thử, metric, chuẩn "đạt" (`eval/benchmark.csv`, `eval/metric_spec.yaml`, `spec.md` §7) | Kiểm đủ cột, đủ câu `kho` / `tu_choi`, đủ ≥1/3 câu từ người dùng / data thật (`run.py check`) |
| Chấm cột `pass` theo metric spec | Chạy cả bộ một lệnh, có run ID, model, token từng câu (`run.py eval`) · tính % đạt (`run.py score`) |
| Persona, số người dùng thật, giá model (`cost/personas.yaml`) | Sinh ~50 phiên, chạy thật qua bản chạy thử, tính chi phí / phiên, / task thành công, / tháng 3 kịch bản (`run.py simulate`) |

*Ví dụ track A (ví dụ cỡ, không phải lời giải):* nhóm viết công cụ `search_lesson` tra bài pre-class đã đánh mã đoạn, luồng "tra đoạn → model trả lời kèm mã đoạn, không có thì nói không có", metric "mọi khẳng định có mã đoạn đúng", persona "ôn dồn trước kiểm tra". Khung chạy 25 câu thử ra `run-1.csv`, nhóm chấm `pass`, `score` in % đạt; `simulate` chạy 50 phiên ra chi phí / task thành công cho hai model.

## Chạy trong 3 phút

Bộ khung cần **Python 3.10 trở lên** (Python 3.9 có sẵn trên macOS vẫn chạy được, chỉ in một dòng nhắc). **Không cần `pip install`.**

**Bước 1 — Mở cửa sổ lệnh ngay trong thư mục repo**

| Windows (PowerShell) | macOS |
|---|---|
| Mở thư mục repo bằng File Explorer → bấm vào thanh địa chỉ → gõ `powershell` → Enter | Mở **Terminal** (Cmd + Space, gõ "Terminal") → gõ `cd ` (có dấu cách) → kéo thả thư mục repo vào → Enter |

Gõ `dir` (Windows) hoặc `ls` (macOS / Linux): thấy `run.py` và `README.md` là đang đứng đúng chỗ.

**Bước 2 — Kiểm Python và chạy thử**

| Việc | Windows (PowerShell) | macOS / Linux |
|---|---|---|
| Kiểm Python | `python --version` (không được thì `py --version`) | `python3 --version` |
| Chạy bản chạy thử (chế độ giả, chưa gọi model) | `python run.py` | `python3 run.py` |
| Kiểm bộ câu thử | `python run.py check` | `python3 run.py check` |
| Tạo file `.env` để nối model | `copy .env.example .env` | `cp .env.example .env` |

- Windows: gõ `python` mà mở Microsoft Store hoặc báo không có lệnh → dùng `py`. Chưa có Python: cài từ python.org, **tick "Add python.exe to PATH"**, mở lại PowerShell.
- macOS: báo `command not found: python` là bình thường → dùng `python3`.
- Ở CP2, `python run.py` hiện câu ôn Day 03. Nhập lựa chọn kèm lý do để thấy gợi ý, câu hỏi làm rõ hoặc câu nhắc phạm vi, sau đó là dòng `model: fake`. Nối model thật ở CP3 theo [docs/connect-model.md](docs/connect-model.md).

Trong README này lệnh viết là `python …`; máy nhóm cần `python3` hay `py` thì gõ thay.

## Lệnh

| Lệnh | Làm gì |
|---|---|
| `python run.py` | Chạy bản chạy thử (gõ đầu vào, nhận kết quả, kèm số lần gọi model / token) |
| `python run.py check` | Kiểm `eval/benchmark.csv` (6 cột, số câu, `kho` / `tu_choi`, mã `source`, ô trống, dòng mẫu) `eval/metric_spec.yaml` (≥3 metric điền đủ) và `TEAMS.md` (đúng format để BTC quét). Chỉ cảnh báo, không sửa file |
| `python run.py eval --try` | **Thử nối model:** chạy 3 câu đầu (`--try 5` = 5 câu) → `eval/run-try.csv`. Thấy "Nối model được" là xong. Không tính là một lượt |
| `python run.py eval` | Chạy cả bộ qua `codebase/agent.py` → `eval/run-1.csv` (lần sau `run-2.csv`…) + `traces/run-1.jsonl`. Mỗi dòng có run ID, model, số lần gọi model / công cụ, token. Model còn giả → chỉ ghi `run-mock.csv`; mọi câu lỗi → `run-error.csv`; Ctrl+C → `run-stopped.csv` — đều **không** được đánh số |
| `python run.py eval --fake` | Thử riêng bộ chạy, không gọi agent → `eval/run-fake.csv` |
| `python run.py score eval/run-1.csv` | Sau khi điền cột `pass` (1 / 0): in % đạt tổng và theo `type`. Còn ô trống → "CHƯA CHẤM XONG", không in % |
| `python run.py simulate --try` | Thử mô phỏng chi phí 10 phiên (làm trước CP3) → `cost/simulate-try.csv` |
| `python run.py simulate` | Mô phỏng chi phí khi dùng thật theo `cost/personas.yaml` (≥50 phiên) → `cost/simulate-N.csv` + `cost/simulate-N-summary.md` |
| `python run.py simulate --rate-from eval/run-2.csv` | Như trên, lấy tỉ lệ đạt từ đúng lượt chỉ định. Không ghi thì khung lấy lượt `run-N` mới nhất đã chấm, cùng model, và ghi rõ đã lấy lượt nào trong bản tóm tắt |

Gói miễn phí báo hết lượt: thêm `--wait 4` sau `eval` hoặc `simulate` (nghỉ 4 giây giữa hai lượt gọi). Sửa CSV bằng Excel: *File → Save As → CSV UTF-8*; Google Sheets: *Tệp → Tải xuống → CSV*.

**Lượt có lỗi kỹ thuật** (cột `error` có chữ): không sửa tay file đó, chạy lại thành lượt mới và ghi vào bảng các lượt ở `eval/README.md`. Không xoá file lượt nào.

Nhóm dùng stack khác (Node, Streamlit, notebook…): sửa hàm `run_app()` trong `run.py` để `python run.py` vẫn chạy được bản chạy thử, và giữ `answer()` trong `codebase/agent.py` để `eval`, `simulate` chạy được.

## Bản chạy thử — viết ở đâu

| File | Viết gì | Bước guide |
|---|---|---|
| `codebase/agent.py` | `answer(text)` — luồng chính, đúng hình dạng ở `spec.md` §4. Khung có sẵn một workflow 2 bước *ví dụ* | 3.2 |
| `codebase/tools.py` | Công cụ của bài toán, mỗi công cụ một hàm có `@tool` | 2.2, 3.2 |
| `codebase/ai.py` | `call_model(system, user)` — chỗ duy nhất gọi model. Chưa điền `.env` thì chạy **chế độ giả** | 3.3 |

- **Trước CP2:** để chế độ giả, công cụ trả dữ liệu giả — `python run.py` đi hết luồng là đủ.
- **Trước CP3:** nối model thật theo [docs/connect-model.md](docs/connect-model.md), `eval --try` thấy token > 0 rồi mới `eval`.
- Bộ chạy gửi **nguyên ô `input`** của câu thử vào `answer(text)`. Dữ liệu nền (bài học, thông báo, lịch…) để trong `data/`, đọc qua công cụ.

### Luồng của Phoenix

Học viên đọc câu ôn Day 03 (chọn workflow cố định hay agent), gõ lựa chọn kèm lý do. Luồng trong `codebase/agent.py` là workflow cố định, mỗi lượt gọi model một lần:

1. `get_lesson()` lấy câu ôn, các gợi ý đã soạn và câu áp dụng mới từ `data/day03.json` (nạp một lần).
2. `call_model()` gửi lời giải thích tới model OpenAI `gpt-6-luna` (Chat Completions). Model chỉ được trả JSON `{"action": "goi_y" | "hoi_lai" | "tu_choi", "hint_id": "<mã>"}`, và JSON Schema (Structured Outputs) giới hạn `hint_id` trong đúng các mã có ở data.
3. `check_hint()` kiểm lại mã gợi ý có thuộc câu ôn. Mã lạ, JSON hỏng hay action lạ đều chuyển sang hỏi lại, còn khi model từ chối trả lời thì hiện câu từ chối. Mỗi trường hợp đều ghi lý do vào trace.
4. Phản hồi chỉ lấy chữ từ data hoặc câu soạn sẵn. Đường gợi ý in gợi ý kèm câu áp dụng mới, đường hỏi lại xin học viên nói rõ chi tiết của đề, đường từ chối nhắc phạm vi và không đưa đáp án.

```
python run.py
```

Đầu vào mẫu để thử ba đường. Cột model thật ghi kết quả chạy ngày 27/11/2026:

| Gõ | Chế độ giả | `gpt-6-luna` |
|---|---|---|
| `Phải gọi công cụ đọc CSV nên em nghĩ cần agent.` | Gợi ý G02 + câu áp dụng mới | Gợi ý G02 + câu áp dụng mới |
| `Em nghĩ agent hợp hơn vì nó thông minh.` | Hỏi lại | Hỏi lại |
| `Cho mình đáp án luôn đi.` | Từ chối | Từ chối |

#### Nối model thật

1. Chép `.env.example` thành `.env` (Windows: `copy .env.example .env` · macOS/Linux: `cp .env.example .env`) rồi điền:
   ```
   MODEL_PROVIDER=openai
   MODEL_NAME=gpt-6-luna
   API_KEY=<key của nhóm>
   ```
   `.env` đã nằm trong `.gitignore`, không commit file này. Để trống `MODEL_PROVIDER` thì bản chạy thử quay về chế độ giả.
2. `python run.py` rồi gõ một câu: dòng cuối phải có `model: gpt-6-luna` và số token lớn hơn 0.
3. `python run.py eval --try 3`: thấy "Nối model được: có token > 0" là xong.

Gọi API lỗi (sai key, hết lượt, mất mạng, hết thời gian chờ) thì lỗi được ghi vào cột `error`, key bị che, và code không tự gọi lại. Gói bị giới hạn số lượt thì thêm `--wait 4`. Có hai biến tuỳ chọn, để trống là tắt: `REASONING_EFFORT` (gửi `reasoning_effort`) và `MAX_OUTPUT_TOKENS` (gửi `max_completion_tokens`). Lần chạy `eval --try 3` ngày 27/11/2026 đo trung bình 507 token vào, 40 token ra và 2,1 giây mỗi câu, nên nhóm chưa bật hai biến này.

## Phần nào thật, phần nào giả

| Thành phần | Thật / Giả | Ghi chú |
|---|---|---|
| Lời gọi AI ở quyết định trung tâm | **Thật** từ CP3 (CP2 dùng mock) | Model: `gpt-6-luna` của OpenAI, gọi qua Chat Completions với Structured Outputs. Chạy thử ngày 27/11/2026 bằng `eval --try 3`: 3/3 câu không lỗi, token lấy từ `usage` của API. Khi `.env` để trống `MODEL_PROVIDER`, nhánh `fake` trong `codebase/ai.py` trả cùng dạng JSON, chọn bằng từ khoá và ghi token 0. Lượt chạy bằng nhánh này không được tính. |
| Câu ôn, gợi ý, câu áp dụng mới | Nhóm tự soạn (`synthetic`) | `data/day03.json`, nguồn và giới hạn ở `data/DATA_CARD.md` |
| Kiểm mã gợi ý, hỏi lại, từ chối | Thật | Code Python trong `codebase/agent.py` và `codebase/tools.py`, chạy giống nhau ở chế độ giả và thật |

## Dùng AI vào việc gì

2–3 dòng (bắt buộc): nhóm dùng công cụ AI nào để làm gì, người kiểm lại phần nào. Chi tiết: [docs/ai-usage.md](docs/ai-usage.md). Coding agent đọc [AGENTS.md](AGENTS.md).

Codex hỗ trợ soạn tình huống mock, viết phép đếm log, soạn thêm câu thử tự viết và rà tính nhất quán giữa bằng chứng, Canvas, spec và bộ câu thử. Chuẩn đánh giá ghi ở `spec.md` §7. Bản CP2 ghi nguồn `tu_viet` cho các tình huống soạn mới. [Khai báo chi tiết](docs/ai-usage.md)

## File mẫu — điền ở bước nào

| File | Điền ở bước guide | Mốc |
|---|---|---|
| `TEAMS.md` | 1.0 | CP1 · **đúng format**, BTC quét khi chấm |
| `canvas.md` | 1.4 | CP1, cập nhật CP2 |
| `evidence/hypothesis.md` | 1.1 | trước khi tìm bằng chứng |
| `evidence/data-mining.md` · `evidence/interviews/TEMPLATE.md` → `P1.md`… · `evidence/survey/TEMPLATE.md` | 1.2 | bắt đầu sau Zoom, xong CP3 |
| `evidence/summary.md` | 1.2 | CP3 |
| `spec.md` | §0–§2: 1.1–1.3 · §3–§5: 2.1–2.3 · §7: 2.4 · §8: 4.2 · §10: suốt | §7 chốt CP2 · §0–§7 CP3 · đủ CP4 |
| `data/DATA_CARD.md` | 2.4 | bản đầu CP2 |
| `eval/benchmark.csv` · `eval/metric_spec.yaml` | 2.4 | ≥10 câu + metric chốt CP2 · 20–30 câu CP3 |
| `codebase/` | 3.2, 3.3 | khung CP2 · AI thật CP3 |
| `eval/report.md` · `eval/README.md` | 4.1 (README mục 1–4 từ 2.4) | CP4 |
| `cost/personas.yaml` · `cost/cost-estimate.md` | 4.2 | thử 10 phiên CP3 · đủ CP4 |
| `validation/log.md` *(bonus)* | 4.3 | CP4 |
| `slides/outline.md` → `demo-slides.pdf` | 5.1 | CP4 |
| `reflection/TEMPLATE.md` → `reflection/<ten>.md` | 5.3 | 23:59 Thứ Bảy 28/11 |
| `AGENTS.md` · `docs/ai-usage.md` | khi dùng coding agent / AI | suốt |

## Bảy hạng mục bắt buộc — nằm ở file nào

| # | Hạng mục | File |
|---|---|---|
| 1 | Bằng chứng pain | `evidence/` (tổng hợp ở `evidence/summary.md`) |
| 2 | Impact có số | `spec.md` §2 |
| 3 | Thiết kế giải pháp | `spec.md` §4 |
| 4 | Bản chạy thử làm trọn lát cắt | `codebase/` · lệnh ở mục "Lệnh" |
| 5 | Định nghĩa "tốt" + bộ câu thử | `data/DATA_CARD.md` · `eval/` |
| 6 | Mô phỏng chi phí khi dùng thật | `cost/` |
| 7 | Slide + demo + video dự phòng | `demo-slides.pdf` ở thư mục gốc · link video: ____ |
| + | *Bonus:* người dùng thử | `validation/log.md` |
