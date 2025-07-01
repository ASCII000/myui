"""
Modulo que contem o componente de input padronizado no projeto.
"""

from typing import Literal, Callable

from PySide6 import QtWidgets, QtCore, QtGui


class MyInput(QtWidgets.QLineEdit):

    def __init__(
        self,
        placeholder: str = "",
        *,
        size_text: int = 18,
        color_text: str = "#ffffff",
        background_color: str = "#707070",
        border_width: int = 0,
        border_radius: int = 0,
        padding: int = 10,
        margin: int = 10,
        alignment: Literal["left", "center", "right"] = "left",
        font_family: str = "Segoe UI",
        font_weight: Literal["normal", "bold"] = "normal",
        width: int | None = 14,
        height: int | None = 300,
    ):
        super().__init__()

        # Callbacks
        self.key_pressed_callback_rules = None
        self.key_pressed_callback = None
        self.f_text = ""

        # Define o placeholder
        self.setPlaceholderText(placeholder)

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

        if width is not None:
            self.setFixedWidth(width)

        if height is not None:
            self.setFixedHeight(height)

        # Cria o estilo CSS
        style = f"""
            QLineEdit {{
                color: {color_text};
                background-color: {background_color}; /* aqui define a cor de fundo */
                border: {border_width}px solid {background_color};
                border-radius: {border_radius}px;
                padding: {padding}px;
                margin: {margin}px;
            }}

            QLineEdit::Focus {{
                background-color: {color_text};
                color: {background_color};
            }}
        """
        
        self.setStyleSheet(style)

    def add_key_pressed_callback(
        self,
        callback: Callable[[str], str],
        callback_rules: Callable[[str], bool] | None = None
    ) -> None:
        """
        Adiciona uma callback para o evento de tecla pressionada.

        Args:
            callback (Callable[[QtWidgets.QLineEdit]]): Função a ser chamada quando uma tecla for pressionada.
            callback_rules (Callable[[str], bool] | None, optional): Função de regra para o evento de tecla pressionada.
                Se fornecido, a callback será chamada apenas se a regra retornar True.
        """
        self.key_pressed_callback_rules = callback_rules
        self.key_pressed_callback = callback

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        key = event.key()
        modifiers = event.modifiers()

        conditions_to_delete = (
            (modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_X),
            (modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_V),
            (modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_Z),
        )

        conditions_to_skip = (
            (modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_C),
            (modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_A),
        )

        # Condicoes para deletar
        if any(conditions_to_delete):
            # Executa o comportamento padrão: selecionar tudo
            self.f_text = ""
            super().keyPressEvent(event)
            return

        # Condicoes para ignorar
        if any(conditions_to_skip):
            super().keyPressEvent(event)
            return


        # Ctrl + X (Cut)
        if modifiers == QtCore.Qt.ControlModifier and key == QtCore.Qt.Key_X:
            if self.hasSelectedText():
                start = self.selectionStart()
                end = start + len(self.selectedText())
                self.f_text = self.f_text[:start] + self.f_text[end:]

                if self.key_pressed_callback:
                    return_text = self.key_pressed_callback(self.f_text)
                    if return_text is not None:
                        self.setText(return_text)
                        self.setCursorPosition(start)
                        return
                else:
                    self.setText(self.f_text)
                    self.setCursorPosition(start)
                    return

        # Backspace/Delete com seleção
        if self.hasSelectedText():
            
            start = self.selectionStart()
            end = start + len(self.selectedText())

            if key in (QtCore.Qt.Key_Backspace, QtCore.Qt.Key_Delete):
                self.f_text = self.f_text[:start] + self.f_text[end:]

                if self.key_pressed_callback:
                    return_text = self.key_pressed_callback(self.f_text)
                    if return_text is not None:
                        self.setText(return_text)
                        self.setCursorPosition(start)
                        return
                else:
                    self.setText(self.f_text)
                    self.setCursorPosition(start)
                    return

        # Backspace sem seleção
        if key == QtCore.Qt.Key_Backspace:
            self.f_text = self.f_text[:-1]

        # Delete sem seleção (opcional)
        elif key == QtCore.Qt.Key_Delete:
            pass  # Implementar caso queira

        # Outros caracteres digitados
        else:

            if self.key_pressed_callback_rules:
                if not self.key_pressed_callback_rules(self.f_text):
                    return

            self.f_text += event.text()

        if self.key_pressed_callback:
            return_text = self.key_pressed_callback(self.f_text)
            if return_text is not None:
                self.setText(return_text)
                self.setCursorPosition(len(return_text))
                return

        super().keyPressEvent(event)
