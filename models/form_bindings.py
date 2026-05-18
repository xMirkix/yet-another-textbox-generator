from enum import Enum

from models.entities import Universe, Character, Expression
from startup.in_memory.static_classes import BorderStyle, Color, TextFont, TextTransform


class BorderSettings:
    style: BorderStyle
    color: Color

    def __init__(self, style: BorderStyle, color: Color):
        self.style = style
        self.color = color

class SpriteSettings:
    universe: Universe | None
    character: Character | None
    expression: Expression | None
    expression_color: Color

    def __init__(self, universe: Universe | None, character: Character | None, expression: Expression | None, expression_color: Color):
        self.universe = universe
        self.character = character
        self.expression = expression
        self.expression_color = expression_color

class FontSettings:
    font: TextFont | None
    asterisk_color: list[Color]
    text_style: TextStyle
    transform: TextTransform

    def __init__(self, font: TextFont | None, asterisk_color: list[Color], text_style: TextStyle, transform: TextTransform):
        self.font = font
        self.asterisk_color = asterisk_color
        self.text_style = text_style
        self.transform = transform

class ExportSettings:
    export_format: ExportFormat
    margin: bool
    size: ExportSize

    def __init__(self, export_format: ExportFormat, margin: bool, size: ExportSize):
        self.export_format = export_format
        self.margin = margin
        self.size = size

class TextStyle(Enum):
    REGULAR = ('Regular','regular')
    DARK_WORLD = ('Dark World','dark world')

class ExportFormat(Enum):
    PNG = 'png'
    GIF = 'gif'

class ExportSize(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'