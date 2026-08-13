import os
import sys
from pathlib import Path
import json

from PySide6.QtWidgets import QListWidgetItem

from ui.generated_ui import Ui_MainWindow


def get_data_path(app_name: str) -> Path:
    if sys.platform == "win32":
        base = os.environ.get("APPDATA", str(Path.home() / "AppData" / "Roaming"))
        return Path(base) / app_name / "last_opened.json"

    elif sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / app_name / "last_opened.json"

    else:
        base = os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local" / "share"))
        return Path(base) / app_name / "last_opened.json"


def reset_ui_list(ui: Ui_MainWindow):
    ui.last_opened_list.clear()
    last_opened: list[str] = last_opened_manager.get_list()

    if len(last_opened) == 0:
        return

    for path in last_opened:
        item = QListWidgetItem(path)
        item.setToolTip(path)
        ui.last_opened_list.addItem(item)

class LastOpenedManger:

    MAX_ITEMS = 10

    def __init__(self, app_name: str = "YATG"):
        self.list: list[str] = []
        self.file_path = get_data_path(app_name)
        self.load()

    def load(self):
        if self.file_path.exists():
            try:
                data = json.loads(self.file_path.read_text(encoding="utf-8"))
                if isinstance(data, list):
                    self.list = [str(x) for x in data]
            except (json.JSONDecodeError, OSError):
                self.list = []

    def save(self):
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self.file_path.write_text(
            json.dumps(self.list, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def add_item(self, item: str):
        if item in self.list:
            self.list.remove(item)
        self.list.insert(0, item)
        self.list = self.list[: self.MAX_ITEMS]
        self.save()

    def get_list(self) -> list[str]:
        return self.list


last_opened_manager = LastOpenedManger()


