"""Giao diện web cho bản chạy thử — gọi đúng luồng answer() trong agent.py (cùng model, cùng chặn rủi ro như CLI).

Chạy:   python codebase/web.py            → mở http://127.0.0.1:8000
        python codebase/web.py --port 8080

Chỉ dùng thư viện chuẩn. Chỉ nghe trên 127.0.0.1 (máy mình). Không gửi API key hay dữ liệu nào ra trình duyệt
ngoài câu ôn, phản hồi soạn sẵn và số đo của lượt gọi (model, token).
"""
import json
import os
import sys
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import tracing  # noqa: E402
from agent import answer  # noqa: E402
from tools import get_lesson  # noqa: E402

PAGE = os.path.join(HERE, "web", "index.html")
CORRECT = "workflow cố định"   # đáp án câu ôn trong data/day03.json
MAX_BODY = 8000
_lock = threading.Lock()      # tracing dùng biến toàn cục: xử lý từng lượt một


def branch_of(output: str) -> dict:
    """Nhận nhánh từ chữ phản hồi, theo đúng cách chấm ở eval/metric_spec.yaml."""
    if output.startswith("Gợi ý G"):
        head, _, rest = output.partition(":")
        hint_text, _, follow = rest.partition("\n\nCâu áp dụng mới:")
        return {"branch": "goi_y", "hint_id": head.replace("Gợi ý", "").strip(),
                "text": hint_text.strip(), "follow_up": follow.strip()}
    if output.startswith("Mình chỉ giúp bạn"):
        return {"branch": "tu_choi", "text": output}
    return {"branch": "hoi_lai", "text": output}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):  # gọn log, không in nội dung học viên gõ
        sys.stdout.write("%s %s\n" % (self.command, self.path))

    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        data = body if isinstance(body, bytes) else json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            with open(PAGE, "rb") as f:
                return self._send(200, f.read(), "text/html; charset=utf-8")
        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return
        if self.path == "/api/lesson":
            lesson = get_lesson()
            return self._send(200, {"question": lesson["question"], "correct": CORRECT})
        self._send(404, {"error": "không có trang này"})

    def do_POST(self):
        if self.path != "/api/answer":
            return self._send(404, {"error": "không có trang này"})
        size = int(self.headers.get("Content-Length") or 0)
        if size > MAX_BODY:
            return self._send(413, {"error": "đầu vào quá dài"})
        try:
            req = json.loads(self.rfile.read(size).decode("utf-8") or "{}")
        except ValueError:
            return self._send(400, {"error": "dữ liệu gửi lên không đọc được"})
        choice = str(req.get("choice") or "").strip()
        reason = str(req.get("reason") or "").strip()
        text = ("Em chọn %s. Lý do: %s" % (choice, reason)) if choice else reason
        with _lock:
            tracing.begin("web")
            try:
                result = answer(text)
            except NotImplementedError as e:
                tracing.end()
                return self._send(500, {"error": "Chưa nối model: %s" % e})
            except Exception as e:  # lỗi gọi model: báo gọn, không lộ chi tiết nhạy cảm
                tracing.end()
                return self._send(502, {"error": "Lỗi khi gọi model (%s). Thử lại sau." % type(e).__name__})
            s, _ = tracing.end()
        output = result.get("output", "") if isinstance(result, dict) else str(result)
        body = branch_of(output)
        body.update(output=output, sent=text, model=", ".join(s["models"]) or "—",
                    model_calls=s["model_calls"], tokens_in=s["tokens_in"], tokens_out=s["tokens_out"])
        self._send(200, body)


def main():
    port = 8000
    if "--port" in sys.argv:
        port = int(sys.argv[sys.argv.index("--port") + 1])
    get_lesson()  # nạp data/day03.json ngay: thiếu / hỏng file thì báo luôn
    server = HTTPServer(("127.0.0.1", port), Handler)
    print("Mở trình duyệt: http://127.0.0.1:%d   (dừng: Ctrl+C)" % port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
