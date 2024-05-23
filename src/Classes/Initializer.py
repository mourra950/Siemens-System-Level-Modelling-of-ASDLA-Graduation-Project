import sys
from PySide6.QtWidgets import QCheckBox, QSpinBox, QDoubleSpinBox, QComboBox
from Classes.Children import Children
from Classes.Data_Submission import DataSubmission
from Classes.Filling import FillingQt
from Classes.Validator import Validator
from Classes.Layer_Node_Manager import LayerNodeManager
from utils.FileGenerator import FileGenerator
from Classes.Connections import Connections
from Classes.Controller import Controller
from Classes.Tensorboard import TensorView
from Classes.ResNet.resbuild import ResBuildWindow
from Classes.Transfer_Learning import DataOfTransfer
from Tests.Layer_Testing import LayerTesting

from Qt.Buttons import QTButtons
from Qt.Dialogue import LayerDialog


sys.path.append("./")


class Initializer(
    Children,
    DataSubmission,
    FillingQt,
    Validator,
    LayerNodeManager,
    FileGenerator,
    Controller,
    Connections,
    TensorView,
    ResBuildWindow,
    QTButtons,
    LayerDialog,
    DataOfTransfer,
    LayerTesting
):
    def __init__(self) -> None:
        print("Initializer")
        Children.__init__(self)
        Controller.__init__(self)
        LayerNodeManager.__init__(self)
        FillingQt.__init__(self)
        ResBuildWindow.__init__(self)
        DataOfTransfer.__init__(self)
        Connections.__init__(self)
        TensorView.__init__(self)
        DataSubmission.__init__(self)
        LayerTesting.__init__(self)
        self.ui.setWindowTitle("The Awesome Project")

    def get_widget_data(self, widget):
        if isinstance(widget, QCheckBox):
            param_value = widget.isChecked()
        elif isinstance(widget, QSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QDoubleSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QComboBox):
            param_value = widget.currentData()
        else:
            param_value = widget.text().strip()
            try:
                param_value = eval(param_value)
            except:
                pass
        return param_value
