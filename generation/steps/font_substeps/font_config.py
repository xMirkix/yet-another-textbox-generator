from typing import TypedDict


class FontConfig(TypedDict):
    font_size:     int
    line_height:   int
    y_text_start:  int
    x_with_sprite: int
    x_no_sprite:   int
    character_width: int
    initial_asterisk_offset: int
    character_extra_offset: int
    space_extra_offset: int