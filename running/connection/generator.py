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
    pass

def init():
    pass