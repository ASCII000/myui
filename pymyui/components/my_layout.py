from typing import TypeVar, Generic

from typing import Literal, Optional
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import QEvent

from .my_notify import MyNotify


T = TypeVar("T")

class MyLayout:
    """
    Abstração simples para layouts verticais ou horizontais.
    """

    def __init__(self, position: str = "vertical"):
        if position == "horizontal":
            self.layout = QtWidgets.QHBoxLayout()
        elif position == "vertical":
            self.layout = QtWidgets.QVBoxLayout()
        else:
            raise ValueError("Posição inválida. Use 'horizontal' ou 'vertical'.")

    def get_layout(self):
        return self.layout

    def add_widget(self, widget: T, stretch: int = 0, alignment: Optional[Literal["left", "center", "right"]] = None) -> T:
        if alignment == "left":
            self.layout.addWidget(widget, stretch, QtCore.Qt.AlignmentFlag.AlignLeft)
        elif alignment == "center":
            self.layout.addWidget(widget, stretch, QtCore.Qt.AlignmentFlag.AlignCenter)
        elif alignment == "right":
            self.layout.addWidget(widget, stretch, QtCore.Qt.AlignmentFlag.AlignRight)
        else:
            self.layout.addWidget(widget, stretch)

        return widget

    def add_layout(self, other_layout):
        self.layout.addLayout(other_layout)

    def add_stretch(self):
        self.layout.addStretch()

    def setContentsMargins(self, left: int, top: int, right: int, bottom: int):
        self.layout.setContentsMargins(left, top, right, bottom)


class MyWindow(QtWidgets.QWidget):
    """
    Janela customizada com método intuitivo de criação de layout.
    """

    def __init__(self, title: str = "Minha Janela", width: int = 400, height: int = 300):
        self.middlewares_events = []
        super().__init__()
        self.setWindowTitle(title)
        self.setFixedSize(width, height)

    def create_layout(self, position: Literal["horizontal", "vertical"] = "vertical") -> MyLayout:
        return MyLayout(position)

    def add_event_middleware(self, event: QEvent.Type, callback):
        self.middlewares_events.append((event, callback))

    def changeEvent(self, event: QEvent):
        for event_name, callback in self.middlewares_events:
            if event.type() == event_name:
                callback(event)

        return super().changeEvent(event)

    def notify(
        self,
        text: str,
        duration: int = 3000,
        width: int = 300,
        height: int = 60,
        corner: Literal[
            "top-left",
            "top-right",
            "bottom-left",
            "bottom-right",
        ] = "bottom-right",
        text_color: str = "#ffffff",
        background_color: str = "#323232",
    ):
        """
        Cria uma notificação overlay dentro da janela principal.
        """
        # Cria a notificação passando self como parent
        notify = MyNotify(
            self,
            text,
            duration,
            width,
            height,
            corner,
            text_color,
            background_color,
        )
        
        # Armazena referência para evitar garbage collection
        if not hasattr(self, '_notifications'):
            self._notifications = []
        self._notifications.append(notify)
        
        # Remove da lista quando fechada
        def cleanup():
            if notify in self._notifications:
                self._notifications.remove(notify)
        
        notify.destroyed.connect(cleanup)
