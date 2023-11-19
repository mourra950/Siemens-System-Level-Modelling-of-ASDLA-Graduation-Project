import os
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
basedir = os.path.dirname(__file__)
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
window.setWindowTitle("System Level Modelling")
with open("skin.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
window.show()
app.exec()
