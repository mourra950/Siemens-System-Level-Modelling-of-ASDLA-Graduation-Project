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
import inspect
import types


class LayerDialog(QDialog):
    def __init__(self, parent=None, t=None, x=None):
        super().__init__(parent)
        self.d = {}
        self.setWindowTitle(x)
        self.a = 6
        self.layout = QVBoxLayout()
        for i in t[x]:
            de = True
            if i["defaultvalue"] == inspect._empty:
                de = False
            print(i["defaultvalue"])
            l2 = QHBoxLayout()
            la = QLabel(f'{i["name"]}')
            if i["type"] == type(1):
                lb = QSpinBox(parent=parent, maximum=1000)
                if de:
                    lb.setValue(int(i["defaultvalue"]))
            elif i["type"] == type(True):
                lb = QCheckBox()

                # lb.addItems(["True", "False"])
                # lb.setEditable(False)
                if de:
                    lb.setChecked(i["defaultvalue"])

            else:
                lb = QLineEdit()
                lb.setText(i["defaultvalue"])
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
                print(
                    self.d[i]["name"], "int", self.d[i]["function"].value()
                )  # self.d[i]
            elif str == self.d[i]["type"]:
                print("ahmed", self.d[i]["function"].text())
                if self.d[i]["function"].text() == "":
                    print("empty")
            elif bool == self.d[i]["type"]:
                if self.d[i]["function"].isChecked():
                    print("True")
                else:
                    print("False")
            else:
                print("default")
        super().accept()