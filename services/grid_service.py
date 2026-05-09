def find_tile(layout, entity_id: int):
    for i in range(layout.count()):
        item = layout.itemAt(i)
        w = item.widget()
        if w and w.property("entity_id") == entity_id:
            row, col, _, _ = layout.getItemPosition(i)
            return w, (row, col)
    return None, None

def swap_tiles(grid_widget, id_a: int, id_b: int):
    layout = grid_widget.layout()
    tile_a, pos_a = find_tile(layout, id_a)
    tile_b, pos_b = find_tile(layout, id_b)
    if tile_a is None or tile_b is None:
        return
    entity_a = tile_a.property("entity")
    entity_b = tile_b.property("entity")
    entity_a.order_position, entity_b.order_position = entity_b.order_position, entity_a.order_position
    layout.addWidget(tile_a, pos_b[0], pos_b[1])
    layout.addWidget(tile_b, pos_a[0], pos_a[1])

def clear_grid(widget):
    widget.setProperty("selected_tile", None)
    layout = widget.layout()
    if layout is None:
        return
    while layout.count():
        item = layout.takeAt(0)
        w = item.widget()
        if w:
            w.deleteLater()

def restore_selection(grid_widget) -> bool:
    selected_id = grid_widget.property("selected_id")
    if selected_id is None:
        return False
    tile, _ = find_tile(grid_widget.layout(), selected_id)
    if tile:
        tile.setStyleSheet("QGroupBox { border: 1px solid orange; }")
        grid_widget.setProperty("selected_tile", tile)
        return True
    return False