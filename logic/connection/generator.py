from ui.generated_ui import Ui_MainWindow
from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings


class Wrapper:

    border_settings: BorderSettings
    sprite_settings: SpriteSettings
    font_settings: FontSettings
    export_settings: ExportSettings


    def __init__(self, input_prompt: str, border_settings: BorderSettings, sprite_settings: SpriteSettings, font_settings: FontSettings, export_settings: ExportSettings):
        self.input_prompt = input_prompt
        self.border_settings = border_settings
        self.sprite_settings = sprite_settings
        self.font_settings = font_settings
        self.export_settings = export_settings


def connect_generator(ui: Ui_MainWindow):
    form = Wrapper(
        input_prompt="",
        border_settings=BorderSettings(1, 1), #UT, White
        sprite_settings=SpriteSettings(-1, -1, -1, 1), # Nothing set, only color
        font_settings=FontSettings(1, True, [1,1,1], "Regular", 1), # Has asterisk, white colors and Regular with no transform
        export_settings=ExportSettings("PNG", True, "Medium") # PNG with medium size and margin
    )
    pass
