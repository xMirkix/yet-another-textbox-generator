from models.entities import Universe, Character, Expression


class SelectionManager:
    selected_universe: Universe | None = None
    selected_character: Character | None = None
    selected_expression: Expression | None = None

    @classmethod
    def reset(cls):
        cls.selected_universe = None
        cls.selected_character = None
        cls.selected_expression = None

    @classmethod
    def set_selected_universe(cls, universe: Universe | None):
        cls.selected_universe = universe

    @classmethod
    def set_selected_character(cls, character: Character | None):
        cls.selected_character = character

    @classmethod
    def set_selected_expression(cls, expression: Expression | None):
        cls.selected_expression = expression

    @classmethod
    def get_selected_universe(cls) -> Universe | None:
        return cls.selected_universe

    @classmethod
    def get_selected_character(cls) -> Character | None:
        return cls.selected_character

    @classmethod
    def get_selected_expression(cls) -> Expression | None:
        return cls.selected_expression