"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Dữ liệu: data/day03.json (mô tả ở data/DATA_CARD.md) — một câu ôn Day 03, các gợi ý đã soạn
(`id`, `when`, `text`) và một câu áp dụng mới. File được đọc MỘT lần khi gọi công cụ lần đầu,
kiểm cấu trúc, đánh chỉ mục gợi ý theo `id`; các lần sau dùng lại bản đã nạp (không mở lại file,
không sao chép). Không công cụ nào sửa dữ liệu đã nạp.
"""
import json
import os

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký, dùng khi viết vòng lặp agent)

DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "day03.json")

_lesson = None   # dict đã nạp từ DATA_PATH
_hints = None    # id gợi ý → bản ghi gợi ý (tham chiếu vào _lesson)


def _load() -> dict:
    """Nạp + kiểm data/day03.json một lần. Sai cấu trúc thì báo rõ trường nào, không chạy tiếp với data hỏng."""
    global _lesson, _hints
    if _lesson is None:
        with open(DATA_PATH, encoding="utf-8-sig") as f:
            lesson = json.load(f)
        for key in ("question", "follow_up_question"):
            if not isinstance(lesson.get(key), str) or not lesson[key].strip():
                raise ValueError("data/day03.json: thiếu hoặc trống trường %r" % key)
        hints = lesson.get("hints")
        if not isinstance(hints, list) or not hints:
            raise ValueError("data/day03.json: 'hints' phải là danh sách không rỗng")
        index = {}
        for k, h in enumerate(hints):
            if not isinstance(h, dict) or not all(isinstance(h.get(f), str) and h[f].strip() for f in ("id", "when", "text")):
                raise ValueError("data/day03.json: hints[%d] thiếu 'id' / 'when' / 'text'" % k)
            if h["id"] in index:
                raise ValueError("data/day03.json: trùng mã gợi ý %r" % h["id"])
            index[h["id"]] = h
        _lesson, _hints = lesson, index
    return _lesson


@tool
def get_lesson() -> dict:
    """get_lesson — lấy câu ôn Day 03 và các gợi ý đã soạn.
    Input: không có. Output: dict {"question", "hints": [{"id", "when", "text"}], "follow_up_question"}
    (đọc từ data/day03.json, nạp một lần). Không tác động ra ngoài."""
    return _load()


@tool
def check_hint(hint_id: str):
    """check_hint — kiểm mã gợi ý model chọn có thuộc câu ôn không.
    Input: hint_id (str). Output: bản ghi gợi ý {"id", "when", "text"} nếu mã hợp lệ, None nếu không.
    Không tác động ra ngoài."""
    _load()
    return _hints.get(hint_id)
