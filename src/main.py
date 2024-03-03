import sys
from PySide6.QtWidgets import (
    QApplication,
)
from PySide6 import QtCore
from PySide6.QtUiTools import QUiLoader

#import classes and different files here
from Qt.dialogue import LayerDialog
from Classes.Initializer import Initializer
from utils.AutoExtraction import AutoExtraction
from paths.SystemPaths import SystemPaths


loader = QUiLoader()

#Initialize the MainUI class to start the program
def main():
    app = QApplication(sys.argv)
    window = MainUI()
    # with open(os.path.join(publicdir, "./GUI/skin.qss"), "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)
    app.exec()
    
class MainUI(QtCore.QObject,SystemPaths,Initializer,AutoExtraction):
    def __init__(self):
        self.loader = loader
        # LayerDialog.__init__(self)
        QtCore.QObject.__init__(self)
        AutoExtraction.__init__(self)
        SystemPaths.__init__(self)
        Initializer.__init__(self)
        self.ui.show()
        
    def the_button_was_clicked(self, x):
        dlg = LayerDialog(layers=self.LAYERS, x=x)

        if dlg.exec():
            print("Success!")
        else:
            print("Cancel!")

    

if __name__ == "__main__":
    main()
