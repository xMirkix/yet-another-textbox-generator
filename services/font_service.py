import threading

from PIL import ImageFont
from PySide6.QtWidgets import QComboBox

from configs.paths import FONTS
from startup.in_memory.static_classes import TextFont


def check_with_system_fonts(fonts: list[TextFont], element: QComboBox):
    for f in fonts:
        try:
            get_font(f, 1)
            element.addItem(f.font_name, userData=f)
        except RuntimeError:
            pass

_font_cache: dict = {}
_font_lock = threading.Lock()


def get_font(font, size):
    key = (font.font_name, size)
    with _font_lock:
        cached = _font_cache.get(key)
        if cached is None:
            cached = _load_font(font, size)
            _font_cache[key] = cached
        return cached

def _load_font(font: TextFont, size: int):
    return ImageFont.truetype(
        str(FONTS / font.source_value),
        size
    )
