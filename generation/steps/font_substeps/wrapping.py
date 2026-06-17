from PIL import ImageFont
from PIL.ImageFont import FreeTypeFont

from generation.steps.font_substeps.helpers import get_character_size
from generation.steps.font_substeps.tokenizer import TextLine, TextToken


def calculate_wrapping(
    text: list[TextLine],
    font: ImageFont.FreeTypeFont,
    max_width: int,
) -> list[TextLine]:
    space_w = get_character_size(" ", font)
    asterisk_w = get_character_size("* ", font)

    if font.getname()[0] == "Wingdings":
        asterisk_w = get_character_size("*", font)

    result: list[TextLine] = []

    for line in text:
        for_each_line(result, line, max_width, space_w, asterisk_w, font)

        if len(result) >= 3:
            return result[:3]

    return result[:3]

def for_each_line(result: list[TextLine], line: TextLine, max_width: int, space_w: int, asterisk_w: int, font: FreeTypeFont) -> None:
    current: list[TextToken] = []
    current_width: int = asterisk_w if line.has_asterisk else 0
    is_first_chunk = True

    for token in line.content:
        token_w = get_character_size(token.content, font)
        gap = space_w if current else 0

        if current and current_width + gap + token_w > max_width: # line has to be wrapped
            result.append(TextLine(current, line.has_asterisk and is_first_chunk))
            is_first_chunk = False
            current = [token]
            current_width = token_w
            if len(result) >= 3: # Doesn't need to process extra tokens beyond limit
                return
        else:
            current.append(token)
            current_width += gap + token_w

    if current:
        result.append(TextLine(current, line.has_asterisk and is_first_chunk))
