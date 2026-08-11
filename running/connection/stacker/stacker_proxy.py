from collections import OrderedDict
from pathlib import Path

from configs.paths import TEMP_DATA_DIR
from generation.generation_request import GenerationRequest
from running.connection.stacker.stacker_logic import generate_stack_logic


CACHE_SIZE = 8

class StackCache:

    cache: OrderedDict[tuple[int, tuple], Path] = OrderedDict()

    slot: int = 0


    def get_stack_image(self, column_amount: int, requests: list[GenerationRequest], has_deltarune_border) -> Path | None:
        if tuple(requests) in self.cache:
            return self.cache[column_amount, tuple(requests)]

        result = generate_stack_logic(column_amount, requests, has_deltarune_border)

        if result is None:
            return None

        path = TEMP_DATA_DIR / f"stack_{self.slot}.png"
        result.save(path)
        self.slot = (self.slot + 1) % CACHE_SIZE

        self.cache[column_amount, tuple(requests)] = path

        if len(self.cache) > CACHE_SIZE:
            self.cache.popitem(last=False)

        return path


stack_cache = StackCache()


