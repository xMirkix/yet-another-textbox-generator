# SECOND
import io

from PIL import Image

from generation.context import GenerationContext
from models.entities import Expression
from models.form_bindings import SpriteSettings
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, settings: SpriteSettings, right_settings: SpriteSettings) -> GenerationContext:
    left_pos, right_pos = get_insert_positions(ctx.border_style)
    resolution = get_resolution(ctx.border_style)

    left_image = make_filler()

    if settings.expression is not None:
        ctx.has_expression = True
        fixed = fit_image_to_resolution(settings.expression)
        left_image = color_image_if_no_color_present(fixed, settings.expression_color)

    right_image = make_filler()

    if right_settings.expression is not None:
        ctx.has_right_expression = True
        fixed = fit_image_to_resolution(right_settings.expression)
        right_image = color_image_if_no_color_present(fixed, right_settings.expression_color)

    return apply_expression(left_image, right_image, ctx, left_pos, right_pos, resolution)

def make_filler() -> Image.Image:
    return Image.new("RGBA", (67, 70), (0, 0, 0, 255))

def fit_image_to_resolution(expression: Expression) -> Image.Image:
    image = bytes_to_image(expression.preview_image)

    result = Image.new("RGBA", (67, 70), (0, 0, 0, 255))

    x = (67 - image.width) // 2
    y = (70 - image.height) // 2
    result.paste(image, (x, y), image)

    return result

def bytes_to_image(image_bytes: bytes) -> Image.Image:
    return Image.open(io.BytesIO(image_bytes)).convert("RGBA")

def color_image_if_no_color_present(image: Image.Image, color: Color) -> Image.Image:
    result = image.convert("RGBA")
    pixels = result.load()
    for x in range(result.width):
        for y in range(result.height):
            r, g, b, a = pixels[x, y]
            if a == 0: # skip transparent pixels
                continue
            if (r, g, b) not in ((0, 0, 0), (255, 255, 255)): # expression already has a color
                return image
            if (r, g, b) == (255, 255, 255): # white pixel gets recolored
                pixels[x, y] = (color.r, color.g, color.b, color.a)
    return result

def get_resolution(border_style) -> tuple[int, int]:
    if border_style == "Deltarune":
        return 297, 84
    return 289, 76

def get_insert_positions(border_style) -> tuple[tuple[int, int], tuple[int, int]]:
    if border_style == "Deltarune":
        return (7, 7), (223, 7)
    return (3, 3), (219, 3)

def apply_expression(left: Image.Image, right: Image.Image | None, ctx: GenerationContext,
                     left_pos: tuple[int, int], right_pos: tuple[int, int],
                     resolution: tuple[int, int]) -> GenerationContext:
    result = Image.new("RGBA", resolution, (0, 0, 0, 0))
    result.paste(left, left_pos, left)

    if right is not None:
        result.paste(right, right_pos, right)

    result.paste(ctx.image, (0, 0), ctx.image)

    if ctx.border_style == "Deltarune": # Fix bug with pixels that are out of border
        result.putpixel((7, 7), (0, 0, 0, 0))
        result.putpixel((7, 76), (0, 0, 0, 0))

        if right is not None:
            result.putpixel((289, 7),  (0, 0, 0, 0))
            result.putpixel((289, 76), (0, 0, 0, 0))

    ctx.image = result
    return ctx