from PySide6.QtWidgets import (
    QVBoxLayout,
    QLabel,
    QDialog,
    QDialogButtonBox,
    QHBoxLayout,
    QLineEdit,
    QSpinBox,
    QComboBox,
    QCheckBox,
)
from numpy import maximum
import types


class LayerDialog(QDialog):
    def __init__(self, parent=None, t=None, x=None):
        super().__init__(parent)
        self.d = {}
        self.setWindowTitle(x)
        self.a = 6
        self.layout = QVBoxLayout()
        for i in t[x]:
            l2 = QHBoxLayout()
            la = QLabel(f'{i["name"]}')
            print(i)
            if i["type"] == type(1):
                lb = QSpinBox(parent=parent, maximum=1000)
            elif i["type"] == type(True):
                lb = QComboBox()
                lb.addItems(["True", "False"])
                lb.setEditable(False)
            else:
                lb = QLineEdit()
            self.d[i["name"]] = {"name": i["name"], "function": lb, "type": i["type"]}
            l2.addWidget(la)
            l2.addWidget(lb)
            self.layout.addLayout(l2)
        buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(buttons)
        self.buttonBox.accepted.connect(self.re)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def re(self):
        for i in self.d:
            if int == self.d[i]["type"]:
                print(self.d[i])
            else:
                print("default")
        super().accept()
