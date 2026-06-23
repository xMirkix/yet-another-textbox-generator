# config/paths.py
import sys
from pathlib import Path

_BUNDLE = Path(__file__).parent.parent

_RUNTIME = Path(sys.executable).parent

ASSETS_DIR = _BUNDLE / 'assets'
BORDERS_DIR = ASSETS_DIR / 'borders'
PREVIEWS_DIR = ASSETS_DIR / 'previews'
STARTUP_DIR = _BUNDLE / 'startup'
IN_MEMORY_DIR = STARTUP_DIR / 'in_memory'
STATIC_DB = IN_MEMORY_DIR / 'static_data.sqlite3'
DYNAMIC_SCHEMA = ASSETS_DIR / 'temp_dynamic_data' / 'schema.sql'
UNDERTALE_PREVIEW = PREVIEWS_DIR / 'undertale_preview.png'
TITLE = ASSETS_DIR / 'title_transparent.png'
ICONS_DIR = _BUNDLE / 'ui' / 'icons'
ICON_LEFT = ICONS_DIR / 'arrow-left.png'
ICON_RIGHT  = ICONS_DIR / 'primary-line-line-arrow-end.png'
ICON_EDIT = ICONS_DIR / 'mono-editor.png'
ICON_DELETE = ICONS_DIR / 'trash_correct_resolution.png'
FONTS = _BUNDLE / 'fonts'
GEN_CONFIG = _BUNDLE / 'configs' / 'gen-config.toml'
LOGO_ICON = _BUNDLE / 'loco.png'

TEMP_DATA_DIR = _RUNTIME / 'data'
DYNAMIC_DB = TEMP_DATA_DIR / 'temp_data.sqlite3'

TEMP_DATA_DIR.mkdir(parents=True, exist_ok=True)