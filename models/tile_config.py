from dataclasses import dataclass
from typing import Callable

@dataclass
class TileConfig:
    on_move:   Callable[[int], None] = lambda d: None
    on_edit:   Callable[[], None]    = lambda: None
    on_select: Callable[[], None]    = lambda: None
    on_delete: Callable[[], None]    = lambda: None