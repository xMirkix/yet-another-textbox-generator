from pathlib import Path
from collections import OrderedDict

from PIL import Image

from configs.paths import TEMP_DATA_DIR
from generation.generation_request import GenerationRequest
from models.form_bindings import BorderSettings, SpriteSettings, ExportSettings, FontSettings
from startup.in_memory.static_classes import Color

def is_valid_configuration_ui(text_input: str, sprite_settings: SpriteSettings, checked: bool, right_sprite_settings: SpriteSettings, right_checked: bool, font_settings: FontSettings) -> str | None:
    if text_input is None or text_input == "":
        return "ERROR in Input/Preview \n To generate empty textboxes, use whitespaces"
    if font_settings.font is None:
        return "ERROR in Font Settings \n No fonts exist. This shouldn't happen. Contact the developer"
    if not validate_and_clear_sprite(sprite_settings, checked):
        return "ERROR in Sprite Settings (Left) \n Fixes: Uncheck include, create an universe, character and expression or open a filled .yatg file"
    if not validate_and_clear_sprite(right_sprite_settings, right_checked):
        return "ERROR in Sprite Settings (Right) \n Fixes: Uncheck include, create an universe, character and expression or open a filled .yatg file"
    return None

def validate_and_clear_sprite(sprite_settings: SpriteSettings, checked: bool) -> bool:
    if not checked:
        sprite_settings.universe = None
        sprite_settings.character = None
        sprite_settings.expression = None
        return True
    return not (sprite_settings.universe is None
                or sprite_settings.character is None
                or sprite_settings.expression is None)

def is_valid_configuration(text_input: str, font_settings: FontSettings):
    if text_input is None or text_input == "":
        return False
    if font_settings.font is None:
        return False
    return True

def generate_png(text_input: str, default_color: Color, border_settings: BorderSettings,
                 sprite_settings: SpriteSettings, right_sprite_settings: SpriteSettings, font_settings: FontSettings,
                 export_settings: ExportSettings) -> Image.Image:
    from generation.steps import border_step, sprite_step, font_step, export_step
    from generation.context import GenerationContext
    image, style = border_step.apply(border_settings)
    ctx = GenerationContext(image=image, has_expression=False, border_style=style)
    ctx = sprite_step.apply(ctx, sprite_settings, right_sprite_settings)
    ctx = font_step.apply(ctx, text_input, default_color, font_settings)
    return export_step.apply(ctx, export_settings)

CACHE_SIZE = 16

class GenerationPngProxy:

    cache: OrderedDict[GenerationRequest, Path] = OrderedDict()

    slot: int = 0

    def generate(self, request: GenerationRequest) -> Path | None:
        if request in self.cache:
            return self.cache[request]

        image = generate_png(
            request.text_input,
            request.default_color,
            request.border_settings,
            request.sprite_settings,
            request.right_sprite_settings,
            request.font_settings,
            request.export_settings,
        )

        path = TEMP_DATA_DIR / f"output_{self.slot}.png"
        image.save(path)
        self.slot = (self.slot + 1) % CACHE_SIZE

        self.cache[request] = path
        if len(self.cache) > CACHE_SIZE:
            self.cache.popitem(last=False)

        return path

