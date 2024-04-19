import os
import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QLabel,
    QFileDialog,
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from pathlib import Path

basedir = os.path.dirname(__file__)
loader = QUiLoader()


class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.path = ""
        self.ui = loader.load(os.path.join(basedir, "MainWindow.ui"), None)
        self.ui.setWindowTitle("Testing File Picker")

        self.pushButton1 = self.ui.findChild(QPushButton, "pushButton1")
        self.pushButton2 = self.ui.findChild(QPushButton, "pushButton2")
        self.label1 = self.ui.findChild(QLabel, "label1")

        self.pushButton1.clicked.connect(self.getFile)
        self.pushButton2.clicked.connect(self.getDirectory)

        self.ui.show()

    def getFile(self):
        path, _ = QFileDialog.getOpenFileName(
            None, "Open file", basedir, "JSON Files (*.json)"
        )
        self.path = Path(path)
        print(self.path)
        self.label1.setText(str(self.path))

    def getDirectory(self):
        dir_name = Path(QFileDialog.getExistingDirectory(
            None, "Select a Directory"))
        print(dir_name)
        self.path = dir_name
        self.label1.setText(str(self.path))


def main():
    app = QApplication(sys.argv)
    window = MainUI()
    app.exec()


if __name__ == "__main__":
    main()
