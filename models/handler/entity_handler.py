from abc import ABC, abstractmethod
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QGroupBox
from services import grid_service
from services.database_service import DBDynamicConnection
from services.tile_service import insert_tile, TileConfig

class EntityHandler(ABC):

    def __init__(self, ui):
        self.ui = ui

    # shared logic

    def handle_move(self, entity, direction: int):
        new_pos = entity.order_position + direction
        other = self.db_select_by_order(new_pos)
        if not other:
            return
        self.db_update_order(entity, new_pos)
        self.db_update_order(other, entity.order_position)

        if self.filter_text():
            self.reload_filtered()
        else:
            grid_service.swap_tiles(self.grid_widget(), entity.get_id(), other.get_id())

    def handle_delete(self, entity, tile: QGroupBox):
        reply = QMessageBox.warning(
            None, "Warning!", self.delete_message(entity),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Cancel:
            return

        was_selected = self.grid_widget().property("selected_id") == entity.get_id()
        self.on_before_delete(entity)
        self.db_delete(entity)
        tile.hide()
        tile.deleteLater()

        if was_selected:
            self.grid_widget().setProperty("selected_tile", None)
            self.grid_widget().setProperty("selected_id", None)
            QTimer.singleShot(0, self.select_first_or_none)

        QTimer.singleShot(0, self.grid_widget().reflow_filter.reflow)

    def handle_select(self, entity, tile: QGroupBox):
        previous = self.grid_widget().property("selected_tile")
        if previous:
            previous.setStyleSheet("")
        self.update_selection_manager(entity)
        tile.setStyleSheet("QGroupBox { border: 1px solid orange; }")
        self.grid_widget().setProperty("selected_tile", tile)
        self.grid_widget().setProperty("selected_id", entity.get_id())

    def select_first_or_none(self):
        layout = self.grid_widget().layout()
        if layout is None or layout.count() == 0:
            self.clear_selection_manager()
            self.grid_widget().setProperty("selected_tile", None)
            self.grid_widget().setProperty("selected_id", None)
            return
        first = layout.itemAt(0).widget()
        if first:
            self.handle_select(first.property("entity"), first)

    def insert_entity_tile(self, entity):
        tile = insert_tile(self.grid_widget(), entity, TileConfig())
        config = TileConfig(
            on_move   = lambda d: self.handle_move(entity, d),
            on_edit   = lambda: self.handle_edit(entity),
            on_select = lambda: self.handle_select(entity, tile),
            on_delete = lambda: self.handle_delete(entity, tile),
        )
        tile.set_config(config)

    # abstract methods

    @abstractmethod
    def grid_widget(self): ...

    @abstractmethod
    def db_delete(self, entity): ...

    @abstractmethod
    def db_select_by_order(self, pos: int): ...

    @abstractmethod
    def db_update_order(self, entity, new_pos: int): ...

    @abstractmethod
    def handle_edit(self, entity): ...

    @abstractmethod
    def delete_message(self, entity) -> str: ...

    @abstractmethod
    def update_selection_manager(self, entity): ...

    @abstractmethod
    def clear_selection_manager(self): ...

    @abstractmethod
    def filter_text(self) -> str: ...

    @abstractmethod
    def reload_filtered(self): ...

    def on_before_delete(self, entity):
        pass  # Override für Cascade

    def get_db(self):
        return DBDynamicConnection.get_instance()