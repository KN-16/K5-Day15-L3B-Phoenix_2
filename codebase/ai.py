"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str, schema=None) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
      và thêm "refused" (bool): model từ chối trả lời (OpenAI message.refusal) — agent.py chuyển sang từ chối.
    schema (tuỳ chọn): JSON Schema model phải theo (OpenAI Structured Outputs); agent.py truyền vào.
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

Model thật — OpenAI Chat Completions, gọi bằng urllib (chỉ thư viện chuẩn), theo docs/connect-model.md §2.1:
    .env: MODEL_PROVIDER=openai · MODEL_NAME=<mã API, trùng tên trong bảng giá> · API_KEY=<key, không commit>
          tuỳ chọn, để trống = tắt: REASONING_EFFORT (gửi reasoning_effort) · MAX_OUTPUT_TOKENS (gửi
          max_completion_tokens). Chỉ bật khi số đo eval --try cho thấy cần.
    - Token lấy từ usage.prompt_tokens / usage.completion_tokens (đã gồm token suy luận) — không ước lượng.
    - Khoá "model" = MODEL_NAME để simulate tra đúng giá (cost/simulate.py so khớp đúng tên); API trả
      tên khác (vd kèm ngày) thì ghi note vào trace.
    - Lỗi HTTP / mạng / timeout / phản hồi thiếu trường / trả rỗng → RuntimeError đã che key, KHÔNG retry —
      khung ghi vào cột error; bị giới hạn lượt / phút thì chạy lại với --wait 4.
    - MODEL_PROVIDER khác openai, hoặc thiếu API_KEY / MODEL_NAME → NotImplementedError ("chưa nối model").
Không dán API key vào file này.
"""
import json
import os
import re
import urllib.error
import urllib.request

from tracing import model_call, note

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
REASONING_EFFORT = (os.environ.get("REASONING_EFFORT") or "").strip().lower()
_max_out = (os.environ.get("MAX_OUTPUT_TOKENS") or "").strip()
if _max_out and not _max_out.isdigit():
    raise ValueError("MAX_OUTPUT_TOKENS trong .env phải là số nguyên dương (để trống = không giới hạn), đang là %r"
                     % _max_out)
MAX_OUTPUT_TOKENS = int(_max_out or 0)  # 0 = không gửi giới hạn

URL_OPENAI = "https://api.openai.com/v1/chat/completions"
TIMEOUT_S = 60


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


_SECRET = re.compile(r"sk-[A-Za-z0-9_*\-]{4,}")


def _redact(text: str) -> str:
    """Che key trong thông báo lỗi — lỗi đi vào cột error của eval/run-N.csv và traces/, là file được commit."""
    if API_KEY:
        text = text.replace(API_KEY, "sk-***")
    return _SECRET.sub("sk-***", text)


def post_json(url: str, headers: dict, body: dict, timeout: float = TIMEOUT_S) -> dict:
    """POST JSON, trả JSON phản hồi (stdlib urllib). Lỗi HTTP / mạng / timeout → RuntimeError đã che key."""
    req = urllib.request.Request(url, data=json.dumps(body).encode("utf-8"), method="POST",
                                 headers={"Content-Type": "application/json", **headers})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            raw = r.read()
    except urllib.error.HTTPError as e:  # có mã HTTP: 401 sai key, 404 sai model, 429 hết lượt, 5xx…
        try:
            detail = e.read().decode("utf-8", "replace")[:300]
        except Exception:
            detail = ""
        raise RuntimeError("HTTP %d: %s" % (e.code, _redact(detail))) from None
    except OSError as e:  # URLError, TimeoutError, mất kết nối…
        raise RuntimeError("Không gọi được API (%s): %s"
                           % (type(e).__name__, _redact(str(getattr(e, "reason", None) or e)))) from None
    try:
        return json.loads(raw.decode("utf-8"))
    except ValueError:
        raise RuntimeError("Phản hồi API không phải JSON: %s" % _redact(raw[:300].decode("utf-8", "replace"))) from None


def call_openai(system: str, user: str, schema=None) -> dict:
    """Gọi đúng MỘT lần OpenAI Chat Completions. → {"text", "tokens_in", "tokens_out", "refused", "api_model"}."""
    messages = ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]
    body = {"model": MODEL_NAME, "messages": messages}
    if schema:
        body["response_format"] = {"type": "json_schema",
                                   "json_schema": {"name": "chon_phan_hoi", "strict": True, "schema": schema}}
    if REASONING_EFFORT:
        body["reasoning_effort"] = REASONING_EFFORT
    if MAX_OUTPUT_TOKENS:
        body["max_completion_tokens"] = MAX_OUTPUT_TOKENS
    data = post_json(URL_OPENAI, {"Authorization": "Bearer " + API_KEY}, body)
    try:
        choice = data["choices"][0]
        text = choice["message"].get("content") or ""
        refusal = choice["message"].get("refusal") or ""
        usage = data["usage"]
        tokens_in, tokens_out = int(usage["prompt_tokens"]), int(usage["completion_tokens"])
    except (KeyError, IndexError, TypeError, ValueError, AttributeError):
        raise RuntimeError("Phản hồi OpenAI thiếu choices / usage: %s"
                           % _redact(json.dumps(data, ensure_ascii=False)[:300])) from None
    if not text and not refusal:  # vd hết max_completion_tokens trong lúc suy luận: lỗi kỹ thuật, không coi là "hỏi lại"
        raise RuntimeError("OpenAI trả rỗng (finish_reason=%s, token ra %d) — tăng hoặc bỏ trống MAX_OUTPUT_TOKENS"
                           % (choice.get("finish_reason"), tokens_out))
    return {"text": text or refusal, "tokens_in": tokens_in, "tokens_out": tokens_out,
            "refused": not text, "api_model": str(data.get("model") or "")}


@model_call
def call_model(system: str, user: str, schema=None) -> dict:
    if MODEL_PROVIDER == "fake":
        return {"text": _mock_decide(user), "model": "fake", "tokens_in": 0, "tokens_out": 0}
    if MODEL_PROVIDER != "openai":
        raise NotImplementedError("codebase/ai.py mới nối MODEL_PROVIDER=openai (để trống = chế độ giả), đang là %r"
                                  % MODEL_PROVIDER)
    missing = [k for k, v in (("API_KEY", API_KEY), ("MODEL_NAME", MODEL_NAME)) if not v]
    if missing:
        raise NotImplementedError("thiếu %s trong .env" % " và ".join(missing))
    r = call_openai(system, user, schema)
    if r["api_model"] and r["api_model"] != MODEL_NAME:
        note("OpenAI trả model=%s (giá tính theo %s)" % (r["api_model"], MODEL_NAME))
    return {"text": r["text"], "model": MODEL_NAME, "tokens_in": r["tokens_in"], "tokens_out": r["tokens_out"],
            "refused": r["refused"]}
