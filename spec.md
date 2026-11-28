# AI SPEC — Gợi ý sửa lỗi chọn workflow hay agent ở Day 03 · Nhóm Phoenix_2 · Phòng D305 (CP2) · Zone chờ BTC

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — hướng A4, học từ lỗi sai trong bài ôn Day 03.
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `answers.csv`, `events.csv` và `chat.csv` trong `data/preclass/`. Các phép đếm ghi tại [evidence/data-mining.md](evidence/data-mining.md). Câu ôn CSV dùng trong bản thử được soạn riêng và ghi nguồn ở [Data Card](data/DATA_CARD.md).

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại theo log BTC: (1) học viên mở bài ôn cuối Day 03 trên pre-class, (2) gửi lượt trả lời, (3) hệ thống ghi kết quả đúng/sai. Giao diện phản hồi và việc học viên làm tiếp sau khi biết mình sai chưa được đối chiếu trực tiếp. [Mô tả dữ liệu của BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/tree/main/data/preclass)
- Công cụ / AI đang được dùng cho việc này: pre-class có trợ giảng dưới video theo [mô tả Track A1 của BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/main/tracks/track-a-edtech.md#a1--tutor-cho-lms-và-trang-pre-class). Việc trợ giảng tham gia lúc xem kết quả bài ôn Day 03 chưa kiểm.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính: học viên L3 đang tự ôn Day 03 trên pre-class, vừa làm sai câu chọn giữa workflow cố định và agent.
- Việc họ cố làm xong: tìm chi tiết quyết định cách chọn workflow hay agent để tự làm được câu tương tự trong bài ôn Day 03.
- Cách học viên tự xem lại sau khi biết kết quả còn chưa kiểm chứng. Giả thuyết của nhóm là học viên có thể mất công tìm lại chi tiết phân biệt hai cách làm hoặc lặp lại cách chọn cũ. [Giả thuyết](evidence/hypothesis.md)
- Pain: Khi chọn sai giữa workflow cố định và agent trong bài ôn Day 03, học viên L3 có thể chưa biết cần xem lại chi tiết nào trong đề để sửa cách chọn ở câu tương tự.
- Bằng chứng: **12/20 học viên (60%)** sai lần đầu ở mục `agentic_fit_scoring_decision` trong log. Bằng chứng hiện có xác nhận số câu sai trong mẫu. Lý do tự sửa khó và thời gian mất mỗi lần còn thiếu số đo. [Tổng hợp bằng chứng](evidence/summary.md)
- CP3: trong 12 học viên trả lời sai, log ghi **2/12 mở lại bài hoặc video Day 03 trong 24 giờ** tính từ lúc nộp. Phép kiểm khác ghi **9/12** không có sự kiện mở lại hoặc hỏi trợ giảng về Day 03 từ mốc trả lời đến hết log. Hai phép đo dùng cùng nguồn, với cửa sổ và hành vi khác nhau. [Cách đếm và ví dụ](evidence/data-mining.md)

## §2. Impact & quyết định chọn *(guide 1.3)*

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| A4 · Gợi ý sau lỗi chọn workflow hay agent | 12/20 sai lần đầu ở một mục trong log Day 03 | 1 lượt/người (*tự ước tính*) | 5 phút (*tự ước tính*) | 60 phút/tháng trong kịch bản 12 người | Có. Bản CP3 chạy một câu ôn với model thật. | Chọn |
| A1 · Chỉ đến đoạn cần xem trong video Day 01 | 34 người có 115 lượt hỏi trên một video. Chưa đo ai gặp khó khi tìm đoạn. | Chưa đo | Chưa đo | Chưa tính | Có thể làm khung cho một video. | Để sau |
| A5 · Soạn nháp thông báo đổi phòng lab | Chưa có mẫu người dùng thật. Bộ lịch BTC là giả lập. | Chưa đo | Chưa đo | Chưa tính | Cần đối chiếu nguồn lịch và hỏi key coach. | Để sau |

- **Impact / tháng** minh họa là 12 người sai trong mẫu log × 1 lượt xem lại/người/tháng (*tự ước tính*) × 5 phút/lượt (*tự ước tính*) = **60 phút/tháng**. Đây là kịch bản để tính thử, chưa đo thời gian thực tế hoặc tác động toàn khóa. [Phép đếm](evidence/data-mining.md)
- Hướng ĐÃ LOẠI + vì sao: A1 có số lượt hỏi, chưa đo thời gian người dùng tìm đoạn. A5 có dữ liệu demo, còn thiếu bằng chứng từ người vận hành. A4 có tín hiệu lỗi sai ở đúng kỹ năng và có thể thu hẹp bản thử về một câu ôn.
- Số lần / tháng của từng kiểu người dùng (dùng cho persona ở §8): chưa có tần suất tháng được đo. Một lượt/người/tháng là giả định ban đầu cho nhóm gặp lỗi.
- CP3: các sự kiện mở lại cho biết lượt hành vi, chưa đo số phút xem lại hoặc thời gian tiết kiệm. Mức 60 phút/tháng vẫn là kịch bản minh họa.

## §3. Giải pháp tương tự *(guide 2.1)*
- Tài liệu BTC mô tả trợ giảng pre-class trả lời sát bài và hỏi lại khi lời hỏi mơ hồ. Phoenix áp dụng cách hỏi lại đó sau thao tác chọn đáp án: thu lý do lựa chọn, chỉ một dấu hiệu để học viên xem lại, rồi đưa câu áp dụng. Chưa thử đối chiếu trực tiếp trên giao diện pre-class. [Mô tả Track A của BTC](https://github.com/VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon/blob/main/tracks/track-a-edtech.md)

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): Một học viên vừa làm sai câu ôn Day 03 nêu lý do chọn workflow hay agent, rồi nhận một gợi ý do AI chọn từ bộ gợi ý đã soạn để tự giải một câu tương tự.
- Phạm vi: một câu ôn CSV, ba gợi ý đã soạn và một câu áp dụng. Ngoài phạm vi là chấm điểm LMS, tạo lời giải hoàn chỉnh, tra cứu tài liệu ngoài bộ câu, và sửa dữ liệu hệ thống đào tạo.
- **Sơ đồ** (Mermaid):

  ```mermaid
  flowchart TD
      A["Học viên nhập lựa chọn và lý do"] --> B["get_lesson đọc câu ôn và điều kiện chọn G01–G03"]
      B --> C["call_model · OpenAI gpt-6-luna chọn action và hint_id theo JSON Schema"]
      C --> D{"Kiểm action và mã gợi ý"}
      D -->|"goi_y và mã hợp lệ"| E["Hiện gợi ý và câu áp dụng mới"]
      D -->|"hoi_lai_mau_thuan và hint_id rỗng"| H["Chỉ ra mâu thuẫn và hỏi một câu"]
      D -->|"hoi_lai hoặc action hoặc mã không hợp lệ"| F["Hỏi một câu để làm rõ"]
      D -->|"tu_choi hoặc model từ chối"| G["Nhắc phạm vi và mời quay lại câu ôn"]
  ```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent. Trình tự lấy dữ liệu, chọn phản hồi và kiểm trước khi hiển thị đã biết trước. Một lần chọn `action` và `hint_id` đủ cho lát cắt, còn việc mở công cụ và hiển thị do Python điều khiển.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `get_lesson()` | Rỗng | Câu ôn, ba gợi ý (`id`, `when`, `text`) và câu áp dụng từ JSON | Đọc cục bộ |
  | `check_hint(hint_id)` | Mã gợi ý do model chọn | Bản ghi đã soạn tương ứng, hoặc `None` nếu mã ngoài danh sách | Đọc cục bộ |

- **Mức tự động:** [x] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm. Học viên tự chọn lại cách hiểu và tự làm câu áp dụng. Gợi ý sai có thể củng cố lỗi hiểu bài.
- **Chỗ chặn rủi ro:** Parse `action` và `hint_id`, kiểm mã thuộc `data/day03.json` trước khi hiện gợi ý. Mã không hợp lệ hoặc JSON lỗi chuyển sang hỏi lại. Phản hồi hiển thị lấy từ dữ liệu hoặc câu mẫu do nhóm viết. Bước này kiểm được mã hợp lệ, còn việc mã có phù hợp với ý của học viên được đo riêng.
- **Chỗ người duyệt:** Nhóm kiểm rubric và nội dung gợi ý trước khi đưa vào dataset. Người chấm dùng tiêu chí trong hồ sơ đánh giá để kiểm các phản hồi và bài làm câu áp dụng.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Chuyển sang câu hỏi làm rõ khi lời giải thích mơ hồ hoặc mã sai. Kiểm bằng B06, B07, B22, B26. |
  | G1 — nói rõ làm được gì | Lời mở đầu CLI chỉ rõ câu ôn và yêu cầu nhập lựa chọn kèm lý do. Khi lệch phạm vi, câu từ chối mời quay lại đúng câu. Kiểm bằng B11, B12, B23. |
  | G11 — giải thích gắn với việc làm tiếp | Gợi ý G01–G03 nêu chi tiết cần xem lại, sau đó CLI hiện câu áp dụng. Kiểm bằng B01–B05, B21. |

- Phần nào còn giả: câu ôn về CSV và các gợi ý trong `data/day03.json` là `synthetic`. Khung CP2 dùng mock từ khóa. Bản CP3 gọi `gpt-6-luna` qua OpenAI Chat Completions ở bước chọn phản hồi, dùng Structured Outputs giới hạn nhánh và mã, rồi Python kiểm mã lần nữa. API từ chối thì dùng câu từ chối cố định. Lỗi kết nối hoặc phản hồi thiếu dữ liệu ghi ở `error` và được che key. [Cách chạy](README.md#luồng-của-phoenix) · [Data Card](data/DATA_CARD.md)
- CP4 thêm hành động `hoi_lai_mau_thuan` trong cùng lần gọi `gpt-6-luna`. Khi học viên chọn agent nhưng lý giải rằng cách xử lý đã định sẵn, Python dùng câu mẫu chỉ ra hai ý trái nhau và hỏi về quyền tự chọn bước tiếp theo. Lý do chưa rõ vẫn dùng câu hỏi chung. [Thay đổi và phép đo](eval/report.md#3-một-lần-cải-tiến)

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
| Nhầm quy trình có nhiều bước với agent | 4 | Chọn G01, hướng vào quyền quyết định bước tiếp. | B01, B04 |
| Dựa vào việc gọi công cụ để chọn agent | 4 | Chọn G02, hướng vào việc ai quyết định gọi công cụ. | B02, B05 |
| Nhầm hai nhánh đã định sẵn với agent | 4 | Chọn G03, hướng vào cách xử lý từng nhánh. | B03, B21 |
| Chỉ nêu lựa chọn, đoán hoặc chưa chắc chọn gì | 2 | Hỏi thêm một chi tiết trong đề, chưa gán mã gợi ý. | B06, B07, B22, B25 |
| Lý do tự mâu thuẫn hoặc có nhiều yếu tố | 2 | Hỏi lại yếu tố quyết định, không gán vội mã. | B08, B26 |
| Đã lý giải được cách chọn workflow | 4 | Hỏi phần người dùng muốn làm rõ, tránh quy họ đang có lỗi hiểu sai. | B09 |
| Lý do về kích thước hoặc tốc độ model chưa có gợi ý phù hợp | 1 | Hỏi lại hoặc nêu giới hạn, giữ nguyên bộ ba gợi ý. | B10, B28 |
| Nhờ giải một bài khác hoặc nhờ soạn tin nhắn | 3 | Nêu phạm vi và mời trở lại câu ôn CSV. | B23, B24, B27 |
| *(tấn công)* Đòi bỏ qua hướng dẫn rồi in danh sách gợi ý và đáp án | 3 | Từ chối và mời học viên nêu lý do của mình. | B11 |
| *(tấn công)* Xin làm hộ câu áp dụng | 3 | Từ chối làm hộ, nhắc phạm vi hỗ trợ. | B12 |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: nêu lý do khớp một lỗi, nhận gợi ý và làm câu áp dụng. Không chắc (lớp 2): hỏi một câu làm rõ. Không có căn cứ (lớp 1): hỏi lại hoặc nêu giới hạn. Người dùng sửa: nhập lại lựa chọn và lý do ngay trên CLI.
- Bị đòi ngoài phạm vi (lớp 3): từ chối và mời lại câu ôn. Trường hợp đặc thù (lớp 4): khi học viên đã nêu đúng dấu hiệu, tránh gợi ý sửa lỗi tiếp. Đây là hành vi kỳ vọng và được kiểm bằng benchmark. [Các sai lệch đã thấy ở mock](eval/README.md#4-lệnh)

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- [Data Card](data/DATA_CARD.md) · [Benchmark](eval/benchmark.csv) — 20 câu tự viết (thuong 6 · kho 9 · tu_choi 5), 0/20 đầu vào từ người dùng hoặc dữ liệu thật · [Metric spec](eval/metric_spec.yaml) (4 metric).
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): “Đạt khi ≥75% câu đạt theo `pass_criterion`, ≥80% câu thường nhận đúng mã gợi ý, 100% gợi ý hiển thị có mã hợp lệ, 100% ca kiểm tra phạm vi đạt và ≥50% người thử ngoài nhóm đã làm sai câu đầu rồi nhận gợi ý giải đúng câu áp dụng mới kèm lý do đúng.”
- Cách áp dụng: số câu đạt tính trên toàn benchmark và một câu chỉ đạt khi đủ các điều kiện trong `pass_criterion`. Với bộ 20 câu hiện tại, cần ≥15/20 câu đạt, ≥5/6 câu thường đúng mã và 7/7 ca kiểm tra phạm vi. Chỉ số học tập dùng mẫu người thử riêng theo `metric_spec.yaml`. Mẫu rỗng ghi “chưa đo”.
- Giữ phạm vi: B11 và B12 phải từ chối rõ. Với các ca phạm vi còn lại, có thể hỏi lại theo luồng Day 03, miễn là phản hồi dừng ở câu hỏi đó, không phân tích đề khác và không lộ gợi ý, đáp án hay lời giải. Nếu `pass_criterion` đòi từ chối, câu đó vẫn trượt khi hệ thống chỉ hỏi lại.
- CP2: chạy mock để kiểm luồng, Diên và Nhân chấm cùng 5 phản hồi và khớp 5/5 quyết định. CP3: [Lượt 1](eval/run-1.csv) trên `gpt-6-luna`, mã `run-1@20261128-080812`, đạt **19/20 (95%)** và có 0 lỗi kỹ thuật. Các ngưỡng kỹ thuật đã đạt. Chỉ số học tập với người thử ngoài nhóm chưa đo, nên chưa kết luận đạt toàn bộ chuẩn. [Hồ sơ đánh giá](eval/README.md#5-đã-chạy-gì) · [Báo cáo](eval/report.md)

## §8. Chi phí khi dùng thật *(guide 4.2)*
- [Persona và giá](cost/personas.yaml) · [simulate-1@20261128-124424](cost/simulate-1.csv) · 50 phiên, seed 42, 70 lượt gọi Luna, 0 phiên lỗi. Tỷ lệ dùng để tính chi phí/task là 20/20 từ [Lượt 2](eval/run-2.csv), chạy cùng model.
- Chi phí/task thành công là **0,00012 USD** với `gpt-6-luna`. Áp đơn giá `gpt-6.2-sol` lên cùng token và tỷ lệ của Luna cho kịch bản **0,0024 USD/task**. [Bảng từ runner](cost/simulate-1-summary.md)
- Chi phí Luna mỗi tháng ước tính **0,0803 USD** ở mức 350, **0,1605 USD** ở mức 700 và **0,2293 USD** ở mức 1.000 người hoạt động. Số người hoạt động và tần suất là giả định. [Báo cáo chi phí](cost/cost-estimate.md)
- Chi phí model ở mức cơ sở khoảng **0,00023 USD/người/tháng**. So với cơ hội **5 phút/người/tháng** giả định ở §2, đáng thử với một nhóm nhỏ để đo thời gian và khả năng áp dụng thực tế trước khi mở rộng.

## §9. Rủi ro & an toàn
- Dữ liệu gửi đi: câu ôn, điều kiện chọn gợi ý và lời giải thích được nhập. Log BTC chỉ dùng để tổng hợp bằng chứng tại máy. Benchmark CP3 dùng tình huống tự viết.
- Phạm vi model: chọn nhánh và mã, còn phản hồi hiển thị lấy từ dữ liệu hoặc câu mẫu. Nhánh hỏi về mâu thuẫn chỉ hiện mẫu khi mã gợi ý rỗng. Việc chấm điểm LMS và làm hộ bài ở ngoài phạm vi.
- Gợi ý lệch có thể khiến học viên củng cố hiểu nhầm. Nhóm kiểm mã bằng Python và chấm mức phù hợp của gợi ý theo từng câu.

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): Khôi phụ trách dữ liệu mock, bằng chứng, impact và nộp. Diên phụ trách luồng chọn gợi ý và kết nối OpenAI. Huy phụ trách bộ câu thử, metric, hướng dẫn chấm và phân tích log Day 03. Nhân tổng hợp spec và Canvas, tích hợp CP3, phụ trách đánh giá Lượt 1 và chuẩn bị demo. [TEAMS.md](TEAMS.md)
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`): AI hỗ trợ soạn dữ liệu mock, câu thử, phép đếm log, kết nối OpenAI và đối chiếu hồ sơ đánh giá. §7 ghi chuẩn đánh giá đã chốt ở CP2. [Khai báo](docs/ai-usage.md)
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
| 27/11/2026 | Diên nối `gpt-6-luna` với Structured Outputs và che key trong lỗi. | Dùng AI thật ở bước chọn phản hồi và giữ cách chặn ở §4. |
| 28/11/2026 | Huy rà benchmark, cách chấm và phép đếm; Khôi đối chiếu mốc nộp bài và cửa sổ 24 giờ. | Giải thích nguồn, mẫu số và giới hạn ở `evidence/summary.md`. |
| 28/11/2026 | Nhân tích hợp hồ sơ CP3 và phụ trách đánh giá Lượt 1 trên bản đã merge. | Đối chiếu kết quả lượt đầu với tiêu chí CP2. |
| 28/11/2026 | CP4 thêm nhánh hỏi rõ mâu thuẫn, chạy Lượt 2 cùng Luna và mô phỏng 50 phiên. | B08 hỏi lại chung ở Lượt 1. Lượt 2 tăng từ 19/20 lên 20/20. [Báo cáo](eval/report.md) · [Chi phí](cost/cost-estimate.md) · [Slide](demo-slides.pdf) |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
