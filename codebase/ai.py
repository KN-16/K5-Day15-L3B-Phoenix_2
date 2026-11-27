"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.
    Mock trả đúng dạng JSON mà model thật phải trả ({"action", "hint_id"}), nên luồng ở agent.py
    (đọc JSON → kiểm mã gợi ý → xuất phản hồi) chạy y hệt khi đổi sang model thật. Mock chỉ đọc
    prompt như model đọc, và chọn theo QUY TẮC CÔNG KHAI (không so khớp câu thử nào):
      1. Từ khoá của một gợi ý = các từ ≥3 ký tự trong `when` của gợi ý đó mà không có trong `when`
         của gợi ý khác (vd G01: lượng, bước · G02: công, đọc, csv · G03: hai, nhánh).
      2. Lời giải thích không chứa từ khoá nào, cũng không chứa workflow / agent / agentic / trình
         → tu_choi (không phải lời giải thích cho câu ôn).
      3. Đúng MỘT gợi ý có từ khoá xuất hiện trong lời giải thích → goi_y với mã đó.
      4. Còn lại (không trúng gợi ý nào, hoặc trúng từ hai gợi ý trở lên) → hoi_lai.
    Giới hạn đã biết: đếm từ, không hiểu nghĩa — vd "nhiều bước: đọc tệp…" trúng cả G01 (bước) và
    G02 (đọc) nên hỏi lại. Model thật thay mock từ CP3.

Nối model thật: điền .env (chép từ .env.example), rồi viết nhánh gọi API ở dưới theo docs/connect-model.md
(có ví dụ OpenAI, Claude, model chạy trên máy, và cách nối nhà cung cấp khác). Không dán API key vào file này.
"""
import json
import os
import re

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Định dạng prompt agent.py dựng và mock đọc lại — để một chỗ cho hai bên dùng chung.
HINT_PREFIX = "- "                            # mỗi dòng gợi ý: "- <id> | <when>"
HINT_SEP = " | "
INPUT_HEADER = "Lời giải thích của học viên:"  # sau dòng này là nguyên văn đầu vào của học viên


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


_WORD = re.compile(r"\w+")
_SCOPE_WORDS = frozenset(("workflow", "agent", "agentic", "trình"))


def _words(s: str) -> set:
    return {w for w in _WORD.findall(s.lower()) if len(w) >= 3}


def _mock_decide(user: str) -> str:
    """Quyết định giả theo quy tắc công khai ở đầu file. Trả chuỗi JSON như model thật."""
    head, _, said = user.partition(INPUT_HEADER)
    hints = [line[len(HINT_PREFIX):].split(HINT_SEP, 1) for line in head.split("\n")
             if line.startswith(HINT_PREFIX) and HINT_SEP in line]
    feats = [(hid, _words(when)) for hid, when in hints]
    said_words = _words(said)
    hit = [hid for hid, f in feats                 # gợi ý có từ khoá riêng nằm trong lời giải thích
           if f.difference(*(g for other, g in feats if other != hid)) & said_words]
    if not hit and not said_words & _SCOPE_WORDS:
        action, hint_id = "tu_choi", ""
    elif len(hit) == 1:
        action, hint_id = "goi_y", hit[0]
    else:
        action, hint_id = "hoi_lai", ""
    return json.dumps({"action": action, "hint_id": hint_id})


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        return {"text": _mock_decide(user), "model": "fake", "tokens_in": 0, "tokens_out": 0}

    # NHÓM VIẾT: gọi model thật ở đây (theo MODEL_PROVIDER, MODEL_NAME, API_KEY) rồi trả đúng 4 khoá.
    # Ví dụ chép được cho từng nhà cung cấp: docs/connect-model.md mục 2.
    raise NotImplementedError(
        "chưa viết phần gọi model thật cho MODEL_PROVIDER=%s trong codebase/ai.py — xem docs/connect-model.md"
        % MODEL_PROVIDER)
