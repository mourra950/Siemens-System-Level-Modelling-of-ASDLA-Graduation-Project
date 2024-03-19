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
from Qt.Buttons import QTButtons
from Qt.Dialogue import LayerDialog



sys.path.append("./")

class Initializer(Children,DataSubmission,FillingQt,Validator,LayerNodeManager,FileGenerator,Controller,Connections,TensorView,ResBuildWindow,QTButtons,LayerDialog):
    def __init__(self) -> None:
        print("Initializer")
        Children.__init__(self)
        Controller.__init__(self)
        LayerNodeManager.__init__(self)
        FillingQt.__init__(self)
        ResBuildWindow.__init__(self)
        Connections.__init__(self)
        TensorView.__init__(self)
        self.ui.setWindowTitle("The Awesome Project")
        
        

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
