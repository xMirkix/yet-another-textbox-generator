# FIRST
from PIL import Image

from configs.paths import BORDERS_DIR
from models.form_bindings import BorderSettings


def apply(settings: BorderSettings) -> Image.Image:
    if settings.style.source_image_file_name == "Original Box":
        return apply_original(settings)
    elif settings.style.source_image_file_name == "Deltarune":
        return apply_deltarune(settings)
    raise ValueError(f"Unknown border style: {settings.style.source_image_file_name}")

def apply_original(settings: BorderSettings) -> Image.Image:
    width, height = 289, 76
    result = Image.new("RGB", (width, height), (0, 0, 0))

    r, g, b = settings.color.r, settings.color.g, settings.color.b
    border_thickness = 3

    pixels = result.load()
    for x in range(width):
        for y in range(height):
            if (x < border_thickness or x >= width - border_thickness or
                    y < border_thickness or y >= height - border_thickness):
                pixels[x, y] = (r, g, b)

    return result

# Color of corner dots: rgb(170, 255, 230)
def apply_deltarune(settings: BorderSettings) -> Image.Image:
    border_path = BORDERS_DIR / "Deltarune.png"
    border_source = Image.open(border_path).convert("RGBA")

    width, height = 297, 84
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))


    r, g, b = settings.color.r, settings.color.g, settings.color.b

    colored_border = Image.new("RGBA", border_source.size, (0, 0, 0, 0))
    pixels_src = border_source.load()
    pixels_dst = colored_border.load()

    for x in range(border_source.width):
        for y in range(border_source.height):
            pixel_src_r, pixel_src_g, pixel_src_b, pixel_src_alpha = pixels_src[x, y]
            if pixel_src_alpha > 0:
                brightness = (pixel_src_r + pixel_src_g + pixel_src_b) / (3 * 255)
                pixels_dst[x, y] = (
                    int(r * brightness),
                    int(g * brightness),
                    int(b * brightness),
                    pixel_src_alpha
                )

    pixels_dst[6, 6] = (170, 255, 230, 255)
    pixels_dst[290, 6] = (170, 255, 230, 255)
    pixels_dst[6, 77] = (170, 255, 230, 255)
    pixels_dst[290, 77] = (170, 255, 230, 255)

    image.paste(colored_border, (0, 0), colored_border)
    return image