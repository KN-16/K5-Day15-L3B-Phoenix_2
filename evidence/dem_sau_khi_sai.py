"""Đếm hành vi sau khi trả lời sai lần đầu câu ôn Day 03 (agentic_fit_scoring_decision).

Chạy từ thư mục gốc repo Phoenix (repo đề BTC đặt cùng cấp):
    python evidence/dem_sau_khi_sai.py ../K5-L3-Day15-AI-Product-Hackathon/data/preclass

Cách đếm (viết trước khi chạy):
- Mẫu: answers.csv, lesson_id = program-day03:chatbot-to-agentic-agent, kc_code = agentic_fit_scoring_decision,
  nguon = pre_post_post, lan_thu = 1, was_correct là True/False. Mỗi học viên 1 dòng.
- Mốc thời gian: answers.created_at (UTC). Cửa sổ 24 giờ sau mốc; chỉ giữ học viên có đủ 24 giờ trước khi log kết thúc.
- "Mở lại bài": events.csv có type lecture_opened hoặc video_opened, cùng lesson_id, sau mốc.
- "Hỏi trợ giảng về Day 03": chat.csv có transcript bắt đầu "Day03", asked_at sau mốc.
"""
import sys

import pandas as pd

d = sys.argv[1].rstrip("/\\") + "/"
L = "program-day03:chatbot-to-agentic-agent"
a = pd.read_csv(d + "answers.csv")
e = pd.read_csv(d + "events.csv", usecols=["hv", "type", "lesson_id", "occurred_at"])
c = pd.read_csv(d + "chat.csv", usecols=["hv", "transcript", "asked_at"])
e["t"] = pd.to_datetime(e.occurred_at, utc=True, format="mixed")
c["t"] = pd.to_datetime(c.asked_at, utc=True, format="mixed")
end = e.t.max()

s = a[(a.lesson_id == L) & (a.kc_code == "agentic_fit_scoring_decision") & (a.nguon == "pre_post_post")
      & (a.lan_thu == 1) & a.was_correct.notna()].copy()
s["t"] = pd.to_datetime(s.created_at, utc=True)
assert s.hv.is_unique, "mỗi học viên phải có đúng 1 dòng"

rows = []
for _, r in s.iterrows():
    if r.t + pd.Timedelta(hours=24) > end:
        continue
    ev = e[(e.hv == r.hv) & (e.t > r.t) & (e.lesson_id == L) & e.type.isin(["lecture_opened", "video_opened"])]
    ch = c[(c.hv == r.hv) & (c.t > r.t) & c.transcript.fillna("").str.startswith("Day03")]
    rows.append(dict(id=r.id, dung=r.was_correct, mo_lai_24h=(ev.t <= r.t + pd.Timedelta(hours=24)).any(),
                     mo_lai_sau=len(ev) > 0, hoi_day03_sau=len(ch) > 0))
R = pd.DataFrame(rows)
R["co_xem_lai"] = R.mo_lai_sau | R.hoi_day03_sau
for ok, g in R.groupby("dung"):
    n = len(g)
    print("Nhóm", "ĐÚNG" if ok else "SAI", "N =", n)
    for col in ["mo_lai_24h", "mo_lai_sau", "hoi_day03_sau", "co_xem_lai"]:
        x = int(g[col].sum())
        print("  %-14s %d/%d (%.0f%%)" % (col, x, n, 100 * x / n))
print("\nVí dụ nhóm SAI không xem lại:", ", ".join(R[(~R.dung) & (~R.co_xem_lai)].id.sort_values().head(5)))
