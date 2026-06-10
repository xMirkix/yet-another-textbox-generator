from PIL import ImageFont, ImageDraw, Image

from generation.steps.font_step import FontConfig
from generation.steps.font_substeps.tokenizer import TextLine, TextToken


def get_shadow_color(color: tuple[int,int,int]) -> tuple[int,int,int]:
    """1px drop-shadow = color/4; white uses special dark-blue shadow."""
    if color == (255, 255, 255):
        return 15, 15, 113 # Dark blue
    return color[0] // 4, color[1] // 4, color[2] // 4

def get_character_size(font: ImageFont.FreeTypeFont, text: str) -> int:
    draw = ImageDraw.Draw(Image.new("RGBA", (1, 1)))
    return int(draw.textlength(text, font=font))

def draw_string(
    draw: ImageDraw.ImageDraw,
    x: int, y: int,
    text: str,
    color: tuple[int, int, int],
    font: ImageFont.FreeTypeFont,
    with_shadow: bool,
) -> int:
    """Draws a string (whole run of same color) at once — preserves kerning."""
    if with_shadow:
        draw.text((x + 1, y + 1), text, font=font, fill=get_shadow_color(color))
    draw.text((x, y), text, font=font, fill=color)
    return get_character_size(font, text)

def measure_line(line: TextLine, font: ImageFont.FreeTypeFont) -> int:
    parts = [t.content for t in line.content]
    text = ("* " if line.has_asterisk else "") + " ".join(parts)
    return get_character_size(font, text)

def get_text_image(
    text: list[TextLine],
    dark_world: bool,
    font: ImageFont.FreeTypeFont,
    config: FontConfig,
) -> Image.Image:
    default_color: tuple[int, int, int] = (255, 255, 255)
    line_height = config["line_height"]

    img_w = max((measure_line(line, font) for line in text), default=1) + 2
    img_h = len(text) * line_height + 2
    img   = Image.new("RGBA", (img_w, img_h), (0, 0, 0, 0))
    draw  = ImageDraw.Draw(img)

    draw.fontmode = "1"

    for i, line in enumerate(text):
        x = 0
        y = i * line_height

        if line.has_asterisk:
            x += draw_string(draw, x, y, "* ", default_color, font, dark_world)

        for j, token in enumerate(line.content):
            if j > 0:
                x += draw_string(draw, x, y, " ", default_color, font, dark_world)

            # Batch characters of the same color → draw as one string (fixes kerning)
            current_color = default_color
            batch = ""
            for ci, char in enumerate(token.content):
                if ci in token.colors:
                    c = token.colors[ci]
                    new_color: tuple[int, int, int] = (c.r, c.g, c.b)
                else:
                    new_color = current_color

                if new_color != current_color:
                    if batch:
                        x += draw_string(draw, x, y, batch, current_color, font, dark_world)
                    batch = char
                    current_color = new_color
                else:
                    batch += char

            if batch:
                x += draw_string(draw, x, y, batch, current_color, font, dark_world)

    return img

def calculate_wrapping(
    text: list[TextLine],
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[TextLine]:
    space_w    = get_character_size(font, " ")
    asterisk_w = get_character_size(font, "* ")
    result: list[TextLine] = []

    for line in text:
        current:       list[TextToken] = []
        current_width: int             = asterisk_w if line.has_asterisk else 0
        is_first_chunk                 = True

        for token in line.content:
            token_w = get_character_size(font, token.content)
            gap     = space_w if current else 0

            if current and current_width + gap + token_w > max_width:
                result.append(TextLine(current, line.has_asterisk and is_first_chunk))
                is_first_chunk = False
                current        = [token]
                current_width  = token_w
            else:
                current.append(token)
                current_width += gap + token_w

        if current:
            result.append(TextLine(current, line.has_asterisk and is_first_chunk))

    return result