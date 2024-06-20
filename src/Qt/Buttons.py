from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QFrame
)
from PySide6.QtGui import QIcon
from utils.Singleton import Singleton


class QTButtons(metaclass=Singleton):

    def qbutton_layer_manager(self, icon_path, qt_layout, border_QFrame, function, *args):
        Button = QPushButton()
        Button.setMaximumWidth(30)
        Button.setIcon(QIcon(icon_path))
        Button.clicked.connect(
            lambda func=function, i=border_QFrame, q_layout=qt_layout:
                func(i, q_layout, *args)
        )

        return Button
