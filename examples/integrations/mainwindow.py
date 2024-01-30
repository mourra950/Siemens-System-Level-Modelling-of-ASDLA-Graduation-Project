import os
import sys
import inspect
from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QPushButton,
    QLabel,
    QLineEdit,
    QDialog,
    QHBoxLayout,
    QDialogButtonBox,
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import torch.nn.modules as nn
import json
from dialogue import LayerDialog


basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.ui = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
        self.ui.setWindowTitle("Testing generating scripts")

        self.Vbox = self.ui.findChild(QVBoxLayout, "Scrollbox")

        try:
            self.t = extract()

            for i in self.t:
                button = QPushButton(i)
                button.clicked.connect(
                    lambda func=self.the_button_was_clicked, x=i: func(x)
                )
                self.Vbox.addWidget(button)

        except:
            print("Error")

        self.ui.show()

    def printerr(self):
        print("no")

    def printyes(self):
        print("yes")

    def the_button_was_clicked(self, x):
        dlg = LayerDialog(t=self.t, x=x)

        if dlg.exec():
            print(dlg)
            print(dlg.accepted)
            print(dlg.a)
            print("Success!")
        else:
            print("Cancel!")

        # dlg.exec()


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
