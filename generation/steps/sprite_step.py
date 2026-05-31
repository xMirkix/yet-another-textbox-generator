# SECOND
import io

from PIL import Image, ImageDraw

from generation.context import GenerationContext
from models.entities import Expression
from models.form_bindings import SpriteSettings
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, settings: SpriteSettings) -> GenerationContext:
    if settings.expression is None:
        filler = Image.new("RGBA", (67, 70), (0, 0, 0, 255))
        apply_expression(filler, ctx, get_insert_position(ctx.border_style), get_resolution(ctx.border_style))
        return ctx  # include not checked
    ctx.has_expression = True

    fixed_resolution_expression = fit_image_to_resolution(settings.expression) # load and adapt expression if needed

    color_corrected_expression = color_image_if_no_color_present(fixed_resolution_expression, settings.expression_color) # color correct expression if needed

    return apply_expression(color_corrected_expression, ctx, get_insert_position(ctx.border_style), get_resolution(ctx.border_style))


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
                pixels[x, y] = (color.r, color.g, color.b, a)
    return result

def get_resolution(border_style) -> tuple[int, int]:
    if border_style == "Deltarune":
        return 297, 84
    return 289, 76

def get_insert_position(border_style) -> tuple[int, int]:
    if border_style == "Deltarune":
        return 7, 7
    return 3, 3

def apply_expression(expression: Image.Image, ctx, insert_position: tuple[int, int], resolution: tuple[int, int]) -> GenerationContext:
    result = Image.new("RGBA", resolution, (0, 0, 0, 0))
    result.paste(expression, insert_position, expression)
    result.paste(ctx.image, (0, 0), ctx.image)

    if ctx.border_style == "Deltarune": # Fix bug with pixels that are out of border
        result.putpixel((7, 7), (0, 0, 0, 0))
        result.putpixel((7, 76), (0, 0, 0, 0))

    ctx.image = result
    return ctx