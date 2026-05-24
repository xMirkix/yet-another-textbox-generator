# SECOND
import io

from PIL import Image, ImageDraw

from generation.context import GenerationContext
from models.entities import Expression
from models.form_bindings import SpriteSettings
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, settings: SpriteSettings) -> GenerationContext:
    if settings.expression is None:
        return ctx  # include not checked
    ctx.has_expression = True

    fixed_resolution_image = fit_image_to_resolution(settings.expression) # load and adapt expression if needed

    color_corrected_image = color_image_if_no_color_present(fixed_resolution_image, settings.expression_color) # color correct expression if needed

    insert_position = get_correct_insert_position(ctx.border_style) # get correct insert position

    if ctx.border_style == "Deltarune":
        return apply_deltarune(color_corrected_image, ctx, insert_position) # extra processing for border corner needed
    else:
        ctx.image.paste(add_black_border(color_corrected_image), insert_position, color_corrected_image) # Undertale style simple paste with black border for least padding
        return ctx


def fit_image_to_resolution(expression: Expression) -> Image.Image:
    image = bytes_to_image(expression.preview_image)

    result = Image.new("RGBA", (69, 70), (0, 0, 0, 0))

    x = (69 - image.width) // 2
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

def get_correct_insert_position(border_style) -> tuple[int, int]:
    if border_style == "Deltarune":
        return 7, 7
    else:
        return 3, 3

def add_black_border(image: Image.Image, thickness: int = 1) -> Image.Image:
    draw = ImageDraw.Draw(image)
    w, h = image.size
    for i in range(thickness):
        draw.rectangle([i, i, w - 1 - i, h - 1 - i], outline=(0, 0, 0, 255))
    return image

def apply_deltarune(image: Image.Image, ctx, insert_position: tuple[int, int]) -> GenerationContext:
    upper_left = ctx.image.crop((7, 7, 14, 14)) # upper left triangle for insert
    down_left = ctx.image.crop((7, 70, 14, 77)) # down left triangle for
    black_line = ctx.image.crop((7, 13, 8, 71)) # black line for padding
    upper_black_line = ctx.image.crop((13, 7, 75, 8))
    down_left_line = ctx.image.crop((13, 76, 75, 77))
    ctx.image.paste(image, insert_position, image) # insert image, can overlap with border
    ctx.image.paste(black_line, (7, 13), black_line) # add padding line 1
    ctx.image.paste(upper_black_line, (13, 7), upper_black_line) # add padding line 2
    ctx.image.paste(down_left_line, (13, 76), down_left_line) # add padding line 3

    apply_upper_left(upper_left, ctx) # apply upper left triangle

    apply_down_left(down_left, ctx) # apply down left triangle

    return ctx

def apply_upper_left(cropped_image: Image.Image, ctx) -> None:
    origin = 7

    for y in range(cropped_image.height):
        for x in range(cropped_image.width):
            if x > origin - y:
                cropped_image.putpixel((x, y), (0, 0, 0, 0))

    ctx.image.paste(cropped_image, (7, 7), cropped_image)

def apply_down_left(cropped_image: Image.Image, ctx) -> None:
    origin = 1
    for y in range(cropped_image.height):
        for x in range(cropped_image.width):
            if x > origin + y:
                cropped_image.putpixel((x, y), (0, 0, 0, 0))

    ctx.image.paste(cropped_image, (7, 70), cropped_image)