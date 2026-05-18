# SECOND
from generation.context import GenerationContext
from models.form_bindings import SpriteSettings


def apply(ctx: GenerationContext, settings: SpriteSettings) -> GenerationContext:
    if settings.expression is None:
        return ctx  # include not checked
        # load expression, replace white, insert expression on the left
    ctx.has_expression = True
    return ctx