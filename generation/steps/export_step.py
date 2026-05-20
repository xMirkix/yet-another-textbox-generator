# FOURTH
from PIL import Image

from generation.context import GenerationContext
from models.form_bindings import ExportSettings, ExportSize


def apply(ctx: GenerationContext, settings: ExportSettings) -> Image.Image:
    # Margin and scaling

    image = apply_margin(ctx, settings)

    amount = get_scale_amount(settings.size)

    image = image.resize((image.width * amount, image.height * amount), Image.Resampling.NEAREST)
    return image

def apply_margin(ctx: GenerationContext, settings: ExportSettings) -> Image.Image:
    if settings.margin:
        src_image = ctx.image.convert("RGBA")

        width = src_image.width + 6
        height = src_image.height + 6
        image = Image.new("RGBA", (width, height), (0, 0, 0, 255))

        image.paste(src_image, (3, 3), src_image)
        return image
    return ctx.image

def get_scale_amount(size: ExportSize):
    if size == ExportSize.SMALL:
        return 1
    if size == ExportSize.MEDIUM:
        return 2
    if size == ExportSize.BIG:
        return 3
    return 1
