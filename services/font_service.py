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

def get_font(font: TextFont, size: int):
    return ImageFont.truetype(
        str(FONTS / font.source_value),
        size
    )
