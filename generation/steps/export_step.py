# FOURTH
from PIL import Image

from generation.context import GenerationContext
from models.form_bindings import ExportSettings


def apply(ctx: GenerationContext, settings: ExportSettings) -> Image.Image:
    # Margin and scaling
    return ctx.image