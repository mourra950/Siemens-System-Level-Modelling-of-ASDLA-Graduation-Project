from PySide6.QtWidgets import (
    QVBoxLayout
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import subprocess



class TensorView:
    def __init__(self) -> None:
        self.tensorQt = self.ui.findChild(QVBoxLayout, "TensorView")
        self.tensorWeb = QWebEngineView()
        self.tensorWeb.load(QtCore.QUrl("http://localhost:5173/"))
        self.tensorQt.addWidget(self.tensorWeb)
        subprocess.run("dir",shell=True) 
        