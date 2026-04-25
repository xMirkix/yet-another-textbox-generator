import sqlite3
from pathlib import Path


class DBStaticConnection:

    DB_PATH = Path(__file__).parent.parent / 'startup' / 'in_memory' / 'static_data.sqlite3'
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    @classmethod
    def saved(cls):
        cls._changed = False

class DBDynamicConnection:
    _instance: DBDynamicConnection | None = None
    _initialized: bool = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, db_path: Path):
        if self._initialized:
            return

        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self._changed = False
        DBDynamicConnection._initialized = True

    @classmethod
    def get_instance(cls) -> DBDynamicConnection:
        if cls._instance is None:
            raise RuntimeError("DBDynamicConnection was not initialized.")
        return cls._instance

    def saved(self):
        self._changed = False

    def reset(self):
        self._changed = False

    def change(self):
        self._changed = True

    def get_state(self) -> bool:
        return self._changed