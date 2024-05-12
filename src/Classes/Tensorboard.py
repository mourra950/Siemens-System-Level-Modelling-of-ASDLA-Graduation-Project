from PySide6.QtWidgets import (
    QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6 import QtCore
from PySide6.QtCore import QUrl,QProcess


class TensorView:
    def __init__(self) -> None:
        self.Tensorboard_Process = QProcess()
        self.Tensorboard_Process.start(
            "tensorboard", ["--logdir",self.log_path])

        # get the tensorboard object from the ui
        self.tensorQt = self.ui.findChild(QVBoxLayout, "TensorView")
        # create and add the webview object qt
        self.tensorWeb = QWebEngineView()
        self.tensorQt.addWidget(self.tensorWeb)
        self.tensorWeb.setUrl(QUrl("http://localhost:6006/"))
