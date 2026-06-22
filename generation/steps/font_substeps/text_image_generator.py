from PIL import ImageFont, Image

from generation.steps.font_step import FontConfig
from generation.steps.font_substeps.helpers import get_character_size, draw_string
from generation.steps.font_substeps.tokenizer import TextLine, TextToken
from generation.steps.font_substeps.wrapping import calculate_wrapping
from startup.in_memory.static_classes import Color

# logic

def get_text_image(
    text: list[TextLine],
    default_color: Color,
    dark_world: bool,
    font: ImageFont.FreeTypeFont,
    config: FontConfig,
    max_size: tuple[int, int],
    asterisk_color: list[Color],
) -> Image.Image:
    default_color = (default_color.r, default_color.g, default_color.b, default_color.a)

    line_height = config["line_height"]

    img_w = max_size[0] - 1 # - 1 for border padding

    img_h = max_size[1]

    img = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))

    text = calculate_wrapping(text, font, img_w - 2,
                          config["character_extra_offset"],
                          config["space_extra_offset"],
                          config["initial_asterisk_offset"])

    is_asterisk_break = count_asterisk_lines(text) == 2 and (not text[1].has_asterisk)

    for i, line in enumerate(text):
        draw_for_each_line(i,
                           img,
                           line,
                           line_height,
                           default_color,
                           font, dark_world,
                           asterisk_color,
                           config["initial_asterisk_offset"],
                           config["character_extra_offset"],
                           config["space_extra_offset"],
                           is_asterisk_break)

    return img

def count_asterisk_lines(text: list[TextLine]) -> int:
    count = 0
    for line in text:
        if line.has_asterisk:
            count += 1
    return count

def draw_for_each_line(
    index: int,
    img: Image.Image,
    line: TextLine,
    line_height: int,
    default_color: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    dark_world: bool,
    asterisk_color: list[Color],
    asterisk_offset: int,
    character_offset: int,
    space_offset: int,
    is_asterisk_break: bool,
) -> None:
    x = 0
    y = index * line_height

    x += manage_asterisk(img, x, y, line.has_asterisk, font, dark_world, asterisk_color, index, is_asterisk_break, asterisk_offset)

    for j, token in enumerate(line.content):
        x = draw_for_each_token(x, y, j, img, token, default_color, font, dark_world, character_offset, space_offset)

def draw_for_each_token(
    x: int,
    y: int,
    index: int,
    img: Image.Image,
    token: TextToken,
    default_color: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    dark_world: bool,
    character_offset: int,
    space_offset: int,
) -> int:
    if index > 0: # for adding space between tokens
        x += draw_string(img, x, y, " ", default_color, font, dark_world, 0) + space_offset

    # Batch characters of the same color -> draw as one string
    current_color = default_color
    batch = ""
    for ci, char in enumerate(token.content): # for each character in the token (could be mid-token color switch)
        if ci in token.colors: # is a switch color index?
            if batch: # draw previous batch
                x += draw_string(img, x, y, batch, current_color, font, dark_world, character_offset)
            batch = char

            color = token.colors[ci] # get new color
            current_color = (color.r, color.g, color.b, color.a)

        else: # just add to batch
            batch += char

    if batch: # draw last batch (or only if no switch entry)
        x += draw_string(img, x, y, batch, current_color, font, dark_world, character_offset)

    return x


def manage_asterisk(
        img: Image.Image,
        x: int,
        y: int,
        has_asterisk: bool,
        font: ImageFont.FreeTypeFont,
        dark_world: bool,
        asterisk_color: list[Color],
        index: int,
        is_asterisk_break: bool,
        offset: int,
) -> int:
    if asterisk_color is None or len(asterisk_color) == 0: # No asterisk
        return 0

    if not has_asterisk and font.getname()[0] == "Wingdings":
        return get_character_size("*", font) + offset

    if not has_asterisk: # Wrapped line, asterisk padding
        return get_character_size("* ", font) + offset

    if index == 2 and is_asterisk_break:
        index -= 1

    color = (asterisk_color[index].r, asterisk_color[index].g, asterisk_color[index].b, asterisk_color[index].a)

    if font.getname()[0] == "Wingdings":
        return draw_string(img, x, y, "*", color , font, dark_world, 0)

    return draw_string(img, x, y, "* ", color, font, dark_world, 0) + offset # offset for longer/shorter space between asterisk and text
