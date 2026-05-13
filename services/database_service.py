import sqlite3
from configs.paths import DYNAMIC_DB, DYNAMIC_SCHEMA, STATIC_DB

from models.entities import Character, Universe, Expression
from services.change_service import Changes
from startup.in_memory.static_classes import Color, BorderStyle, TextFont, TextTransform


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

    def select_all_colors(self) -> list[Color]:
        rows = self.connection.execute("SELECT * FROM Colors").fetchall()
        return [Color(*row) for row in rows]

    def select_all_border_styles(self) -> list[BorderStyle]:
        rows = self.connection.execute("SELECT * FROM BorderStyles").fetchall()
        return [BorderStyle(*row) for row in rows]

    def select_all_text_fonts(self) -> list[TextFont]:
        rows = self.connection.execute("SELECT * FROM Fonts").fetchall()
        return [TextFont(*row) for row in rows]

    def select_all_text_transforms(self) -> list[TextTransform]:
        rows = self.connection.execute("SELECT * FROM Transforms").fetchall()
        return [TextTransform(*row) for row in rows]

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



    # SELECTS

    def select_table(self, table_name: str):
        return self.connection.execute(f"""
            SELECT * FROM {table_name}
        """).fetchall()

    def select_all_universes(self) -> list[Universe]:
        rows = self.connection.execute("SELECT * FROM Universes ORDER BY order_position").fetchall()
        return [Universe(*row) for row in rows]

    def select_universe_by_order_position(self, order_position: int) -> Universe | None:
        rows = self.connection.execute(
            "SELECT * FROM Universes WHERE order_position = ?", (order_position,)
        ).fetchone()
        if rows is None:
            return None
        return Universe(*rows)

    def select_filtered_universes(self, name) -> list[Universe]:
        rows = self.connection.execute(
            "SELECT * FROM Universes WHERE universe_name LIKE ? ORDER BY order_position", (f"%{name}%",)
        ).fetchall()
        return [Universe(*row) for row in rows]

    def count_universes(self) -> int:
        return self.connection.execute("SELECT COUNT(*) FROM Universes").fetchone()[0]

    def select_all_characters_from_universe(self, universe_id: int) -> list[Character]:
        rows = self.connection.execute(
            "SELECT * FROM Characters WHERE universe_id = ? ORDER BY order_position", (universe_id,)
        ).fetchall()
        return [Character(*row) for row in rows]

    def select_character_by_order_position(self, universe_id: int, order_position: int) -> Character | None:
        rows = self.connection.execute(
            "SELECT * FROM Characters WHERE universe_id = ? AND order_position = ?", (universe_id, order_position)
        ).fetchone()
        if rows is None:
            return None
        return Character(*rows)

    def select_filtered_characters(self, universe_id: int, name) -> list[Character]:
        rows = self.connection.execute(
            "SELECT * FROM Characters WHERE universe_id = ? AND character_name LIKE ? ORDER BY order_position",
            (universe_id, f"%{name}%")
        ).fetchall()
        return [Character(*row) for row in rows]

    def count_characters(self, universe_id: int) -> int:
        return self.connection.execute(
            "SELECT COUNT(*) FROM Characters WHERE universe_id = ?", (universe_id,)
        ).fetchone()[0]

    def select_all_expressions_from_character(self, character_id: int) -> list[Expression]:
        rows = self.connection.execute(
            "SELECT * FROM Expressions WHERE character_id = ? ORDER BY order_position",
            (character_id,)
        ).fetchall()
        return [Expression(*row) for row in rows]

    def select_expression_by_order_position(self, character_id: int, order_position: int) -> Expression | None:
        rows = self.connection.execute(
            "SELECT * FROM Expressions WHERE character_id = ? AND order_position = ?",
            (character_id, order_position)
        ).fetchone()
        if rows is None:
            return None
        return Expression(*rows)

    def select_filtered_expressions(self, character_id: int, name) -> list[Expression]:
        rows = self.connection.execute(
            "SELECT * FROM Expressions WHERE character_id = ? AND expression_name LIKE ? ORDER BY order_position",
            (character_id, f"%{name}%")
        ).fetchall()
        return [Expression(*row) for row in rows]

    def count_expressions(self, character_id: int) -> int:
        return self.connection.execute(
            "SELECT COUNT(*) FROM Expressions WHERE character_id = ?", (character_id,)
        ).fetchone()[0]

    # INSERTS


    def insert_universe(self, universe: Universe):
        self.connection.execute(
            "INSERT INTO Universes (universe_name, preview_image, order_position) VALUES (?, ?, ?)",
            (universe.universe_name, universe.preview_image, universe.order_position)
        )
        self.connection.commit()
        Changes.change()

    def insert_character(self, character: Character):
        self.connection.execute(
            "INSERT INTO Characters (character_name, universe_id, default_style, default_font, default_text_transform, preview_image, order_position) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (character.character_name, character.universe_id, character.default_style, character.default_font,
             character.default_text_transform, character.preview_image, character.order_position)
        )
        self.connection.commit()
        Changes.change()

    def insert_expression(self, expression: Expression):
        self.connection.execute(
            "INSERT INTO Expressions (expression_name, character_id, preview_image, order_position) VALUES (?, ?, ?, ?)",
            (expression.expression_name, expression.character_id, expression.preview_image, expression.order_position)
        )
        self.connection.commit()
        Changes.change()

    # UPDATES


    def update_universe(self, universe):
        self.connection.execute(
            "UPDATE Universes SET universe_name = ?, preview_image = ? WHERE universe_id = ?",
            (universe.universe_name, universe.preview_image, universe.universe_id)
        )
        self.connection.commit()
        Changes.change()

    def update_character(self, character):
        self.connection.execute(
            "UPDATE Characters SET character_name = ?, universe_id = ?, default_style = ?, default_font = ?, default_text_transform = ?, preview_image = ? WHERE character_id = ?",
            (character.character_name, character.universe_id, character.default_style, character.default_font,
             character.default_text_transform, character.preview_image, character.character_id)
        )
        self.connection.commit()
        Changes.change()

    def update_universe_order_position(self, universe_id: int, order_position: int):
        self.connection.execute(
            "UPDATE Universes SET order_position = ? WHERE universe_id = ?",
            (order_position, universe_id)
        )
        self.connection.commit()
        Changes.change()

    def update_character_order_position(self, character_id: int, order_position: int):
        self.connection.execute(
            "UPDATE Characters SET order_position = ? WHERE character_id = ?",
            (order_position, character_id)
        )
        self.connection.commit()
        Changes.change()

    def update_expression(self, expression):
        self.connection.execute(
            "UPDATE Expressions SET expression_name = ?, character_id = ?, preview_image = ? WHERE expression_id = ?",
            (expression.expression_name, expression.character_id, expression.preview_image, expression.expression_id)
        )
        self.connection.commit()
        Changes.change()

    def update_expression_order_position(self, expression_id: int, order_position: int):
        self.connection.execute(
            "UPDATE Expressions SET order_position = ? WHERE expression_id = ?",
            (order_position, expression_id)
        )

    # DELETES


    def delete_universe(self, universe_id, order_position: int):
        self.connection.execute(
            "UPDATE Universes SET order_position = order_position - 1 WHERE order_position > ?", (order_position,)
        )
        self.connection.execute(
            "DELETE FROM Universes WHERE universe_id = ?", (universe_id,)
        )
        self.connection.commit()
        Changes.change()

    def delete_character(self, character_id, universe_id: int, order_position: int):
        self.connection.execute(
            "UPDATE Characters SET order_position = order_position - 1 WHERE order_position > ? AND universe_id = ?", (order_position, universe_id)
        )
        self.connection.execute(
            "DELETE FROM Characters WHERE character_id = ?", (character_id,)
        )
        self.connection.commit()
        Changes.change()

    def delete_expression(self, expression_id, character_id: int, order_position: int):
        self.connection.execute(
            "UPDATE Expressions SET order_position = order_position - 1 WHERE order_position > ? AND character_id = ?", (order_position, character_id)
        )
        self.connection.execute(
            "DELETE FROM Expressions WHERE expression_id = ?", (expression_id,)
        )
        self.connection.commit()
        Changes.change()

    def delete_all_tables(self):
        self.connection.execute("DELETE FROM Universes")
        self.connection.execute("DELETE FROM Characters")
        self.connection.execute("DELETE FROM Expressions")
        self.connection.commit()


