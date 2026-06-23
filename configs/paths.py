import sys
from pathlib import Path

def is_frozen():
    return getattr(sys, "frozen", False) or hasattr(sys, "_MEIPASS")

if is_frozen():
    BASE_DIR = Path(sys.executable).parent
else:
    BASE_DIR = Path(__file__).resolve().parent.parent

RUNTIME_DIR = Path(sys.executable).parent if is_frozen() else BASE_DIR
TEMP_DATA_DIR = RUNTIME_DIR / "data"
TEMP_DATA_DIR.mkdir(parents=True, exist_ok=True)

ASSETS_DIR = BASE_DIR / "assets"
STARTUP_DIR = BASE_DIR / "startup"
FONTS = BASE_DIR / "fonts"
CONFIGS_DIR = BASE_DIR / "configs"
UI_DIR = BASE_DIR / "ui"

ICONS_DIR = UI_DIR / "icons"
ICON_LEFT = ICONS_DIR / "arrow-left.png"
ICON_RIGHT = ICONS_DIR / "primary-line-line-arrow-end.png"
ICON_EDIT = ICONS_DIR / "mono-editor.png"
ICON_DELETE = ICONS_DIR / "trash_correct_resolution.png"

ICON_APP_DIR = ICONS_DIR / "app"

LOGO_ICON = ICON_APP_DIR / (
    "logo.ico" if sys.platform == "win32"
    else "logo.icns" if sys.platform == "darwin"
    else "logo.png"
)

IN_MEMORY_DIR = STARTUP_DIR / "in_memory"
STATIC_DB = IN_MEMORY_DIR / "static_data.sqlite3"
DYNAMIC_DB = TEMP_DATA_DIR / "temp_data.sqlite3"

BORDERS_DIR = ASSETS_DIR / "borders"
PREVIEWS_DIR = ASSETS_DIR / "previews"

UNDERTALE_PREVIEW = PREVIEWS_DIR / "undertale_preview.png"
TITLE = ASSETS_DIR / "title_transparent.png"

DYNAMIC_SCHEMA = ASSETS_DIR / "temp_dynamic_data" / "schema.sql"

GEN_CONFIG = CONFIGS_DIR / "gen-config.toml"
