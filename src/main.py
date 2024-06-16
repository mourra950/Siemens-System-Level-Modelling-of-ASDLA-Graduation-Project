from paths.SystemPaths import SystemPaths
from utils.AutoExtraction import AutoExtraction
from Classes.Initializer import Initializer
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import sys
from PySide6.QtWidgets import QApplication
from Tests.StaticAnalysis import StaticAnalysis


def main():

    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


class MainUI(QtCore.QObject, Initializer):
    def __init__(self):

        self.debug = False
        self.SysPath = SystemPaths()

        self.AutoExtraction = AutoExtraction(self.debug)
        self.StaticAnalysis = StaticAnalysis(
            self.SysPath.warning_rules_path, self.debug)

        self.loader = QUiLoader()
        (
            self.LAYERS,
            self.LOSSFUNC,
            self.OPTIMIZERS,
            self.SCHEDULERS,
            self.PRETRAINED_MODELS,
            self.LAYERS_WITHOUT_RES,
            self.DATASETS,
        ) = self.AutoExtraction.extracted_data()

        Initializer.__init__(self)
        self.ui.show()


if __name__ == "__main__":
    main()
