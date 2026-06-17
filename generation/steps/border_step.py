# FIRST
from PIL import Image

from configs.paths import BORDERS_DIR
from models.form_bindings import BorderSettings


def apply(settings: BorderSettings) -> tuple[Image.Image, str]:
    return apply_border(settings, settings.style.source_image_file_name, get_resolution(settings)), settings.style.source_image_file_name

def get_resolution(settings: BorderSettings) -> tuple[int, int]:
    if settings.style.source_image_file_name == "Deltarune":
        return 297, 84
    return 289, 76

def apply_border(settings: BorderSettings, source_image, resolution: tuple[int, int]) -> Image.Image:
    suffix = source_image + '.png'
    border_path = BORDERS_DIR / suffix
    border_source = Image.open(border_path).convert("RGBA")

    width, height = resolution
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    r, g, b = get_color_with_least_values(settings.color.r, settings.color.g, settings.color.b)

    pixels_src = border_source.load()
    pixels_dst = result.load()

    for x in range(border_source.width):
        for y in range(border_source.height):
            for_each_pixel(x, y, (r, g, b, settings.color.a), pixels_src, pixels_dst)

    if settings.style.source_image_file_name == "Deltarune" and settings.color.a == 255:
        set_corners(pixels_dst) # Replace 4 Dots in Corner with right color

    return result


def for_each_pixel(x: int, y: int, rgb: tuple[int, int, int, int], pixels_src, pixels_dst):
    pixel_src_r, pixel_src_g, pixel_src_b, pixel_src_alpha = pixels_src[x, y]

    if pixel_src_alpha > 0:
        brightness = (pixel_src_r + pixel_src_g + pixel_src_b) / (3 * 255)
        final_r = int(rgb[0] * brightness) % 256
        final_g = int(rgb[1] * brightness) % 256
        final_b = int(rgb[2] * brightness) % 256
        final_a = 255 if (pixel_src_r + pixel_src_g + pixel_src_b) == 0 else rgb[3]

        pixels_dst[x, y] = (
            final_r,
            final_g,
            final_b,
            final_a
            )

def get_color_with_least_values(r: int, g: int, b: int) -> tuple[int, int, int]:
    if r + g + b < 50:
        return max(r, 20), max(g, 20), max(b, 20)
    return r, g, b


def set_corners(pixels_dst):
    pixels_dst[6, 6] = (170, 255, 230, 255)
    pixels_dst[290, 6] = (170, 255, 230, 255)
    pixels_dst[6, 77] = (170, 255, 230, 255)
    pixels_dst[290, 77] = (170, 255, 230, 255)