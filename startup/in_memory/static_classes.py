class BorderStyle:
    border_id: int
    border_name: str
    preview_file_name: str
    source_image_file_name: str

    def __init__(self, border_id: int, border_name: str,  preview_file_name: str, source_image_file_name: str):
        self.border_id = border_id
        if border_name is not None:
            self.border_name = border_name
        else:
            raise ValueError('Name must be provided')
        if preview_file_name is not None:
            self.preview_file_name = preview_file_name
        else:
            raise ValueError('Image path must be provided')
        if source_image_file_name is not None:
            self.source_image_file_name = source_image_file_name
        else:
            raise ValueError('Source image path must be provided')

    def __str__(self): return self.border_name

class Color:
    color_id: int
    color_name: str
    r: int
    g: int
    b: int
    a: int = 255

    def __init__(self, color_id: int, color_name: str, r: int, g: int, b: int, a: int = 255):
        self.color_id = color_id
        self.color_name = color_name
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self): return self.color_name

    def __eq__(self, other) -> bool:
        if isinstance(other, Color):
            return self.color_id == other.color_id and self.r == other.r and self.g == other.g and self.b == other.b and self.a == other.a
        return False

    def __hash__(self) -> int:
        return hash((self.color_id, self.r, self.g, self.b, self.a))

class TextFont:
    font_id: int
    font_name: str
    source_value: str

    def __init__(self, font_id: int, font_name: str, font_source_value: str):
        self.font_id = font_id
        if font_name is not None and font_source_value is not None :
            self.font_name = font_name
            self.source_value = font_source_value
        else:
            raise ValueError('Name must be provided')

    def __str__(self): return self.font_name

    def __hash__(self) -> int:
        return hash(self.font_id)

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

    def __str__(self): return self.transform_name

    def __hash__(self) -> int:
        return hash(self.transform_id)