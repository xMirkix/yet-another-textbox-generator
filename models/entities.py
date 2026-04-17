class Universe:
    universe_id: int
    name: str
    preview_image: bytes | None
    order_position: int

    def __init__(self, universe_id: int, name: str, preview_image: bytes, order_position: int):
        self.universe_id = universe_id
        self.preview_image = preview_image
        if name is not None:
            self.name = name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
            raise ValueError('Order position must be provided and not negative')

class Character:
    character_id: int
    name: str
    universe_id: int
    default_style: int
    default_text_transform: int
    preview_image: bytes | None
    order_position: int

    def __init__(self, character_id: int, name: str, universe_id: int, default_style: int, default_text_transform: int, preview_image: bytes, order_position: int):
        self.character_id = character_id
        self.universe_id = universe_id
        self.default_style = default_style
        self.default_text_transform = default_text_transform
        self.preview_image = preview_image
        if name is not None:
            self.name = name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
            raise ValueError('Order position must be provided and not negative')

class Expression:
    expression_id: int
    name: str
    universe_id: int
    character_id: int
    image: bytes
    order_position: int

    def __init__(self, expression_id: int, name: str, universe_id: int, character_id: int, image: bytes, order_position: int):
        self.expression_id = expression_id
        self.universe_id = universe_id
        self.character_id = character_id
        if image is not None:
            self.image = image
        else:
            raise ValueError('Image must be provided')
        if name is not None:
            self.name = name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
                raise ValueError('Order position must be provided and not negative')