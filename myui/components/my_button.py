"""
Modulo que contem o componente de botao padronizado no projeto.
"""

from typing import Literal

from PySide6 import QtWidgets, QtGui


class MyButton(QtWidgets.QPushButton):
    """
    Botão customizado com estilos padronizados.
    
    Variantes:
    - back_button: botão discreto para ações como "Voltar"
    - confirm_button: botão chamativo para ações de confirmação
    """

    def __init__(
        self,
        text: str,
        *,
        variant: Literal["success", "error", "natural"] = "natural",
        width: int | None = None,
        height: int | None = None,
        font_size: int = 10,
        border_radius: int = 2,
        padding: int = 10,
        font_family: str = "Segoe UI",
        background_color: str | None = None,
        text_color: str | None = None,
        hover_color: str | None = None,
    ):
        """
        Args:
            text (str): Texto do botão.
            variant (Literal["success", "error", "natural"], optional): Variante do botão. Defaults to "natural".
            width (int, optional): Largura do botão. Defaults to None.
            height (int, optional): Altura do botão. Defaults to None.
            font_size (int, optional): Tamanho da fonte. Defaults to 10.
            border_radius (int, optional): Raio de borda. Defaults to 2.
            padding (int, optional): Preenchimento interno. Defaults to 10.
            font_family (str, optional): Familia da fonte. Defaults to "Segoe UI".
            background_color (str, optional): Cor de fundo. Defaults to None.
            text_color (str, optional): Cor do texto. Defaults to None.
            hover_color (str, optional): Cor ao passar o mouse. Defaults to None.
        """
        super().__init__(text)
  
        # Define estilo baseado na variante
        match variant:

            case "success":
                self.background = background_color or "#4C9A9A"
                self.color = text_color or "#BABABA"
                self.hover_background = hover_color or "#3A7A7A" 

            case "error":
                self.background = "#7A4C6D"
                self.color = text_color or "#BABABA"
                self.hover_background = hover_color or "#5A3851" 

            case "natural":
                self.background = background_color or "#5A6E7A"
                self.color = text_color or "#BABABA"
                self.hover_background = hover_color or "#485A66"

        # Define fonte
        font = QtGui.QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        self.setFont(font)

        self.border_radius = border_radius
        self.padding = padding

        self._default_style()

        # Define tamanho
        if width is not None:
            self.setFixedWidth(width)
        if height is not None:
            self.setFixedHeight(height)

    def _default_style(self):
        """
        Define o estilo padrão do botão.
        """

        style = f"""
            QPushButton {{
                background-color: {self.background};
                color: {self.color};
                border: 2px solid {self.hover_background};
                border-radius: 8px;
                padding: {self.padding}px;
                font-weight: bold;
            }}

            QPushButton:hover {{
                background-color: {self.color};
                color: {self.background};
            }}
        """
        self.setStyleSheet(style)

    def _pressed_style(self):
        """
        Define o estilo ao pressionar o botão.
        """
        style = f"""
            QPushButton {{
                background-color: {self.background};
                color: {self.color};
                border: 2px solid {self.hover_background};
                border-radius: 8px;
                padding: {self.padding}px;
                font-weight: bold;
                opacity: 0.8;
            }}
        """
        self.setStyleSheet(style)

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Cria efeito visual ao pressionar o botão.
        """
        self._pressed_style()
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent) -> None:
        """
        Restaura o estilo ao soltar o botão.
        """
        self._default_style()
        super().mouseReleaseEvent(event)

    def onClick(self, callback):
        """
        Define uma função de callback para o evento de clique.
        """
        self.clicked.connect(callback)
