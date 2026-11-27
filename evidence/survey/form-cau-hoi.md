# Thu bằng chứng pain — phỏng vấn qua tin nhắn + khảo sát Google Form

Đối tượng: học viên L3 khoá AI20K, **ngoài nhóm Phoenix**, đã học hoặc ôn Day 03.
Nguyên tắc: hỏi chuyện **đã xảy ra**, không giới thiệu sản phẩm của nhóm, không hỏi "bạn có muốn tính năng X không".

---

## A. Phỏng vấn qua tin nhắn (cần ≥3 người)

### Tin nhắn mời
> Chào bạn, mình là Huy nhóm Phoenix (L3). Nhóm mình đang tìm hiểu cách các bạn ôn bài Day 03 trên pre-class. Bạn cho mình hỏi 4 câu ngắn (khoảng 5 phút) được không? Mình không ghi tên bạn, chỉ ghi lại câu trả lời để làm bằng chứng cho bài hackathon.

### 4 câu hỏi (gửi lần lượt, đi theo câu chuyện họ kể)
1. Lần gần nhất bạn làm câu ôn Day 03 về chọn **workflow cố định hay agent** là khi nào? Bạn còn nhớ mình chọn gì và dựa vào chi tiết nào trong đề không?
2. Sau khi thấy kết quả và đáp án, bạn đã làm gì tiếp? (xem lại video/bài, hỏi trợ giảng AI, hỏi bạn, hay làm tiếp phần khác?) Vì sao?
3. Nếu bạn không xem lại: lúc đó bạn nghĩ mình đã hiểu chưa, hay chưa biết nên xem lại chỗ nào?
4. Thử đọc câu này giúp mình rồi chọn và giải thích 1–2 câu:
   > "Mỗi sáng, chương trình dùng công cụ đọc một tệp CSV và kiểm tra các cột bắt buộc. Nếu thiếu cột, chương trình ghi lỗi. Nếu đủ cột, chương trình xuất báo cáo. Bạn chọn workflow cố định hay agent cho việc này? Vì sao?"

**Phản xạ khi nghe:** nghe "mình thường…" → hỏi "lần gần nhất là khi nào?" · được khen ý tưởng → cảm ơn, quay lại chuyện thật · không hỏi dẫn dắt kiểu "bạn thấy khó đúng không?".

### Mẫu ghi chép — mỗi người một file `evidence/interviews/P1.md`, `P2.md`, `P3.md`

```markdown
# P1 — học viên L3 (ngoài nhóm)

- Ngày, hình thức: 28/11/2026 · tin nhắn Zalo/Discord
- Đã làm câu ôn Day 03 workflow/agent: có / không nhớ
- Lần gần nhất: …
- Lựa chọn lúc đó + chi tiết dựa vào: …
- Sau khi thấy đáp án đã làm gì: xem lại / hỏi AI / hỏi bạn / làm tiếp · vì sao: …
- Câu 4 — chọn: … · lý do nguyên văn: "…"

## Trích nguyên văn (bỏ tên)
- "…"
- "…"

## Khớp hay lệch với log (9/12 không xem lại sau khi sai)?
…
```

Không ghi tên, số điện thoại, tên tài khoản. Chụp màn hình thì che tên trước khi lưu.

---

## B. Khảo sát Google Form (cần ≥20 người)

**Cài đặt form:** tắt "Thu thập địa chỉ email", không bắt đăng nhập, không có câu hỏi tên.

**Tiêu đề:** Ôn bài Day 03 trên pre-class (2 phút, ẩn danh)
**Mô tả:** Nhóm Phoenix (L3) tìm hiểu cách học viên ôn Day 03. Không thu tên hay email. Câu trả lời chỉ dùng dưới dạng số tổng hợp và trích ngắn đã bỏ tên cho bài hackathon.

1. Bạn có học hoặc ôn Day 03 (chatbot → agent) trên pre-class không? · Có / Không *(Không → kết thúc)*
2. Bạn có nhớ câu ôn về chọn **workflow cố định hay agent** không? · Có, nhớ rõ / Nhớ mang máng / Không nhớ
3. Lần đó bạn trả lời đúng hay sai? · Đúng / Sai / Không nhớ
4. Sau khi thấy đáp án, bạn đã làm gì? *(chọn nhiều)* · Xem lại video hoặc bài Day 03 · Hỏi trợ giảng AI · Hỏi bạn hoặc TA · Tra Google/ChatGPT riêng · Làm tiếp phần khác, không xem lại · Không nhớ
5. Nếu không xem lại, vì sao? *(chọn nhiều)* · Đọc đáp án là hiểu rồi · Không biết nên xem lại chỗ nào · Không có thời gian · Không nghĩ là quan trọng · Khác: …
6. Trong tháng qua, bạn gặp bao nhiêu lần tình huống "sai câu ôn mà chưa hiểu vì sao sai"? · 0 · 1–2 · 3–5 · >5
7. Lần gần nhất như vậy, bạn mất khoảng bao lâu để hiểu lại (nếu có)? · <5 phút · 5–15 phút · >15 phút · Không tìm hiểu lại
8. **Đọc câu sau rồi chọn:** "Mỗi sáng, chương trình dùng công cụ đọc một tệp CSV và kiểm tra các cột bắt buộc. Nếu thiếu cột, chương trình ghi lỗi. Nếu đủ cột, chương trình xuất báo cáo." · Workflow cố định / Agent
9. **Viết 1–2 câu lý do bạn chọn ở câu 8.** *(đoạn ngắn, bắt buộc)*

Sau khi đóng form: tải CSV câu trả lời, giữ log đủ (ẩn danh) trong `evidence/survey/`. Câu 9 của người chọn **Agent** là lời giải thích thật → gửi Huy để thêm câu thử nguồn `nguoi_dung` (tối đa 10 câu).

---

## C. Đếm gì sau khi thu (viết trước khi đọc kết quả)

- Phỏng vấn: x/n người không xem lại sau khi sai (n nhỏ: ghi "x/3", không ghi %); lý do nguyên văn.
- Khảo sát: trong số người nhớ mình trả lời **sai** (câu 3), tỉ lệ chọn "Làm tiếp phần khác, không xem lại" ở câu 4 → so với log BTC (9/12 không xem lại).
- Câu 8–9: trong số người chọn Agent, bao nhiêu lý do thuộc G01 (số bước) · G02 (có công cụ) · G03 (có hai nhánh) · kiểu khác.
