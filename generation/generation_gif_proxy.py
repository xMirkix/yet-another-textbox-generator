from pathlib import Path
from collections import OrderedDict

from PIL import Image

from generation.generation_request import GenerationRequest
from configs.paths import TEMP_DATA_DIR
from generation.gif_logic import deactivate_asterisks, for_each_line
from generation.gif_save_logic import save_gif
from generation.steps.font_step import get_config, get_image_resolution
from generation.steps.font_step import trim_newlines
from generation.steps.font_substeps.wrapping import calculate_wrapping
from services.font_service import get_font
from generation.steps.font_substeps.tokenizer import tokenize
import copy

def generate_gif(request: GenerationRequest) -> list[Image.Image] | None:
    font_settings = request.font_settings
    if font_settings.font is None:
        return None

    request.text_input = trim_newlines(request.text_input)

    tokens = tokenize(request.text_input, font_settings.transform, len(font_settings.asterisk_color) > 0)

    config = get_config(font_settings.font.font_name)

    font = get_font(font_settings.font, config["font_size"])

    max_width, _ = get_image_resolution(request.sprite_settings.expression is not None, request.right_sprite_settings.expression is not None, config)

    text = calculate_wrapping(tokens, font, max_width - 3,
                          config["character_extra_offset"],
                          config["space_extra_offset"],
                          config["initial_asterisk_offset"])

    current_position = [0, 0, 0]  # first line, first token, first character

    frame_counter: list[int] = [0] # for alternating expressions

    result: list[Image.Image] = []

    while current_position[0] < len(text): # for each line
        text_copy = copy.deepcopy(text) # reset copy for deactivation

        deactivate_asterisks(text_copy, current_position[0]) # deactivates future asterisks

        for_each_line(text_copy, current_position, result, request, frame_counter)

        current_position[0] += 1
        current_position[1] = 0
        current_position[2] = 0

    return result

CACHE_SIZE = 16

class GenerationGifProxy:
    cache: OrderedDict[GenerationRequest, Path] = OrderedDict()
    slot: int = 0

    def generate(self, request: GenerationRequest) -> Path | None:
        if request in self.cache:
            return self.cache[request]

        frames = generate_gif(request)

        if not frames:
            return None

        path = TEMP_DATA_DIR / f"output_{self.slot}.gif"

        save_gif(frames, [30] * len(frames), path)

        self.slot = (self.slot + 1) % CACHE_SIZE
        self.cache[request] = path
        if len(self.cache) > CACHE_SIZE:
            self.cache.popitem(last=False)

        return path