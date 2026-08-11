from enum import Enum

from models.entities import Universe, Character, Expression
from startup.in_memory.static_classes import BorderStyle, Color, TextFont, TextTransform


class BorderSettings:
    style: BorderStyle
    color: Color

    def __init__(self, style: BorderStyle, color: Color):
        self.style = style
        self.color = color

    def __eq__(self, other) -> bool:
        if isinstance(other, BorderSettings):
            return self.style == other.style and self.color == other.color
        return False

    def __hash__(self) -> int:
        return hash((self.style, self.color))

class ColorType(Enum):
    SIMPLE = ('Simple','simple')
    EVERYTHING = ('Everything','everything')
    CUSTOM = ('Custom','custom')

    def __eq__(self, other) -> bool:
        if isinstance(other, ColorType):
            return self.value[0] == other.value[0]
        return False

    def __hash__(self) -> int:
        return hash(self.value[0])

class SpriteSettings:
    universe: Universe | None
    character: Character | None
    expression: Expression | None
    alternating_expression: Expression | None
    alternating_interval: int
    alternating_duration: int
    expression_color: Color | None
    color_type: ColorType | None
    selected_colors: tuple | None
    simple_recoloring: bool | None

    def __init__(self, universe: Universe | None, character: Character | None, expression: Expression | None,
                 alternating_expression: Expression | None, alternating_interval: int, alternating_duration: int,
                 expression_color: Color | None, color_type: ColorType | None, selected_colors: tuple | None, simple_recoloring: bool | None):
        self.universe = universe
        self.character = character
        self.expression = expression
        self.alternating_expression = alternating_expression
        self.alternating_interval = alternating_interval
        self.alternating_duration = alternating_duration
        self.expression_color = expression_color
        self.color_type = color_type
        self.selected_colors = selected_colors
        self.simple_recoloring = simple_recoloring

    def __eq__(self, other) -> bool:
        if isinstance(other, SpriteSettings):
            return (self.universe == other.universe
                    and self.character == other.character
                    and self.expression == other.expression
                    and self.expression_color == other.expression_color
                    and self.alternating_expression == other.alternating_expression
                    and self.alternating_interval == other.alternating_interval
                    and self.alternating_duration == other.alternating_duration
                    and self.color_type == other.color_type
                    and self.selected_colors == other.selected_colors
                    and self.simple_recoloring == other.simple_recoloring)
        return False

    def __hash__(self) -> int:
        return hash((self.universe, self.character, self.expression, self.alternating_expression, self.alternating_interval, self.alternating_duration, self.expression_color, self.color_type, tuple(self.selected_colors) if self.selected_colors is not None else None, self.simple_recoloring))

class TextStyle(Enum):
    REGULAR = ('Regular','regular')
    DARK_WORLD = ('Dark World','dark world')

    def __eq__(self, other) -> bool:
        if isinstance(other, TextStyle):
            return self.value[0] == other.value[0]
        return False

    def __hash__(self) -> int:
        return hash(self.value[0])

class ExportFormat(Enum):
    PNG = 'png'
    GIF = 'gif'

    def __eq__(self, other) -> bool:
        if isinstance(other, ExportFormat):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

class ExportSize(Enum):
    SMALL = 'small'
    MEDIUM = 'medium'
    BIG = 'big'

    def __eq__(self, other) -> bool:
        if isinstance(other, ExportSize):
            return self.value == other.value
        return False

    def __hash__(self):
        return hash(self.value)

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

    def __eq__(self, other) -> bool:
        if isinstance(other, FontSettings):
            return self.font == other.font and self.asterisk_color == other.asterisk_color and self.text_style == other.text_style and self.transform == other.transform
        return False

    def __hash__(self) -> int:
        return hash((self.font, tuple(self.asterisk_color), self.text_style, self.transform))

class ExportSettings:
    export_format: ExportFormat
    margin: bool
    size: ExportSize

    def __init__(self, export_format: ExportFormat, margin: bool, size: ExportSize):
        self.export_format = export_format
        self.margin = margin
        self.size = size

    def __eq__(self, other) -> bool:
        if isinstance(other, ExportSettings):
            return self.export_format == other.export_format and self.margin == other.margin and self.size == other.size
        return False

    def __hash__(self) -> int:
        return hash((self.export_format, self.margin, self.size))
