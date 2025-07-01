"""
Modulo que contem o componente de label padronizado no projeto.
"""

from typing import Literal
from PySide6 import QtWidgets, QtCore, QtGui

class MyLabel(QtWidgets.QLabel):
    def __init__(
        self,
        text: str,
        *,
        size_text: int = 18,
        color_text: str = "#ffffff",
        border_width: int = 0,
        border_radius: int = 0,
        alignment: Literal["left", "center", "right"] = "center",
        font_family: str = "Segoe UI",
        font_weight: Literal["normal", "bold"] = "normal",
    ):
        super().__init__()

        # Define o texto
        self.setText(text)

        # Define alinhamento
        align_map = {
            "left": QtCore.Qt.AlignLeft,
            "center": QtCore.Qt.AlignCenter,
            "right": QtCore.Qt.AlignRight,
        }
        self.setAlignment(align_map.get(alignment, QtCore.Qt.AlignCenter))

        # Define o weight da fonte
        weight_map = {
            "normal": QtGui.QFont.Normal,
            "bold": QtGui.QFont.Bold,
        }
        resolved_weight = weight_map.get(font_weight, QtGui.QFont.Bold)

        # Cria a fonte
        font = QtGui.QFont()
        font.setFamily(font_family)
        font.setPointSize(size_text)
        font.setWeight(resolved_weight)

        # Para ter certeza, usar setBold() também se weight for bold
        if font_weight == "bold":
            font.setBold(True)

        self.setFont(font)

        # Cria o estilo CSS
        style = f"""
            QLabel {{
                color: {color_text};
                border: {border_width}px solid {color_text};
                border-radius: {border_radius}px;
            }}
        """
        self.setStyleSheet(style)

        db = QtGui.QFontDatabase()
        if font_family not in db.families():
            print(f"⚠️ Aviso: fonte '{font_family}' não encontrada no sistema.")
