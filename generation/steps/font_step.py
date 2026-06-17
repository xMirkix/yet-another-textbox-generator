# THIRD
import platform
from pathlib import Path
from typing import Literal
from PIL import ImageFont
from generation.context import GenerationContext
from generation.steps.font_substeps.font_config import FontConfig
from generation.steps.font_substeps.text_image_generator import get_text_image
from models.form_bindings import FontSettings, TextStyle
from generation.steps.font_substeps.tokenizer import tokenize
from configs.paths import GEN_CONFIG, FONTS
import tomllib
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, text: str, default_color: Color, settings: FontSettings) -> GenerationContext:
    if settings.font is None:
        return ctx

    try:
        trimmed = trim_newlines(text)
        lines = tokenize(trimmed, settings.transform, len(settings.asterisk_color) > 0)

        config = get_config(settings.font.font_name)

        font = get_font(settings.font.font_name,settings.font.font_file_name, config["font_size"])

        x, y = get_image_resolution(ctx.has_expression, config)

        image_text = get_text_image(lines, default_color, is_dark_world_style(settings.text_style), font, config, (x, y), settings.asterisk_color) # includes asterisk

        insert_position = get_text_insert_position(ctx.border_style, ctx.has_expression , config)

        ctx.image.paste(image_text, insert_position, image_text)

    except OSError:
        pass
    return ctx

def get_text_insert_position(style: str, with_sprite: bool, config: FontConfig) -> tuple[int, int]:
    x, y = 3, 3

    if style == "Deltarune":
        x, y = 7, 7

    key: Literal["x_with_sprite", "x_no_sprite"] = "x_with_sprite" if with_sprite else "x_no_sprite"

    x, y = x + config[key], y + config["y_text_start"]
    return x, y

def get_image_resolution(with_sprite: bool, config: FontConfig) -> tuple[int, int]:
    x, y = 0, 0
    key: Literal["x_with_sprite", "x_no_sprite"] = "x_with_sprite" if with_sprite else "x_no_sprite"

    x, y = x + config[key], y + config["y_text_start"]
    return (
        283 - x,
        70 - y,
    )

def is_dark_world_style(style: TextStyle) -> bool:
    return style == TextStyle.DARK_WORLD

def get_config(font: str) -> FontConfig:
    with open(GEN_CONFIG, "rb") as f:
        config: dict[str, FontConfig] = tomllib.load(f)
    return config.get(font.replace(" ", "-")) or config["default"]

# helpers
def trim_newlines(text: str) -> str:
    while text.count("\n") > 2:
        text = text[:text.rfind("\n")]
    return text


def get_font(font_name, font_file_name: str, size: int) -> ImageFont.FreeTypeFont:
    system_fonts = ["Wingdings", "UndertaleSans", "UndertalePapyrus"]

    if font_name in system_fonts:
        return load_system_font(font_file_name, size, encoding="symb")

    font_path = (FONTS / font_file_name)

    return ImageFont.truetype(str(font_path), size)

def load_system_font(font_file_name: str, size: int, **kwargs) -> ImageFont.FreeTypeFont:

    system = platform.system()

    if system == "Windows":
        font_dir = Path("C:/Windows/Fonts")
    elif system == "Linux":
        font_dir = Path.home() / ".local/share/fonts"
    elif system == "Darwin":
        font_dir = Path("/Library/Fonts")
    else:
        raise OSError("Unknown OS")

    return ImageFont.truetype(str(font_dir / font_file_name), size, **kwargs)