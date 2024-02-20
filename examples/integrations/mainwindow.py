import os
import sys
basedir = os.path.dirname(__file__)
resdir = os.path.normpath(os.path.join(basedir,'../../public/'))
srcdir = os.path.normpath(os.path.join(basedir,'../../src/'))


from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QPushButton,
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from dialogue import LayerDialog

sys.path.append(srcdir)

from utils.AutoExtraction import (
    extract_torch_layers,
    extract_torch_lossfunctions,
    extract_torch_optimizers,
)


loader = QUiLoader()


class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load(os.path.normpath(os.path.join(resdir, "./GUI/mainwindow.ui")), None)
        
        self.find_children()
        self.extract_data()
        self.fill_placeholders()
        
        self.ui.setWindowTitle("Integration")
        self.ui.show()

    def printerr(self):
        print("no")

    def printyes(self):
        print("yes")

    def the_button_was_clicked(self, x):
        dlg = LayerDialog(layers=self.LAYERS, x=x)

        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")
    def fill_placeholders(self):
        self.fill_layers()
        self.fill_optimizers()
        self.fill_lossfunctions()
    def extract_data(self):
        self.LAYERS = extract_torch_layers()
        self.LOSSFUNC = extract_torch_lossfunctions()
        self.OPTIMIZERS = extract_torch_optimizers()
    def find_children(self):
        self.layers_scroll_box = self.ui.findChild(QVBoxLayout, "Scrollbox")

    def fill_optimizers(self):
        ...
    def fill_lossfunctions(self):
        ...
    def fill_layers(self):
        try:
            for i in self.LAYERS:
                button = QPushButton(i)
                button.clicked.connect(
                    lambda func=self.the_button_was_clicked, x=i: func(x)
                )
                self.layers_scroll_box.addWidget(button)

        except:
            print("Error")

        

def main():
    
    app = QApplication(sys.argv)

    window = MainUI()
    with open(os.path.join(resdir, "./GUI/skin.qss"), "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    app.exec()


if __name__ == "__main__":
    main()
