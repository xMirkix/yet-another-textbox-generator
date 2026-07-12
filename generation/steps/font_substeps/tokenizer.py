from __future__ import annotations
from dataclasses import dataclass

from services.database_service import DBStaticConnection
from startup.in_memory.static_classes import Color, TextTransform
from configs.paths import STATIC_DB

@dataclass
class TextToken:  # One word
    content: str
    colors: dict[int, Color]
    pauses: dict[int, int]

@dataclass
class TextLine:
    content: list[TextToken]
    has_asterisk: bool

def tokenize(text: str, transform: TextTransform, has_asterisk: bool) -> list[TextLine]:
    connection = DBStaticConnection(STATIC_DB)
    lines = text.split("\n")
    return [for_each_line(line, transform, has_asterisk, connection) for line in lines]


def for_each_line(line: str, transform: TextTransform, has_asterisk: bool, connection: DBStaticConnection) -> TextLine:
    parts = line.split(" ")
    tokens = [tokenize_word(part, transform, connection) for part in parts]
    return TextLine(tokens, has_asterisk)


def tokenize_word(part: str, transform: TextTransform, connection: DBStaticConnection) -> TextToken:
    colors: dict[int, Color] = {}
    pauses: dict[int, int] = {}

    while True:
        tag = find_next_tag(part)
        if tag is None:
            break

        tag_type, index, closing, value = tag

        if tag_type == "color":
            extract_color(value, connection, index, colors)
        elif tag_type == "pause":
            extract_pause(value, index, pauses)

        part = part[:index] + part[closing + 1:]

    return TextToken(apply_transform(part, transform), colors, pauses)


def find_next_tag(part: str) -> tuple[str, int, int, str] | None:
    tag_prefixes = {"color": "color=<", "pause": "pause=<"}

    candidates = []
    for tag_type, prefix in tag_prefixes.items():
        index = part.find(prefix)
        if index != -1:
            candidates.append((index, tag_type, prefix))

    if not candidates:
        return None

    index, tag_type, prefix = min(candidates, key=lambda c: c[0])
    closing = part.find(">", index)
    if closing == -1:
        return None

    value = part[index + len(prefix):closing]
    return tag_type, index, closing, value


def extract_color(color_name: str, connection: DBStaticConnection, index: int, colors: dict[int, Color]) -> None:
    color_name = color_name.capitalize().replace("-", " ")
    found_colors = connection.select_color_by_name(color_name)
    if found_colors:
        colors[index] = found_colors[0]


def extract_pause(pause_value: str, index: int, pauses: dict[int, int]) -> None:
    try:
        pauses[index] = int(pause_value)
    except ValueError:
        pass


def apply_transform(part: str, transform: TextTransform) -> str:
    if transform.transform_id == 2:
        return part.upper()
    if transform.transform_id == 3:
        return part.lower()
    if transform.transform_id == 4:
        return capitalize_first_letter(part)
    return part


def capitalize_first_letter(text: str) -> str:
    for i, char in enumerate(text):
        if char.isalpha():
            return text[:i] + char.upper() + text[i + 1:].lower()
    return text