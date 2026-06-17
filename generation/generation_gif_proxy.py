from pathlib import Path
from collections import OrderedDict

from PIL import Image

from generation.generation_request import GenerationRequest
from configs.paths import TEMP_DATA_DIR
from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from startup.in_memory.static_classes import Color


def generate_gif(text_input: str, default_color: Color, border_settings: BorderSettings, sprite_settings: SpriteSettings, font_settings: FontSettings, export_settings: ExportSettings) -> list[Image.Image]:
    pass # TODO

CACHE_SIZE = 10

class GenerationGifProxy:
    cache: OrderedDict[GenerationRequest, Path] = OrderedDict()
    slot: int = 0

    def generate(self, request: GenerationRequest) -> Path | None:
        if request in self.cache:
            return self.cache[request]

        frames = generate_gif(
            request.text_input,
            request.default_color,
            request.border_settings,
            request.sprite_settings,
            request.font_settings,
            request.export_settings,
        )

        if not frames:
            return None

        path = TEMP_DATA_DIR / f"output_{self.slot}.gif"
        frames[0].save(path, save_all=True, append_images=frames[1:], loop=0)

        self.slot = (self.slot + 1) % CACHE_SIZE
        self.cache[request] = path
        if len(self.cache) > CACHE_SIZE:
            self.cache.popitem(last=False)

        return path