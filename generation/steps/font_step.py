# THIRD
from PIL import ImageFont

from generation.context import GenerationContext
from models.form_bindings import FontSettings
from startup.in_memory.static_classes import TextTransform
from matplotlib import font_manager


def apply(ctx: GenerationContext, text: str, settings: FontSettings) -> GenerationContext:
    # Text offset if it has_expression and keep asterisk in mind
    # Apply transform, line breaks, asterisks and dark world
    applied_text = apply_text_transform(text, settings.transform)
    trimmed = trim_newlines(applied_text)

    try:
        ctx = apply_asterisks(ctx, trimmed, settings)
        ctx = apply_text(ctx, trimmed, settings)
        ctx = apply_dark_world(ctx, settings)
    except OSError:
        return ctx

    return ctx

def apply_text_transform(text: str, transform: TextTransform) -> str:
    if transform.transform_id == 2:
        return text.upper()
    if transform.transform_id == 3:
        return text.lower()
    if transform.transform_id == 4:
        return text.title()
    return text

def trim_newlines(text: str) -> str:
    while text.count("\n") > 2: # limit to 3 lines
        text = text[:text.rfind("\n")]
    return text

def get_font(font_name: str, font_size: int) -> ImageFont.FreeTypeFont:
    path = font_manager.findfont(font_manager.FontProperties(family=font_name))
    return ImageFont.truetype(path, font_size)

def apply_asterisks(ctx: GenerationContext, text: str, settings: FontSettings) -> GenerationContext:
    if not settings.asterisk_color:  # empty - disabled
        return ctx
    # TODO: Place asterisks in right color and position
    return ctx

def apply_text(ctx: GenerationContext, text: str, settings: FontSettings) -> GenerationContext:
    # TODO: Wrap text, generate it as an image and place it on ctx.image
    # Keep offset in mind if ctx.has_expression
    return ctx

def apply_dark_world(ctx: GenerationContext, settings: FontSettings) -> GenerationContext:
    if settings.text_style.value != "dark world":
        return ctx
    # TODO: Insert Dark World pattern (color has gradients...)
    return ctx