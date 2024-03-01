import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout,QLabel,QCheckBox,QDialog
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import inspect


class Initializer:
        def __init__(self) -> None:
                print("Initializer")
                
                
                self.ui = self.loader.load(os.path.normpath(os.path.join(self.publicdir, "./GUI/mainwindow.ui")), None)
                self.ui.setWindowTitle("The Awesome Project")
                
                #search for qt elements 
                self.find_children()
                #using extracted data start filling element with necessary information
                self.fill_placeholders()
                
                self.ui.show()
                
                

        def fill_placeholders(self):
                self.fill_layers()
                self.fill_optimizers()
                self.fill_lossfunctions()
        def find_children(self):
                self.qt_layers_scroll_box = self.ui.findChild(QVBoxLayout, "Scrollbox")
                self.qt_layersList_QVBoxLayout = self.ui.findChild(QVBoxLayout, 'layersList_QVBoxLayout')
                self.qt_inputWidth_QLineEdit = self.ui.findChild(QLineEdit, 'inputWidth_QLineEdit')
                self.qt_inputHeight_QLineEdit = self.ui.findChild(QLineEdit, 'inputHeight_QLineEdit')
                self.qt_batchSize_QLineEdit = self.ui.findChild(QLineEdit, 'batchSize_QLineEdit')
                self.qt_learningRate_QLineEdit = self.ui.findChild(QLineEdit, 'learningRate_QLineEdit')
                self.qt_numEpochs_QLineEdit = self.ui.findChild(QLineEdit, 'numEpochs_QLineEdit')
                self.qt_selectedOptimizer_QLineEdit = self.ui.findChild(QLineEdit, 'selectedOptimizer_QLineEdit')
                self.qt_selectedLossFunc_QLineEdit = self.ui.findChild(QLineEdit, 'selectedLossFunc_QLineEdit')
                # self.qt_inputType_RGB_QRadioButton = self.ui.findChild(QRadioButton, 'inputType_RGB_QRadioButton')
                # self.qt_inputType_grayScale_QRadioButton = self.ui.findChild(QRadioButton, 'inputType_grayScale_QRadioButton')
                # self.qt_addedLayers_QVBoxLayout = self.ui.findChild(QVBoxLayout, 'addedLayers_QVBoxLayout')
                self.qt_optimizersList_QVBoxLayout = self.ui.findChild(QVBoxLayout, 'optimizersList_QVBoxLayout')
                self.qt_lossFuncsList_QVBoxLayout = self.ui.findChild(QVBoxLayout, 'lossFuncsList_QVBoxLayout')
                # self.qt_submitParams_QPushButton = self.ui.findChild(QPushButton, 'submitParams_QPushButton')
                # self.qt_submitArch_QPushButton = self.ui.findChild(QPushButton, 'submitArch_QPushButton')
                # self.qt_generateFiles_QPushButton = self.ui.findChild(QPushButton, 'generateFiles_QPushButton')

        def fill_optimizers(self):
                for optimizer in self.OPTIMIZERS:
                        selectOptimizer_QPushButton = QPushButton(optimizer)
                        selectOptimizer_QPushButton.clicked.connect(
                        lambda  i=optimizer, j=self.OPTIMIZERS, k=self.on_select_optimizer_clicked \
                        : self.on_torch_func_clicked(i,j,k)
                        )
                        self.qt_optimizersList_QVBoxLayout.addWidget(selectOptimizer_QPushButton)
        def fill_lossfunctions(self):
                for lossfunc in self.LOSSFUNC:
                        selectLossFunc_QPushButton = QPushButton(lossfunc)
                        selectLossFunc_QPushButton.clicked.connect(
                        lambda  i=lossfunc, j=self.LOSSFUNC, k=self.on_select_lossfunc_clicked \
                    : self.on_torch_func_clicked(i,j,k)
                )
                        self.qt_lossFuncsList_QVBoxLayout.addWidget(selectLossFunc_QPushButton)
        def fill_layers(self):
                try:
                        for i in self.LAYERS:
                                button = QPushButton(i)
                                button.clicked.connect(
                                lambda func=self.the_button_was_clicked, x=i: func(x)
                                )
                                self.qt_layersList_QVBoxLayout.addWidget(button)

                except Exception as e:
                        print(e)  
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
                                self.selected_optimizer['params'][params_names[i]] = param_value

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
                lambda i=func_name, j=params_names, k=params_value_widgets, l=paramsWindow_QDialog \
                        : on_submit_func(i,j,k,l)
                )
                allParamsColumn_QVBoxLayout.addWidget(submitLayer_QPushButton)
                paramsWindow_QDialog.setLayout(allParamsColumn_QVBoxLayout)
                paramsWindow_QDialog.setWindowTitle(f"{func_name}")
                paramsWindow_QDialog.exec()