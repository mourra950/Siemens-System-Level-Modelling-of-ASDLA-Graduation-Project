import os
import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout, QLabel, QCheckBox, QDialog
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import inspect


class FillingQt:

    def fill_placeholders(self):
        self.fill_layers()
        self.fill_optimizers()
        self.fill_lossfunctions()

    def fill_optimizers(self):
        for optimizer in self.OPTIMIZERS:
            selectOptimizer_QPushButton = QPushButton(optimizer)
            selectOptimizer_QPushButton.clicked.connect(
                lambda func=self.on_torch_func_clicked, i=optimizer, j=self.OPTIMIZERS, k=self.on_select_optimizer_clicked: func(
                    i, j, k)
            )
            self.qt_optimizersList_QVBoxLayout.addWidget(
                selectOptimizer_QPushButton)

    def fill_lossfunctions(self):
        for lossfunc in self.LOSSFUNC:
            selectLossFunc_QPushButton = QPushButton(lossfunc)
            selectLossFunc_QPushButton.clicked.connect(
                lambda func=self.on_torch_func_clicked, i=lossfunc, j=self.LOSSFUNC, k=self.on_select_lossfunc_clicked: func(
                    i, j, k)
            )
            self.qt_lossFuncsList_QVBoxLayout.addWidget(
                selectLossFunc_QPushButton)

    def fill_layers(self):
        for layer in self.LAYERS:
            selectLayer_QPushButton = QPushButton(layer)
            selectLayer_QPushButton.clicked.connect(
                lambda func=self.on_torch_func_clicked, i=layer, j=self.LAYERS, k=self.on_submit_layer_clicked: func(
                    i, j, k)
            )
            self.qt_layersList_QVBoxLayout.addWidget(
                selectLayer_QPushButton)
