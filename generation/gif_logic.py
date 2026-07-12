from PIL import Image

from generation.generation_request import GenerationRequest
from generation.steps.font_substeps.tokenizer import TextLine, TextToken
import copy

from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from startup.in_memory.static_classes import Color


def deactivate_asterisks(text_copy: list[TextLine], i: int):
    j = i + 1

    while j < len(text_copy):
        text_copy[j].has_asterisk = False  # hides asterisk, bad naming, I know
        j += 1


def for_each_line(text: list[TextLine],
                  current_position: list[int],
                  result: list[Image.Image],
                  request: GenerationRequest,
                  frame_counter: list[int],):
    line = text[current_position[0]]

    content: list[TextToken] = line.content

    while current_position[1] < len(content):  # for each token
        text_copy = copy.deepcopy(text)  # reset copy for deactivation

        deactivate_tokens(text_copy, current_position[0], current_position[1])  # deactivate future tokens

        paused = for_each_character(text_copy, current_position, result, request, frame_counter)

        append_additional_images(text_copy, current_position, result, request, frame_counter, paused)

        current_position[1] += 1
        current_position[2] = 0


def deactivate_tokens(text_copy: list[TextLine], current_line: int, current_token: int):
    i = current_line
    j = current_token + 1
    while j < len(text_copy[i].content):  # tokens in same line after current get fully transparent
        text_copy[i].content[j].colors = {0: get_transparent()}
        j += 1

    i += 1

    while i < len(text_copy):  # remaining lines, all tokens should be invisible
        j = 0
        while j < len(text_copy[i].content):
            text_copy[i].content[j].colors = {0: get_transparent()}
            j += 1
        i += 1


def append_additional_images(text: list[TextLine], current_position: list[int], result: list[Image.Image], request: GenerationRequest, frame_counter: list[int], paused: bool):
    amount = 1

    if current_position[2] == 0:
        return

    current_char = text[current_position[0]].content[current_position[1]].content[current_position[2] - 1]

    if current_char == "," or current_char == ";":
        amount = 6

    if current_char == "." or current_char == "!" or current_char == "?":
        amount = 19

    is_talking_pause = amount == 1 or amount == 6

    if paused:
        is_talking_pause = False

    for _ in range(amount):
        if is_talking_pause:
            sprite = resolve_sprite(request.sprite_settings, frame_counter[0])
            sprite_right = resolve_sprite(request.right_sprite_settings, frame_counter[0])
            frame_counter[0] += 1
        else:
            sprite = request.sprite_settings
            sprite_right = request.right_sprite_settings

        result.append(generate_single(
            text, request.default_color, request.border_settings,
            sprite, sprite_right, request.font_settings, request.export_settings
        ))

    if not is_talking_pause:
        frame_counter[0] = 0


def get_transparent() -> Color:
    return Color(16, "Transparent", 0, 0, 0, 0)


def for_each_character(text: list[TextLine],
                       current_position: list[int],
                       result: list[Image.Image],
                       request: GenerationRequest,
                       frame_counter: list[int],) -> bool:
    line = text[current_position[0]]

    token = line.content[current_position[1]]

    content = token.content

    pauses = token.pauses

    has_pauses = False

    while current_position[2] < len(content):  # for each character
        text_copy = copy.deepcopy(text)

        deactivate_characters(text_copy, current_position[0], current_position[1], current_position[2])

        sprite = resolve_sprite(request.sprite_settings, frame_counter[0])

        sprite_right = resolve_sprite(request.right_sprite_settings, frame_counter[0])

        result.append(
            generate_single(text_copy, request.default_color, request.border_settings, sprite, sprite_right,
                            request.font_settings, request.export_settings))

        frame_counter[0] += 1

        pause = pauses.get(current_position[2] + 1, 0)

        if pause > 0:
            has_pauses = True
            frame_counter[0] = 0

            padding_image = generate_single(
                text_copy,
                request.default_color,
                request.border_settings,
                request.sprite_settings,
                request.right_sprite_settings,
                request.font_settings,
                request.export_settings,
            )

            for _ in range(pause):
                result.append(padding_image.copy())

        current_position[2] += 1

    last_pause = pauses.get(len(content), 0)

    sprite = request.sprite_settings
    sprite_right = request.right_sprite_settings

    padding_image = generate_single(text, request.default_color, request.border_settings, sprite,
                                    sprite_right, request.font_settings,request.export_settings)

    for _ in range(last_pause):
        result.append(padding_image.copy())

    only_pause = pauses.get(0, 0)

    if len(content) == 0 and 0 in pauses:
        for _ in range(only_pause):
            result.append(padding_image.copy())

    if last_pause > 0 or only_pause > 0:
        has_pauses = True

    if last_pause > 0 or only_pause > 0:
        frame_counter[0] = 0

    return has_pauses


def deactivate_characters(text_copy: list[TextLine], current_line: int, current_token: int, current_character: int):
    k = current_character + 1  # deactivate all characters after current

    line = text_copy[current_line]
    token = line.content[current_token]
    colors = token.colors

    colors = {key: val for key, val in colors.items() if key < k}
    colors[k] = get_transparent()

    token.colors = colors

def resolve_sprite(sprite_settings: SpriteSettings, frame_index: int) -> SpriteSettings:
    if sprite_settings.alternating_expression is None:
        return sprite_settings

    cycle_length = sprite_settings.alternating_interval + sprite_settings.alternating_duration
    cycle_pos = (frame_index + sprite_settings.alternating_interval) % cycle_length

    if cycle_pos < sprite_settings.alternating_interval:
        return sprite_settings

    alt = copy.copy(sprite_settings)
    alt.expression = sprite_settings.alternating_expression
    return alt


def generate_single(text_input: list[TextLine], default_color: Color, border_settings: BorderSettings,
                    sprite_settings: SpriteSettings, right_sprite_settings: SpriteSettings, font_settings: FontSettings,
                    export_settings: ExportSettings) -> Image.Image:
    from generation.steps import border_step, sprite_step, font_step_gif, export_step
    from generation.context import GenerationContext
    image, style = border_step.apply(border_settings)
    ctx = GenerationContext(image=image, has_expression=False, border_style=style)
    ctx = sprite_step.apply(ctx, sprite_settings, right_sprite_settings)
    ctx = font_step_gif.apply(ctx, text_input, default_color, font_settings)
    return export_step.apply(ctx, export_settings)