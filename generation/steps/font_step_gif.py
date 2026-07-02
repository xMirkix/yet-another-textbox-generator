# THIRD (only for gif, since already tokenized)
from generation.context import GenerationContext
from generation.steps.font_step import get_config, get_image_resolution, is_dark_world_style, get_text_insert_position
from generation.steps.font_substeps.text_image_generator import get_text_image
from models.form_bindings import FontSettings
from generation.steps.font_substeps.tokenizer import TextLine

from services.font_service import get_font
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, text_tokenized: list[TextLine], default_color: Color, settings: FontSettings) -> GenerationContext:
    if settings.font is None:
        return ctx

    try:
        config = get_config(settings.font.font_name)

        font = get_font(settings.font, config["font_size"])

        x, y = get_image_resolution(ctx.has_expression, ctx.has_right_expression, config)

        image_text = get_text_image(text_tokenized, default_color, is_dark_world_style(settings.text_style), font, config, (x, y), settings.asterisk_color) # includes asterisk

        insert_position = get_text_insert_position(ctx.border_style, ctx.has_expression , config)

        ctx.image.paste(image_text, insert_position, image_text)

    except OSError:
        pass
    return ctx