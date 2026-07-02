from dataclasses import dataclass
from PIL import Image

@dataclass
class GenerationContext:
    image: Image.Image
    has_expression: bool = False
    has_right_expression: bool = False
    border_style: str = "Original"