from PySide6.QtWidgets import (
    QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6 import QtCore


class TensorView:
    def __init__(self) -> None:
        # find the window
        self.tensorQt = self.ui.findChild(QVBoxLayout, "TensorView")
        # create and add the webview object qt
        self.tensorWeb = QWebEngineView()
        self.tensorQt.addWidget(self.tensorWeb)
        self.tensorWeb.load(QtCore.QUrl("http://localhost:6006/"))
