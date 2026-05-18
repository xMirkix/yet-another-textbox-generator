# THIRD
from generation.context import GenerationContext
from models.form_bindings import FontSettings


def apply(ctx: GenerationContext, text: str, settings: FontSettings) -> GenerationContext:
    # Text offset if it has_expression
    # Apply transform, line breaks, asterisks and dark world
    return ctx
