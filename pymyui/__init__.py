"""
MyUI Framework - A simple and intuitive Python framework for creating fast desktop interfaces
"""

__version__ = "1.0.0"
__author__ = "Emerson Silva"
__description__ = "A simple and intuitive Python framework for creating fast desktop interfaces"

from .controllers.app import MyApp
from .components.my_button import MyButton
from .components.my_input import MyInput
from .components.my_label import MyLabel
from .components.my_layout import MyLayout
from .components.my_notify import MyNotify

__all__ = [
    "MyApp",
    "MyButton", 
    "MyInput",
    "MyLabel",
    "MyLayout",
    "MyNotify",
]
