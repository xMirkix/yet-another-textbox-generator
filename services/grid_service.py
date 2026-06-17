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
    if not tile_a or not tile_b:
        return

    layout.removeWidget(tile_a)
    layout.removeWidget(tile_b)

    entity_a = tile_a.property("entity")
    entity_b = tile_b.property("entity")

    entity_a.order_position, entity_b.order_position = entity_b.order_position, entity_a.order_position

    layout.addWidget(tile_a, pos_b[0], pos_b[1])
    layout.addWidget(tile_b, pos_a[0], pos_a[1])

def clear_tile_selection(grid_widget):
    layout = grid_widget.layout()
    if layout is None:
        return
    for i in range(layout.count()):
        item = layout.itemAt(i)
        w = item.widget()
        if w:
            w.setStyleSheet("")

def restore_selection(grid_widget, entity_id: int | None) -> bool:
    if entity_id is None:
        return False
    tile, _ = find_tile(grid_widget.layout(), entity_id)
    if tile:
        clear_tile_selection(grid_widget)
        tile.setStyleSheet("QGroupBox { border: 1px solid orange; }")
        return True
    return False

def clear_grid(widget):
    layout = widget.layout()
    if layout is None:
        return
    while layout.count():
        item = layout.takeAt(0)
        w = item.widget()
        if w:
            w.hide()
            w.deleteLater()