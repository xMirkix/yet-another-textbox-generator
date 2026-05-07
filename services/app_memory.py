from models.form_bindings import BorderSettings, SpriteSettings, FontSettings, ExportSettings
from ui.generated_ui import Ui_MainWindow


class Memory:
    _instance: Memory | None = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, input_prompt: str,
                 border_settings: BorderSettings,
                 sprite_settings: SpriteSettings,
                 font_settings: FontSettings,
                 export_settings: ExportSettings,
                 ui: Ui_MainWindow):
        self.input_prompt = input_prompt
        self.border_settings = border_settings
        self.sprite_settings = sprite_settings
        self.font_settings = font_settings
        self.export_settings = export_settings
        self.ui = ui

    @classmethod
    def get_instance(cls) -> Memory:
        if cls._instance is None:
            raise RuntimeError("Memory was not initialized.")
        return cls._instance

    # --- Updater (UI → Memory) ---

    def update_input(self):
        self.input_prompt = self.ui.input.toPlainText()
        # TODO add the generation function here to update output

    def update_border_settings(self):
        self.border_settings.update(self.ui, )

    def update_sprite_settings(self):
        self.sprite_settings = SpriteSettings.from_ui(self.ui)

    def update_font_settings(self):
        self.font_settings = FontSettings.from_ui(self.ui)

    def update_export_settings(self):
        self.export_settings = ExportSettings.from_ui(self.ui)

    # --- Getter ---

    def get_input_prompt(self) -> str:
        return self.input_prompt

    def get_border_settings(self) -> BorderSettings:
        return self.border_settings

    def get_sprite_settings(self) -> SpriteSettings:
        return self.sprite_settings

    def get_font_settings(self) -> FontSettings:
        return self.font_settings

    def get_export_settings(self) -> ExportSettings:
        return self.export_settings