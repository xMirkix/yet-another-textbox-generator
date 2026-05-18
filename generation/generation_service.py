from pathlib import Path

from PIL import Image

from configs.paths import TEMP_GIF, TEMP_PNG
from models.form_bindings import BorderSettings, FontSettings, SpriteSettings, ExportSettings

_last_output: Path | None = None

def is_valid_configuration_ui(text_input: str, sprite_settings: SpriteSettings, checked: bool, font_settings: FontSettings):
    if text_input is None or text_input == "":
        return False
    if font_settings.font is None:
        return False
    if not checked:
        sprite_settings.universe = None
        sprite_settings.character = None
        sprite_settings.expression = None
        return True
    if sprite_settings.universe is None or sprite_settings.character is None or sprite_settings.expression is None:
        return False
    return True

def is_valid_configuration(text_input: str, font_settings: FontSettings): # TODO CHANGES NEEDED WHEN MAKING CLI TOOL, LIKELY DIFFERENT USAGE
    if text_input is None or text_input == "":
        return False
    if font_settings.font is None:
        return False
    return True

def get_last_output() -> Path | None:
    return _last_output

def generate(text_input: str, border_settings: BorderSettings, sprite_settings: SpriteSettings, font_settings: FontSettings, export_settings: ExportSettings):
    global _last_output
    _last_output = TEMP_GIF if export_settings.export_format == "gif" else TEMP_PNG
    if _last_output == TEMP_GIF:
        frames = generate_gif(text_input, border_settings, sprite_settings, font_settings, export_settings)
        frames[0].save(TEMP_GIF, save_all=True, append_images=frames[1:], loop=0)
        return _last_output
    image = generate_png(text_input, border_settings, sprite_settings, font_settings, export_settings)
    image.save(TEMP_PNG)
    return _last_output

def generate_png(text_input: str, border_settings: BorderSettings, sprite_settings: SpriteSettings, font_settings: FontSettings, export_settings: ExportSettings) -> Image.Image:
    from generation.steps import border_step, sprite_step, font_step, export_step
    from generation.context import GenerationContext
    ctx = GenerationContext(image=border_step.apply(border_settings))
    ctx = sprite_step.apply(ctx, sprite_settings)
    ctx = font_step.apply(ctx, text_input, font_settings)
    return export_step.apply(ctx, export_settings)


def generate_gif(text_input: str, border_settings: BorderSettings, sprite_settings: SpriteSettings, font_settings: FontSettings, export_settings: ExportSettings) -> list[Image.Image]:
    pass # TODO