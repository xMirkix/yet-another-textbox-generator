class Universe:
    universe_id: int
    universe_name: str
    preview_image: str | None #base64
    order_position: int

    def __init__(self, universe_id: int, universe_name: str, preview_image: str, order_position: int):
        self.universe_id = universe_id
        self.preview_image = preview_image
        if universe_name is not None:
            self.universe_name = universe_name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
            raise ValueError('Order position must be provided and not negative')

class Character:
    character_id: int
    character_name: str
    universe_id: int
    default_style: int
    default_text_transform: int
    preview_image: str | None
    order_position: int

    def __init__(self, character_id: int, character_name: str, universe_id: int, default_style: int, default_text_transform: int, preview_image: str, order_position: int):
        self.character_id = character_id
        self.universe_id = universe_id
        self.default_style = default_style
        self.default_text_transform = default_text_transform
        self.preview_image = preview_image
        if character_name is not None:
            self.character_name = character_name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
            raise ValueError('Order position must be provided and not negative')

class Expression:
    expression_id: int
    expression_name: str
    universe_id: int
    character_id: int
    image: str
    order_position: int

    def __init__(self, expression_id: int, expression_name: str, universe_id: int, character_id: int, image: str, order_position: int):
        self.expression_id = expression_id
        self.universe_id = universe_id
        self.character_id = character_id
        if image is not None:
            self.image = image
        else:
            raise ValueError('Image must be provided')
        if expression_name is not None:
            self.expression_name = expression_name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
                raise ValueError('Order position must be provided and not negative')