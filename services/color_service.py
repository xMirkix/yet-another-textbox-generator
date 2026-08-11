import io
from io import BytesIO

from PIL import Image

from models.entities import Expression


def is_similar(
    primary_hsv: tuple[float, float, float],
    pixel_hsv: tuple[float, float, float],
    hue_threshold: float = 0.08,
    sat_threshold: float = 0.25,
) -> bool:
    hp, sp, vp = primary_hsv
    h, s, v = pixel_hsv

    if sp <= sat_threshold:
        return s <= sat_threshold

    return hue_diff(hp, h) <= hue_threshold and abs(sp - s) <= sat_threshold

def get_primary_color(image: Image.Image) -> tuple[int, int, int] | None:
    pixels = image.load()
    amounts: dict[tuple[int, int, int], int] = {}
    for x in range(image.width):
        for y in range(image.height):
            r, g, b, a = pixels[x, y]
            if a == 0 or (r, g, b) == (0, 0, 0): continue
            key = (r, g, b)
            amounts[key] = amounts.get(key, 0) + 1

    if not amounts:
        return None

    max_amount_color = None
    max_amount = 0
    for c, amount in amounts.items():
        if amount > max_amount:
            max_amount = amount
            max_amount_color = c
    return max_amount_color

def clamp01(v: float) -> float:
    return max(0.0, min(1.0, v))


def hue_diff(h1: float, h2: float) -> float:
    d = abs(h1 - h2)
    return min(d, 1.0 - d)

def bytes_to_image(image_bytes: bytes) -> Image.Image:
    return Image.open(io.BytesIO(image_bytes)).convert("RGBA")

def fit_image_to_resolution(expression: Expression) -> Image.Image:
    image = bytes_to_image(expression.preview_image)

    return fit_logic(image)


def fit_expression_image(blob: bytes) -> bytes:
    image = Image.open(BytesIO(blob)).convert("RGBA")

    result = fit_logic(image)

    output = BytesIO()
    result.save(output, format="PNG")

    return output.getvalue()



def fit_logic(image: Image.Image) -> Image.Image:
    result = Image.new("RGBA", (67, 70), (0, 0, 0, 255))

    x = (67 - image.width) // 2
    y = (70 - image.height) // 2
    result.paste(image, (x, y), image)

    return result

