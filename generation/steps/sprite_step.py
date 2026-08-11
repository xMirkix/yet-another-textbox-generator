# SECOND
import colorsys
import io
from typing import Callable

from PIL import Image

from generation.context import GenerationContext
from models.entities import Expression
from models.form_bindings import SpriteSettings, ColorType
from services.color_service import get_primary_color, fit_image_to_resolution, clamp01, is_similar
from startup.in_memory.static_classes import Color


def apply(ctx: GenerationContext, settings: SpriteSettings, right_settings: SpriteSettings) -> GenerationContext:
    left_pos, right_pos = get_insert_positions(ctx.border_style)
    resolution = get_resolution(ctx.border_style)

    left_image = make_filler()

    if settings.expression is not None:
        ctx.has_expression = True
        fixed = fit_image_to_resolution(settings.expression)
        left_image = color_image_if_color_present(fixed, settings.expression_color, settings.color_type, settings.selected_colors, settings.simple_recoloring)

    right_image = make_filler()

    if right_settings.expression is not None:
        ctx.has_right_expression = True
        fixed = fit_image_to_resolution(right_settings.expression)
        right_image = color_image_if_color_present(fixed, right_settings.expression_color, settings.color_type, settings.selected_colors, settings.simple_recoloring)

    return apply_expression(left_image, right_image, ctx, left_pos, right_pos, resolution)

def make_filler() -> Image.Image:
    return Image.new("RGBA", (67, 70), (0, 0, 0, 255))

def color_image_if_color_present(image: Image.Image, color: Color | None, color_type: ColorType | None, selected_colors: tuple | None, simple_recoloring: bool | None, hue_threshold: float = 0.08, sat_threshold: float = 0.25, ) -> Image.Image:
    if color is None or color_type is None:
        return image

    if color_type == ColorType.CUSTOM:
        return simple_color_logic(image, color, selected_colors, simple_recoloring)

    if color_type == ColorType.EVERYTHING:
        return complex_color_logic(image, color, False)

    return complex_color_logic(image, color, True)

def simple_color_logic(image: Image.Image, color: Color, selected_colors: tuple | None, simple_recoloring: bool) -> Image.Image:
    if selected_colors is None or simple_recoloring is None:
        return image

    primary = get_primary_color(image)
    if primary is None:
        return image

    pr, pg, pb = primary
    _, _, vp = colorsys.rgb_to_hsv(pr / 255, pg / 255, pb / 255)
    ht, st, vt = colorsys.rgb_to_hsv(color.r / 255, color.g / 255, color.b / 255)

    pixels = image.load()

    for x in range(image.width):
        for y in range(image.height):

            r, g, b, a = pixels[x, y]

            if a == 0: continue
            if (r, g, b) == (0, 0, 0): continue

            c = Color(-1, "", r, g, b)

            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

            if c in selected_colors:
                if simple_recoloring:
                    pixels[x, y] = (color.r, color.g, color.b, color.a)
                else:
                    delta_v = v - vp
                    new_v = clamp01(vt + delta_v)

                    nr, ng, nb = colorsys.hsv_to_rgb(ht, st, new_v)
                    pixels[x, y] = (round(nr * 255), round(ng * 255), round(nb * 255),
                                    a)  # color in pixels with adjusted new color

    return image


def complex_color_logic(image: Image.Image, color: Color, is_simple: bool, hue_threshold: float = 0.08, sat_threshold: float = 0.25,):
    result = image.convert("RGBA")
    primary = get_primary_color(result)
    if primary is None:
        return result

    pr, pg, pb = primary
    hp, sp, vp = colorsys.rgb_to_hsv(pr / 255, pg / 255, pb / 255)
    ht, st, vt = colorsys.rgb_to_hsv(color.r / 255, color.g / 255, color.b / 255)
    pixels = result.load()

    for x in range(result.width):
        for y in range(result.height):
            r, g, b, a = pixels[x, y]
            if a == 0: # skip transparent pixels
                continue
            if (r, g, b) == (0, 0, 0): # skip black pixels
                continue

            h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)

            if is_simple and not is_similar((hp, sp, vp), (h, s, v), hue_threshold, sat_threshold): # color is distinct enough to not get colored (e.g., eyes)
                continue

            delta_v = v - vp
            new_v = clamp01(vt + delta_v)

            nr, ng, nb = colorsys.hsv_to_rgb(ht, st, new_v)
            pixels[x, y] = (round(nr * 255), round(ng * 255), round(nb * 255), a) # color in pixels with adjusted new color

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