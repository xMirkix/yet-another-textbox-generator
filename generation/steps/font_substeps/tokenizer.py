from __future__ import annotations
from dataclasses import dataclass

from services.database_service import DBStaticConnection
from startup.in_memory.static_classes import Color, TextTransform

@dataclass
class TextToken: # One word
    content: str
    colors: dict[int, Color]

@dataclass
class TextLine:
    content: list[TextToken]
    has_asterisk: bool

def tokenize(text: str, transform: TextTransform, has_asterisk: bool) -> list[TextLine]:
    connection = DBStaticConnection()
    lines = text.split("\n")
    text_lines: list[TextLine] = []

    for line in lines:
        text_lines.append(for_each_line(line, transform, has_asterisk, connection))

    return text_lines

def for_each_line(line: str, transform: TextTransform, has_asterisk: bool, connection: DBStaticConnection) -> TextLine:
    parts = line.split(" ")
    tokens: list[TextToken] = []
    for part in parts:
        colors = {}
        index = part.find("color=<")
        while index != -1:
            closing = part.find(">", index)
            if closing == -1:
                break

            color_name = part[index + 7:closing]
            color_name = color_name.capitalize()
            color_name = color_name.replace("-", " ")
            found_colors = connection.select_color_by_name(color_name)

            if found_colors:
                colors[index] = found_colors[0]

            part = part[:index] + part[closing + 1:]

            index = part.find("color=<", index)

        tokens.append(TextToken(apply_transform(part, transform), colors))

    return TextLine(tokens, has_asterisk)

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
            return text[:i] + char.upper() + text[i+1:].lower()
    return text