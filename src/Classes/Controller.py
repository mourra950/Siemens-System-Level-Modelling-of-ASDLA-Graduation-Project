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

class Controller:
    def __init__(self) -> None:
        self.res_block_built = False
    def on_generate_files_clicked(self):
        generator = self.file_read_json()
        self.generate_model()
        self.generate_train()

    def on_res_block_clicked(self, func_name, torch_funcs, on_submit_func):
        if(self.res_block_built):
            self.on_torch_func_clicked(func_name, torch_funcs, on_submit_func)
        else:
            self.res_block_built = True
            self.ResCreation.show()

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
