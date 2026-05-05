from dataclasses import dataclass

@dataclass
class Universe:
    universe_id: int
    universe_name: str
    preview_image: str | None
    order_position: int

    def __post_init__(self):
        if not self.universe_name:
            raise ValueError('Name must be provided')
        if not self.order_position or self.order_position <= 0:
            raise ValueError('Order position must be provided and not negative')

@dataclass
class Character:
    character_id: int
    character_name: str
    universe_id: int
    default_style: int
    default_text_transform: int
    preview_image: str | None
    order_position: int


    def __post_init__(self):
        if self.character_name is None:
            raise ValueError('Name must be provided')

        if self.order_position is None or self.order_position < 0:
            raise ValueError('Order position must be provided and not negative')

@dataclass
class Expression:
    expression_id: int
    expression_name: str
    universe_id: int
    character_id: int
    image: str
    order_position: int

    def __post_init__(self):
        if self.image is None:
            raise ValueError('Image must be provided')

        if self.expression_name is None:
            raise ValueError('Name must be provided')

        if self.order_position is None or self.order_position < 0:
            raise ValueError('Order position must be provided and not negative')