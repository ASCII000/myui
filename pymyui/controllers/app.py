"""
Módulo que contém a classe de controle da aplicação.

É uma extensão de QApplication, feito para minimizar métodos não usados
e adicionar métodos personalizados para simplicidade.
"""

import sys
from typing import Literal

from PySide6.QtWidgets import QApplication

from pymyui.components import (
    MyWindow,
    MyLayout,
    MyLabel,
    MyButton,
    MyInput
)


class CustomApp(QApplication):
    """
    Classe de controle da aplicação.
    """

    def __init__(self, argv):
        super().__init__(argv)


class MyApp:
    """
    Wrapper da classe de controle da aplicação.
    """

    def __init__(
        self,
        width: int = 800,
        height: int = 600,
        background_color: str = "#ffffff",
        primary_color: str = "#707070",
        secondary_color: str = "#FFFFFF",
        font_family: str = "Segoe UI",
    ):
        """
        Args:
            width (int, optional): Largura da janela. Defaults to 800.
            height (int, optional): Altura da janela. Defaults to 600.
            background_color (str, optional): Cor de fundo. Defaults to "#ffffff".
            primary_color (str, optional): Cor primária. Defaults to "#707070".
            secondary_color (str, optional): Cor secundária. Defaults to "#FFFFFF".
            font_family (str, optional): Família da fonte. Defaults to "Segoe UI".
        """
        self.background_color = background_color
        self.primary_color = primary_color
        self.secondary_color = secondary_color
        self.font_family = font_family
        self.layouts = []

        # Aplicativo
        self.app = CustomApp(sys.argv)

        # Janela
        self.window = MyWindow()
        self.window.setFixedSize(width, height)
        self.window.setStyleSheet(f"background-color: {background_color};")

        # Layout principal
        self.main_layout = self.add_layout("vertical")
        self.window.setLayout(self.main_layout.get_layout())

        # Fim da janela
        self.window.show()

    def add_layout(self, position: Literal["horizontal", "vertical"] = "vertical") -> MyLayout:
        """
        Cria um layout na janela principal.

        Args:
            position (Literal["horizontal", "vertical"], optional): Posição do layout. Defaults to "vertical".
        """
        new_layout = self.window.create_layout(position)
        self.layouts.append(new_layout)
        return new_layout

    def add_label(
        self,
        text: str,
        *,
        size_text: int = 12,
        color_text: str | None = None,
        border_width: int = 0,
        border_radius: int = 0,
        alignment: Literal['left', 'center', 'right'] = "center",
        font_family: str | None = None,
        font_weight: Literal['normal', 'bold'] = "normal"
    ) -> MyLabel:
        """
        Cria um label.

        Args:
            text (str): Texto do label.
        """
        return MyLabel(
            alignment=alignment,
            border_radius=border_radius,
            border_width=border_width,
            color_text=color_text or self.secondary_color,
            font_family=font_family or self.font_family,
            font_weight=font_weight,
            size_text=size_text,
            text=text
        )

    def add_button(
        self,
        text: str,
        *,
        color_text: str | None = None,
        border_radius: int = 6,
        variant: Literal['success', 'error', 'natural'] = "natural",
        font_family: str | None = None,
        font_size: int = 10,
        width: int | None = None,
        height: int = 60,
        padding: int = 10
    ) -> MyButton:
        """
        Cria um botão.

        Args:
            text (str): Texto do botão.
        """
        return MyButton(
            border_radius=border_radius,
            font_family=font_family or self.font_family,
            font_size=font_size,
            padding=padding,
            text=text,
            variant=variant,
            width=width,
            height=height,
            hover_color=self.secondary_color,
            background_color=self.background_color,
            text_color=color_text or self.secondary_color,
        )

    def add_input(
        self,
        placeholder: str = "",
        *,
        size_text: int = 12,
        color_text: str | None = None,
        border_width: int = 0,
        border_radius: int = 3,
        padding: int = 10,
        margin: int = 10,
        alignment: Literal["left", "center", "right"] = "left",
        font_family: str | None = None,
        font_weight: Literal["normal", "bold"] | int = "normal",
        width: int | None = None,
        height: int | None = 65,
    ) -> MyInput:
        """
        Cria um input.

        Args:
            placeholder (str, optional): Placeholder do input. Defaults to "".
        """
        return MyInput(
            alignment=alignment,
            border_radius=border_radius,
            border_width=border_width,
            color_text=color_text or self.secondary_color,
            font_family=font_family or self.font_family,
            font_weight=font_weight,
            margin=margin,
            padding=padding,
            placeholder=placeholder,
            size_text=size_text,
            width=width,
            height=height
        )

    def run(self):
        """
        Executa a aplicação.
        """

        for layout in self.layouts:
            if layout is not self.main_layout:
                self.main_layout.add_layout(layout.get_layout())


        self.main_layout.add_stretch()
        self.app.exec()
