from ui.generated_ui import Ui_MainWindow


class BorderSettings:
    style: int
    color: int

    def __init__(self, style: int, color: int):
        self.style = style
        self.color = color

class SpriteSettings:
    universe: int
    character: int
    expression: int
    expression_color: int

    def __init__(self, universe: int, character: int, expression: int, expression_color: int):
        self.universe = universe
        self.character = character
        self.expression = expression
        self.expression_color = expression_color

class FontSettings:
    font: int
    asterisk: bool
    asterisk_color: list[int]
    text_style: str
    transform: int

    def __init__(self, font: int, asterisk: bool, asterisk_color: list[int], text_style: str, transform: int):
        self.font = font
        self.asterisk = asterisk
        self.asterisk_color = asterisk_color
        self.text_style = text_style
        self.transform = transform

class ExportSettings:
    export_format: str
    margin: bool
    size: str

    def __init__(self, export_format: str, margin: bool, size: str):
        self.export_format = export_format
        self.margin = margin
        self.size = size