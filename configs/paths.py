import atexit
import shutil
import sys
import tempfile
import time
from pathlib import Path

_BUNDLE = Path(__file__).resolve().parent.parent

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
ICON_LEFT = ICONS_DIR / 'left.png'
ICON_RIGHT = ICONS_DIR / 'right.png'
ICON_EDIT = ICONS_DIR / 'edit.png'
ICON_DELETE = ICONS_DIR / 'trash.png'
ICON_UP = ICONS_DIR / 'up.png'
ICON_DOWN = ICONS_DIR / 'down.png'
ICON_EYE = ICONS_DIR / 'preview.png'

ICON_APP_DIR = ICONS_DIR / 'app'
LOGO_ICON = ICON_APP_DIR / (
    "logo.ico" if sys.platform == "win32"
    else "logo.icns" if sys.platform == "darwin"
    else "logo.png"
)

FONTS = _BUNDLE / 'fonts'
GEN_CONFIG = _BUNDLE / 'configs' / 'gen-config.toml'

def _make_temp_data_dir() -> Path:
    root = Path(tempfile.gettempdir())
    for old in root.glob("yatg_*"):
        try:
            if time.time() - old.stat().st_mtime > 86400:
                shutil.rmtree(old, ignore_errors=True)
        except OSError:
            pass
    d = Path(tempfile.mkdtemp(prefix="yatg_"))

    def _cleanup() -> None:
        shutil.rmtree(d, ignore_errors=True)

    atexit.register(_cleanup)
    return d


TEMP_DATA_DIR = _make_temp_data_dir()
DYNAMIC_DB = TEMP_DATA_DIR / 'temp_data.sqlite3'