from PIL import Image

from generation.generation_request import GenerationRequest
from running.connection.generator.generation_calls import png_proxy


def is_dt_box(r: GenerationRequest) -> bool:
    return r.border_settings.style.border_id == 2


def compute_row_offsets(requests_in_column: list[GenerationRequest], dt_positions: set[int]) -> list[int]:
    offsets = [0] * len(requests_in_column)
    pending = 0
    for i, r in enumerate(requests_in_column):
        is_dt_row = i in dt_positions
        dt_box = is_dt_box(r)

        if is_dt_row and not dt_box:
            pending += 1
            if pending > 2:
                pending = 2
            offsets[i] += 4 * pending
        elif is_dt_row and dt_box:
            if pending > 0:
                offsets[i] += 4
            pending = 0
        elif not is_dt_row and pending > 0:
            offsets[i] += 4
            pending = 0

    return offsets



def do_single_page(requests: list [GenerationRequest], page_deltarune_border: bool, dt_positions: set[int]) -> Image.Image:

    total_width = 295

    if page_deltarune_border:
        total_width = 303

    offsets = compute_row_offsets(requests, dt_positions)

    images: list[tuple[Image.Image, bool]] = [] # True if it's a deltarune border

    total_height = sum(offsets)

    for r in requests:
        if page_deltarune_border:
            total_height += 90
        else:
            total_height += 82

        path = png_proxy.generate(r)
        image = Image.open(path)

        images.append((image, r.border_settings.style.border_id == 2))

    final_image = Image.new("RGBA", (total_width, total_height), (0, 0, 0, 255))

    height = 0

    for (image, dt_border), extra in zip(images, offsets):
        height += extra
        horizontal_offset = 0

        if page_deltarune_border and not dt_border:
            horizontal_offset = 4

        final_image.paste(image, (horizontal_offset, height), image)

        height += image.height

    return final_image


def make_filler_col(expressions_per_column: int, has_deltarune_border: bool) -> Image.Image:
    total_width = 295

    if has_deltarune_border:
        total_width = 303

    total_height = 0

    for _ in range(expressions_per_column):
        if has_deltarune_border:
            total_height += 90
        else:
            total_height += 82

    return Image.new("RGBA", (total_width, total_height), (0, 0, 0, 255))


def chunk_requests_row_major(requests: list[GenerationRequest], column_amount: int) -> list[list[GenerationRequest]]:
    chunks: list[list[GenerationRequest]] = [[] for _ in range(column_amount)]

    for i, r in enumerate(requests):
        chunks[i % column_amount].append(r)

    return chunks


def compute_global_dt_row_positions(requests: list[GenerationRequest], column_amount: int) -> set[int]:
    return {i // column_amount for i, r in enumerate(requests) if is_dt_box(r)}


def generate_stack_logic(column_amount: int, requests: list[GenerationRequest], has_deltarune_border: bool) -> Image.Image | None:

    amount_of_requests = len(requests)

    if amount_of_requests == 0:
        return None

    chunks = chunk_requests_row_major(requests, column_amount)
    dt_positions = compute_global_dt_row_positions(requests, column_amount)
    rows_per_column = max(1, -(-amount_of_requests // column_amount))

    col: list[Image.Image] = []

    for chunk in chunks:
        if chunk:
            col.append(do_single_page(chunk, has_deltarune_border, dt_positions))
        else:
            col.append(make_filler_col(rows_per_column, has_deltarune_border))

    max_height = max(c.height for c in col)

    final_image = Image.new("RGBA", (col[0].width * column_amount, max_height), (0, 0, 0, 255))

    for i, c in enumerate(col):
        final_image.paste(c, (i * c.width, 0), c)

    return final_image
