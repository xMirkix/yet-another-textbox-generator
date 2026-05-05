# config/paths.py
from pathlib import Path

ROOT = Path(__file__).parent.parent

ASSETS_DIR         = ROOT / 'assets'
PREVIEWS_DIR       = ASSETS_DIR / 'previews'
TEMP_DATA_DIR      = ASSETS_DIR / 'temp_dynamic_data'
STARTUP_DIR        = ROOT / 'startup'
IN_MEMORY_DIR      = STARTUP_DIR / 'in_memory'

STATIC_DB          = IN_MEMORY_DIR / 'static_data.sqlite3'
DYNAMIC_DB         = TEMP_DATA_DIR / 'temp_data.sqlite3'
DYNAMIC_SCHEMA     = TEMP_DATA_DIR / 'schema.sql'

UNDERTALE_PREVIEW  = PREVIEWS_DIR / 'undertale_preview.png'
WHITE_PREVIEW      = PREVIEWS_DIR / 'white_preview.png'