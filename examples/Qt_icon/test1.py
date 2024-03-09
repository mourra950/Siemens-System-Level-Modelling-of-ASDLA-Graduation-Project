import torch.nn.modules as nn
import os
import sys
import inspect
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QDialog,
    QHBoxLayout,
    QStyle
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

from PySide6 import QtCore

basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.ui = loader.load(os.path.join(basedir, "test.ui"), None)
        self.ui.setWindowTitle("Testing generating scripts")
        t = os.path.normpath(
            os.path.join(basedir, "imgs/delete.png"))
        self.Vbox = self.ui.findChild(QVBoxLayout, "Scrollbox")
        button = QPushButton()

        Icon = QIcon(t)
        button.setIcon(Icon)
        button.setIconSize(QtCore.QSize(50, 50))

        self.Vbox.addWidget(button)

        self.ui.show()


def main():
    app = QApplication(sys.argv)

    window = MainUI()
    # with open(os.path.join(basedir, "skin.qss"), "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)
    app.exec()


if __name__ == "__main__":
    main()
