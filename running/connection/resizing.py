from PySide6.QtCore import QObject, QEvent

class GridReflowFilter(QObject):
    def __init__(self, grid_widget, tile_width: int = 250, spacing: int = 10):
        super().__init__(grid_widget)
        self.grid_widget = grid_widget
        self.tile_width = tile_width
        self.spacing = spacing
        grid_widget.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.Resize:
            self._reflow()
        return super().eventFilter(obj, event)

    def _reflow(self):
        layout = self.grid_widget.layout()
        if layout is None:
            return

        available_width = self.grid_widget.width()
        cols = max(1, available_width // (self.tile_width + self.spacing))
        
        items = []
        for i in range(layout.count()):
            item = layout.itemAt(i)
            w = item.widget()
            if w and not w.isHidden():
                row, col, _, _ = layout.getItemPosition(i)
                items.append((row, col, w))

        items.sort(key=lambda x: (x[0], x[1]))
        widgets = [w for _, _, w in items]

        while layout.count():
            layout.takeAt(0)

        # In korrekter Reihenfolge neu einfügen
        for i, w in enumerate(widgets):
            layout.addWidget(w, i // cols, i % cols)

    def reflow(self):
        self._reflow()