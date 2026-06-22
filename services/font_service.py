from PIL import ImageFont
from PySide6.QtWidgets import QComboBox
from matplotlib import font_manager

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

#def load_system_font(font_name: str, size: int):
    #try:
        #path = font_manager.findfont(
            #font_manager.FontProperties(family=font_name),
            #fallback_to_default=False
        #)

        #if font_name == "Wingdings":
            #return ImageFont.truetype(path, size, encoding="symb")

        #return ImageFont.truetype(path, size)

    #except Exception:
        #raise RuntimeError(
            #f"Font '{font_name}' ist not installed."
        #)
