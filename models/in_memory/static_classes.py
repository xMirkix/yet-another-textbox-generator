class BorderStyle:
    border_id: int
    border_name: str
    image: str #base64
    order_position: int

    def __init__(self, border_id: int, border_name: str, order_position: int, image: str):
        self.border_id = border_id
        if border_name is not None:
            self.border_name = border_name
        else:
            raise ValueError('Name must be provided')
        if order_position is not None and order_position > 0:
            self.order_position = order_position
        else:
            raise ValueError('Order position must be provided and not negative')
        self.image = image

class Color:
    color_id: int
    color_name: str
    r: int
    g: int
    b: int

    def __init__(self, color_id: int, color_name: str, r: int, g: int, b: int):
        self.color_id = color_id
        self.color_name = color_name
        self.r = r
        self.g = g
        self.b = b

class TextFont:
    font_id: int
    font_name: str
    font_value: str

    def __init__(self, font_id: int, font_name: str, font_value: str):
        self.font_id = font_id
        if font_name is not None:
            self.font_name = font_name
        else:
            raise ValueError('Name must be provided')
        if font_value is not None:
            self.font_value = font_value
        else:
            raise ValueError('Value must be provided')

class TextTransform:
    transform_id: int
    transform_name: str
    transform: str

    def __init__(self, transform_id: int, transform_name: str):
        self.transform_id = transform_id
        if transform_name is not None:
            self.transform_name = transform_name
        else:
            raise ValueError('Name must be provided')