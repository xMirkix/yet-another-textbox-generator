import sqlite3
from pathlib import Path

from models.entities import Character, Universe, Expression


class DBStaticConnection:

    DB_PATH = Path(__file__).parent.parent / 'startup' / 'in_memory' / 'static_data.sqlite3'
    connection = sqlite3.connect(DB_PATH)
    cursor = connection.cursor()

    @classmethod
    def saved(cls):
        cls._changed = False

    def select_table(self, table_name: str):
        return self.connection.execute(f"""
            SELECT * FROM {table_name}
        """).fetchall()

class DBDynamicConnection:
    _instance: DBDynamicConnection | None = None
    _initialized: bool = False
    BASE_DIR = Path(__file__).parent.parent / 'assets' / 'temp_dynamic_data'
    db_path = BASE_DIR / 'temp_data.sqlite3'

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.connection = sqlite3.connect(self.db_path)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()
        self._changed = False
        DBDynamicConnection._initialized = True

    @classmethod
    def get_instance(cls) -> DBDynamicConnection:
        if cls._instance is None:
            raise RuntimeError("DBDynamicConnection was not initialized.")
        return cls._instance

    def select_table(self, table_name: str):
        return self.connection.execute(f"""
            SELECT * FROM {table_name}
        """).fetchall()

    def select_all_universes(self) -> list[Universe]:
        return self.connection.execute(f"""
                SELECT * FROM Universes
        """).fetchall()

    def select_all_characters_from_universe(self, universe_id: int) -> list[Character]:
        return self.connection.execute(f"""
                SELECT * FROM Characters c WHERE c.universe_id = {universe_id}
                                       """).fetchall()

    def select_all_expressions_from_character(self, universe_id: int, character_id: int) -> list[Expression]:
        return self.connection.execute(f"""
                    SELECT * FROM Expressions e WHERE e.universe_id = {universe_id} AND e.character_id = {character_id}
                                       """).fetchall()

    def create_all_tables(self):
        sql = (self.BASE_DIR / 'schema.sql').read_text(encoding='utf-8')
        return self.connection.executescript(sql)