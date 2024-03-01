import os
import sys
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
import threading

basedir = os.path.dirname(__file__)


def start_tensorboard():
    os.system("tensorboard --logdir logs/fit")


loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
x = threading.Thread(target=start_tensorboard)
x.start()
window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
window.setWindowTitle("System Level Modelling")
with open(os.path.join(basedir, "skin.qss"), "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)
window.show()
app.exec()
