import sys
from PySide6.QtWidgets import (
    QApplication,
)
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

# import classes and different files here
from Classes.Initializer import Initializer

from utils.AutoExtraction import AutoExtraction
from paths.SystemPaths import SystemPaths
import subprocess

loader = QUiLoader()

# Initialize the MainUI class to start the program


def main():
    # tensoboardproccess = subprocess.Popen(
    #     ["tensorboard", "--logdir", "E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/data/tensorboardlogs"])
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()
    # tensoboardproccess.kill()
    # while True:
    #     if tensoboardproccess.wait()!= None:
    #         break


class MainUI(QtCore.QObject, SystemPaths, Initializer, AutoExtraction):
    def __init__(self):
        self.loader = loader
        # QtCore.QObject.__init__(self)
        SystemPaths.__init__(self)
        AutoExtraction.__init__(self)
        Initializer.__init__(self)
        self.ui.show()


if __name__ == "__main__":
    main()
