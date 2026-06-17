from abc import ABC, abstractmethod
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox, QGroupBox
from services import grid_service
from services.database_service import DBDynamicConnection
from services.tile_service import insert_tile, TileConfig
from ui.generated_ui import Ui_MainWindow


class EntityHandler(ABC):

    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui

    # shared logic

    def handle_move(self, entity, direction: int):
        new_pos = entity.order_position + direction
        other = self.db_select_by_order(entity, new_pos)
        if not other:
            return
        self.db_update_order(entity, new_pos)
        self.db_update_order(other, entity.order_position)

        if self.filter_text():
            QTimer.singleShot(0, self.reload_filtered)
        else:
            grid_service.swap_tiles(self.grid_widget(), entity.get_id(), other.get_id())

    def handle_delete(self, entity, tile: QGroupBox):
        reply = QMessageBox.warning(
            None, "Warning!", self.delete_message(entity),
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel
        )
        if reply == QMessageBox.StandardButton.Cancel:
            return
        selected = self.get_selected_entity()
        was_selected = selected is not None and selected.get_id() == entity.get_id()
        self.on_before_delete(entity)
        self.db_delete(entity)
        tile.hide()
        tile.deleteLater()
        if was_selected:
            self.clear_selection_manager()
            QTimer.singleShot(0, self.select_first_or_none)
        QTimer.singleShot(0, self.grid_widget().reflow_filter.reflow)

    def handle_select(self, entity, tile: QGroupBox):
        grid_service.clear_tile_selection(self.grid_widget())
        self.update_selection_manager(entity)
        tile.setStyleSheet("QGroupBox { border: 1px solid orange; }")

    def select_first_or_none(self):
        layout = self.grid_widget().layout()
        if layout is None or layout.count() == 0:
            self.clear_selection_manager()
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
    def db_select_by_order(self, entity, new_pos: int): ...

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

    @abstractmethod
    def get_selected_entity(self): ...

    @abstractmethod
    def on_before_delete(self, entity): ... # Override für Cascade

    def get_db(self):
        return DBDynamicConnection.get_instance()