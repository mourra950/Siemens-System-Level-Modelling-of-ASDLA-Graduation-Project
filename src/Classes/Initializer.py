import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout, QLabel, QCheckBox, QDialog, QSpinBox, QRadioButton
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import inspect
from Classes.Children import Children
from Classes.DataSubmission import DataSubmission
from Classes.Filling import FillingQt
from Classes.Validator import Validator
from Classes.LayerNodeManager import LayerNodeManager
from utils.FileGenerator import FileGenerator
from Classes.Conn import Connections
from Classes.Controller import Controller
from Classes.Tensorboard import TensorView
from Classes.ResNet.resbuild import ResBuildWindow

sys.path.append("./")

class Initializer(Children,DataSubmission,FillingQt,Validator,LayerNodeManager,FileGenerator,Controller,Connections,TensorView,ResBuildWindow):
    def __init__(self) -> None:
        print("Initializer")
        LayerNodeManager.__init__(self)
        self.ui = self.loader.load(self.GUI_path, None)
        self.ui.setWindowTitle("The Awesome Project")

        self.find_children()
        
        self.fill_placeholders()
        ResBuildWindow.__init__(self)
        
        Connections.__init__(self)
        TensorView.__init__(self)
        self.ResCreation.show()
        # self.ui.show()

    def get_widget_data(self, widget):
        if isinstance(widget, QCheckBox):
            param_value = widget.isChecked()
        if isinstance(widget, QSpinBox):
            param_value = widget.value()
        else:
            param_value = widget.text().strip()
            try:
                param_value = eval(param_value)
            except:
                pass
        return param_value
