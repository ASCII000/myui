"""
Modulo que contem o componente de notificação padronizado no projeto.
"""

import textwrap

from PySide6 import QtWidgets, QtCore


class MyNotify(QtWidgets.QWidget):
    """
    Notificação overlay que aparece dentro da janela principal.
    """
    _current_notification = None

    def __init__(
        self,
        parent: QtWidgets.QWidget,
        text: str = "Notificação",
        duration: int = 3000,  # em milissegundos
        width: int | None = 250,
        height: int = 60,
        corner: str = "bottom-right",
        text_color: str = "#ffffff",
        background_color: str = "#323232",
        font_family: str = "Segoe UI",
    ):

        self.fade_out_animation = None
        super().__init__(parent)

        if MyNotify._current_notification:
            MyNotify._current_notification.close()
        else:
            MyNotify._current_notification = self

        text = "\n".join(textwrap.wrap(text, width=50))

        self.parent_widget = parent
        self.corner = corner
        self.setFixedSize(width, height)

        # Remove as flags de janela - agora é um widget filho
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        # Estilo da notificação com sombra
        self.label = QtWidgets.QLabel(text, self)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet(
            f"""
            QLabel {{
                background-color: {background_color};
                color: {text_color};
                padding: 12px;
                font-size: 14px;
                font-weight: normal;
                font-family: {font_family};
                border-radius: 8px;
            }}
            """
        )

        self.label.setGeometry(0, 0, width, height)

        # Posiciona dentro da janela pai
        self._position_widget(corner)

        # Timer para fechar automaticamente
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self._fade_out)
        self.timer.setSingleShot(True)
        self.timer.start(duration)

        # Animação de fade in
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity_effect)

        self.fade_in_animation = QtCore.QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_in_animation.setDuration(300)
        self.fade_in_animation.setStartValue(0.0)
        self.fade_in_animation.setEndValue(1.0)
        self.fade_in_animation.start()

        # Conecta o redimensionamento da janela pai para reposicionar
        if hasattr(parent, 'resizeEvent'):
            self.original_resize_event = parent.resizeEvent
            parent.resizeEvent = self._on_parent_resize

        # Mostra a notificação
        self.show()
        self.raise_()

    def _position_widget(self, corner):
        """Posiciona a notificação dentro da janela pai"""
        if not self.parent_widget:
            return

        parent_rect = self.parent_widget.rect()
        margin = 20

        if corner == "top-left":
            x = margin
            y = margin
        elif corner == "top-right":
            x = parent_rect.width() - self.width() - margin
            y = margin
        elif corner == "bottom-left":
            x = margin
            y = parent_rect.height() - self.height() - margin
        elif corner == "bottom-right":
            x = parent_rect.width() - self.width() - margin
            y = parent_rect.height() - self.height() - margin
        else:
            # Default para bottom-right
            x = parent_rect.width() - self.width() - margin
            y = parent_rect.height() - self.height() - margin

        self.move(x, y)

    def _on_parent_resize(self, event):
        """Reposiciona a notificação quando a janela pai é redimensionada"""
        if hasattr(self, 'original_resize_event'):
            self.original_resize_event(event)
        
        # Reposiciona a notificação
        if hasattr(self, 'corner'):
            self._position_widget(self.corner)

    def _fade_out(self):
        """Animação de fade out antes de fechar"""
        self.fade_out_animation = QtCore.QPropertyAnimation(self.opacity_effect, b"opacity")
        self.fade_out_animation.setDuration(300)
        self.fade_out_animation.setStartValue(1.0)
        self.fade_out_animation.setEndValue(0.0)
        self.fade_out_animation.finished.connect(self.close)
        self.fade_out_animation.start()

    def closeEvent(self, event):
        if hasattr(self, 'timer'):
            self.timer.stop()

        # Restaura o evento de resize original do pai
        if hasattr(self, 'original_resize_event') and self.parent_widget:
            self.parent_widget.resizeEvent = self.original_resize_event

        if MyNotify._current_notification is self:
            MyNotify._current_notification = None   # ← ADICIONADO

        event.accept()

    def force_close(self):
        """Fecha imediatamente a notificação, sem animação."""
        if hasattr(self, 'timer'):
            self.timer.stop()
        if hasattr(self, 'fade_out_animation'):
            if self.fade_out_animation:
                self.fade_out_animation.stop()
        self.hide()
        self.deleteLater()
        if MyNotify._current_notification is self:
            MyNotify._current_notification = None
