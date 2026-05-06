import sqlite3
from configs.paths import DYNAMIC_DB, DYNAMIC_SCHEMA, STATIC_DB

from models.entities import Character, Universe, Expression
from static.change_service import Changes


class DBStaticConnection:

    DB_PATH = STATIC_DB
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
    db_path = DYNAMIC_DB

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

    def reconnect(self):
        self.connection.close()
        self.connection = sqlite3.connect(self.db_path)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.cursor = self.connection.cursor()

    def create_all_tables(self):
        sql = DYNAMIC_SCHEMA.read_text(encoding='utf-8')
        return self.connection.executescript(sql)

    def select_table(self, table_name: str):
        return self.connection.execute(f"""
            SELECT * FROM {table_name}
        """).fetchall()

    def select_all_universes(self) -> list[Universe]:
        rows = self.connection.execute("SELECT * FROM Universes").fetchall()
        return [Universe(*row) for row in rows]

    def count_universes(self) -> int:
        return self.connection.execute("SELECT COUNT(*) FROM Universes").fetchone()[0]

    def select_all_characters_from_universe(self, universe_id: int) -> list[Character]:
        rows = self.connection.execute(
            "SELECT * FROM Characters WHERE universe_id = ?", (universe_id,)
        ).fetchall()
        return [Character(*row) for row in rows]

    def select_all_expressions_from_character(self, character_id: int) -> list[Expression]:
        rows = self.connection.execute(
            "SELECT * FROM Expressions WHERE character_id = ?",
            (character_id,)
        ).fetchall()
        return [Expression(*row) for row in rows]

    def insert_universe(self, universe: Universe):
        self.connection.execute(
            "INSERT INTO Universes (universe_name, preview_image, order_position) VALUES (?, ?, ?)",
            (universe.universe_name, universe.preview_image, universe.order_position)
        )
        self.connection.commit()  # <-- das hier
        Changes.change()