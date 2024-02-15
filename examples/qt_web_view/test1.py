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
)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import torch.nn.modules as nn

basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.ui = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
        self.ui.setWindowTitle("TensorBoard test")

        self.Vbox = self.ui.findChild(QVBoxLayout, "weblay")
        t = QWebEngineView()
        t.load(QtCore.QUrl("http://localhost:6006/"))
        self.Vbox.addWidget(t)

        self.ui.show()

    def the_button_was_clicked(self, x):
        dlg = QDialog()
        l1 = QVBoxLayout()
        for i in self.t[x]:
            l2 = QHBoxLayout()
            la = QLabel(f'{i["name"]}')
            lb = QLineEdit()
            l2.addWidget(la)
            l2.addWidget(lb)
            l1.addLayout(l2)

        label = QLabel(f"{x}")
        verti = QVBoxLayout()
        verti.addWidget(label)
        dlg.setLayout(l1)
        dlg.setWindowTitle(f"{x}")
        dlg.exec()


def extract():
    N = dir(nn)

    annotationslist = [type(1), type("a"), type(True), type((2, 2))]

    testdict = dict()

    for j in N:
        obj = getattr(nn, j)

        if (
            isinstance(obj, type)
            and obj is not nn.Module
            and issubclass(obj, nn.Module)
        ):
            inspector = inspect.signature(obj).parameters
            templist = list()
            for i in inspector:
                if (
                    inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD
                ) and (inspector[i].annotation in annotationslist):
                    templist.append(
                        {
                            "name": inspector[i].name,
                            "defaultvalue": inspector[i].default,
                            "type": inspector[i].annotation,
                        }
                    )
            if len(templist) > 0:
                testdict[obj.__name__] = templist
    return testdict


def main():
    app = QApplication(sys.argv)

    window = MainUI()
    with open(os.path.join(basedir, "skin.qss"), "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    app.exec()


if __name__ == "__main__":
    main()
