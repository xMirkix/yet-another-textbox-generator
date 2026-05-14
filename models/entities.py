from dataclasses import dataclass

@dataclass
class Universe:
    universe_id: int
    universe_name: str
    preview_image: bytes | None
    order_position: int

    def __post_init__(self):
        if not self.universe_name:
            raise ValueError('Name must be provided')
        if not self.order_position or self.order_position <= 0:
            raise ValueError('Order position must be provided and not negative')

    def get_id(self) -> int:
        return self.universe_id

    def get_name(self) -> str:
        return self.universe_name

@dataclass
class Character:
    character_id: int
    character_name: str
    universe_id: int
    default_style: int
    default_font: int
    default_text_transform: int
    preview_image: bytes | None
    order_position: int


    def __post_init__(self):
        if self.character_name is None:
            raise ValueError('Name must be provided')

        if self.order_position is None or self.order_position < 0:
            raise ValueError('Order position must be provided and not negative')

    def get_id(self) -> int:
        return self.character_id

    def get_name(self) -> str:
        return self.character_name

@dataclass
class Expression:
    expression_id: int
    expression_name: str
    universe_id: int
    character_id: int
    preview_image: bytes
    order_position: int

    def __post_init__(self):
        if self.preview_image is None:
            raise ValueError('Image must be provided')

        if self.expression_name is None:
            raise ValueError('Name must be provided')

        if self.order_position is None or self.order_position < 0:
            raise ValueError('Order position must be provided and not negative')

    def get_id(self) -> int:
        return self.expression_id

    def get_name(self) -> str:
        return self.expression_name