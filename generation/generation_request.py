from dataclasses import dataclass

from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from startup.in_memory.static_classes import Color


@dataclass
class GenerationRequest:
    text_input: str
    default_color: Color
    border_settings: BorderSettings
    sprite_settings: SpriteSettings
    right_sprite_settings: SpriteSettings
    font_settings: FontSettings
    export_settings: ExportSettings

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, GenerationRequest):
            return NotImplemented
        return (
                self.text_input == other.text_input and
                self.default_color == other.default_color and
                self.border_settings == other.border_settings and
                self.sprite_settings == other.sprite_settings and
                self.right_sprite_settings == other.right_sprite_settings and
                self.font_settings == other.font_settings and
                self.export_settings == other.export_settings
        )

    def __hash__(self) -> int:
        return hash((
            self.text_input,
            self.default_color,
            self.border_settings,
            self.sprite_settings,
            self.right_sprite_settings,
            self.font_settings,
            self.export_settings,
        ))