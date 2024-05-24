from paths.SystemPaths import SystemPaths
from utils.AutoExtraction import AutoExtraction
from Classes.Initializer import Initializer
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import sys
from PySide6.QtWidgets import QApplication


# import classes and different files here


def main():

    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


class MainUI(QtCore.QObject, SystemPaths, Initializer):
    def __init__(self):
        self.AutoExtraction = AutoExtraction()
        self.loader = QUiLoader()
        self.debug = True
        self.LAYERS, self.LOSSFUNC, self.OPTIMIZERS, self.PRETRAINED_MODELS, self.LAYERS_WITHOUT_RES = self.AutoExtraction.extracted_data()
        SystemPaths.__init__(self)
        Initializer.__init__(self)
        self.ui.show()


if __name__ == "__main__":
    main()
