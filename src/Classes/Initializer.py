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
from Classes.Children import Childreen
from Classes.DataSubmission import DataSubmission
from Classes.Filling import FillingQt
from Classes.Validator import Validator
from Classes.LayerNodeManager import LayerNodeManager
from utils.FileGenerator import FileGenerator
from Classes.Conn import Connections
from Classes.Controller import Controller


sys.path.append("./")

class Initializer(Childreen,DataSubmission,FillingQt,Validator,LayerNodeManager,FileGenerator,Controller,Connections):
    def __init__(self) -> None:
        print("Initializer")
        LayerNodeManager.__init__(self)
        self.ui = self.loader.load(self.GUI_path, None)
        self.ui.setWindowTitle("The Awesome Project")

        self.find_children()
        
        self.fill_placeholders()
        Connections.__init__(self)

        self.ui.show()

    def on_submit_layer_clicked(self, layer_type, params_names, params_value_widgets, paramsWindow_QDialog):
        print("Submit layer")
        layer = {
            'type': layer_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])

            if param_value != '':
                layer['params'][params_names[i]] = param_value

        self.create_layer_node(layer, -1)
        paramsWindow_QDialog.close()

    def on_select_lossfunc_clicked(self, lossfunc_type, params_names, params_value_widgets, paramsWindow_QDialog):
        self.selected_lossfunc = {
            'type': lossfunc_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])

            if param_value != '':
                self.selected_lossfunc['params'][params_names[i]] = param_value

        self.qt_selectedLossFunc_QLineEdit.setText(lossfunc_type)
        paramsWindow_QDialog.close()

    def on_select_optimizer_clicked(self, optimizer_type, params_names, params_value_widgets, paramsWindow_QDialog):
        self.selected_optimizer = {
            'type': optimizer_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])

            if param_value != '':
                self.selected_optimizer['params'][params_names[i]
                                                  ] = param_value

            self.qt_selectedOptimizer_QLineEdit.setText(optimizer_type)
        paramsWindow_QDialog.close()

    def on_torch_func_clicked(self, func_name, torch_funcs, on_submit_func):
        paramsWindow_QDialog = QDialog()
        paramsWindow_QDialog.setMinimumWidth(330)
        allParamsColumn_QVBoxLayout = QVBoxLayout()
        params_value_widgets = []
        params_names = []

        for param in torch_funcs[func_name]:
            if type(param['defaultvalue']) == bool:
                paramValue_QWidget = QCheckBox()
                paramValue_QWidget.setChecked(param['defaultvalue'])
            elif type(param['defaultvalue']) == int:
                paramValue_QWidget = QSpinBox( maximum=1000)
                paramValue_QWidget.setValue(0)
            else:
                paramValue_QWidget = QLineEdit()
                if (
                    param['defaultvalue'] != inspect._empty
                    and
                    param['defaultvalue'] != None
                ):
                    paramValue_QWidget.setText(str(param['defaultvalue']))

            params_names.append(param['name'])
            params_value_widgets.append(paramValue_QWidget)

            paramRow_QHBoxLayout = QHBoxLayout()
            paramRow_QHBoxLayout.addWidget(QLabel(f'{param["name"]}'))
            paramRow_QHBoxLayout.addWidget(paramValue_QWidget)
            allParamsColumn_QVBoxLayout.addLayout(paramRow_QHBoxLayout)

        allParamsColumn_QVBoxLayout.addWidget(QLabel())
        submitLayer_QPushButton = QPushButton('Submit Layer')
        submitLayer_QPushButton.clicked.connect(
            lambda i=func_name, j=params_names, k=params_value_widgets, l=paramsWindow_QDialog: on_submit_func(
                i, j, k, l)
        )
        allParamsColumn_QVBoxLayout.addWidget(submitLayer_QPushButton)
        paramsWindow_QDialog.setLayout(allParamsColumn_QVBoxLayout)
        paramsWindow_QDialog.setWindowTitle(f"{func_name}")
        paramsWindow_QDialog.exec()

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
