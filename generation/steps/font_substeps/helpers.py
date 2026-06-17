from PIL import ImageDraw, Image, ImageFont

from generation.steps.font_substeps.tokenizer import TextLine


def get_shadow_color(color: tuple[int,int,int,int]) -> tuple[int,int,int, int]:
    """1px drop-shadow = color/4; white uses special dark-blue shadow."""
    if color == (255, 255, 255, 255):
        return 15, 15, 113, 255 # Dark blue
    return color[0] // 4, color[1] // 4, color[2] // 4, color[3]

def get_character_size(text: str, char_width: int) -> int:
    return len(text) * char_width

def draw_string(
    img: Image.Image,
    x: int, y: int,
    text: str,
    color: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    with_shadow: bool,
    char_width: int,
    spacing: int = 0,
) -> int:
    if color[3] == 0:
        return get_character_size(text, char_width)
    if x >= img.width:
        return get_character_size(text, char_width)

    start_x = x
    for char in text:
        draw_single(img, x, y, char, color, font, with_shadow, char_width)
        x += char_width + spacing
    return x - start_x

def draw_single(
    img: Image.Image,
    x: int, y: int,
    text: str,
    color: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    with_shadow: bool,
    char_width: int
) -> int:
    if with_shadow:
        return draw_gradient_string(img, x, y, text, color, font, char_width)
    draw = ImageDraw.Draw(img)
    draw.fontmode = "1"
    draw.text((x, y), text, font=font, fill=color)
    return get_character_size(text, char_width)

def draw_gradient_string(
    image: Image.Image,
    x: int, y: int,
    text: str,
    color: tuple[int, int, int, int],
    font: ImageFont.FreeTypeFont,
    char_width: int,
    gradient_strength: float = 0.45,  # 0.0 = no gradient, 1.0 = white on top
) -> int:
    draw = ImageDraw.Draw(image)
    draw.fontmode = "1"

    # calculate bounding box of the text
    bbox = font.getbbox(text)           # (left, top, right, bottom)
    text_w = int(bbox[2] - bbox[0])
    text_h = int(bbox[3] - bbox[1])

    if text_w <= 0 or text_h <= 0:
        return get_character_size(text, char_width)

    # render text as white mask on black background
    mask_img = Image.new("L", (text_w, text_h), 0)
    mask_draw = ImageDraw.Draw(mask_img)
    mask_draw.fontmode = "1"
    mask_draw.text((-bbox[0], -bbox[1]), text, font=font, fill=255)

    # generate vertical colorgradient: brighter at top -> base color at the bottom
    gradient_img = Image.new("RGB", (text_w, text_h))
    gd = ImageDraw.Draw(gradient_img)
    for row in range(text_h):
        t = row / max(text_h - 1, 1)          # 0.0 at the top -> 1.0 at the bottom
        blend = (1.0 - t) * gradient_strength  # higher up -> more brightness

        r = min(255, int(color[0] + (255 - color[0]) * blend))
        g = min(255, int(color[1] + (255 - color[1]) * blend))
        b = min(255, int(color[2] + (255 - color[2]) * blend))
        gd.line([(0, row), (text_w - 1, row)], fill=(r, g, b))

    # use mask as alpha-channel
    gradient_img.putalpha(mask_img)

    # put shadow below text before pasting
    draw.text((x + 1, y + 1), text, font=font, fill=get_shadow_color(color))

    # paste on main picture (only where mask is white)
    image.paste(gradient_img, (int(x + bbox[0]), int(y + bbox[1])), mask=mask_img)

    return get_character_size(text, char_width)

# DOESN'T WORK WITH WINGDINGS!
def measure_line(line: TextLine, char_width: int) -> int:
    parts = [t.content for t in line.content]
    text = ("* " if line.has_asterisk else "") + " ".join(parts)
    return get_character_size(text, char_width)