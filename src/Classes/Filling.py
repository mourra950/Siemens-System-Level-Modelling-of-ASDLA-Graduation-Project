from PySide6.QtWidgets import (
    QPushButton,
)
from PySide6.QtUiTools import QUiLoader


class FillingQt:
    def __init__(self) -> None:
        self.fill_placeholders(
            self.qt_layersList_QVBoxLayout, self.LAYERS, self.qt_addedLayers_QVBoxLayout)
        self.fill_layers(self.res_layersList_QVBoxLayout,
                         self.LAYERS_WITHOUT_RES, self.res_addedLayers_QVBoxLayout,self.Resarchitecture)

    def fill_placeholders(self, qt_layout, layers, q2_lay):
        self.fill_layers(qt_layout, layers, q2_lay,self.architecture)
        self.fill_optimizers()
        self.fill_lossfunctions()
        self.fill_pretrained_model()

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

    def fill_layers(self, qt_layout, layers, q2_layout, arch_dict):
        for layer in layers:
            selectLayer_QPushButton = QPushButton(layer)
            if (layer == "Residual Block"):
                selectLayer_QPushButton.clicked.connect(
                    lambda func=self.on_res_block_clicked, i=layer, j=self.LAYERS, k=self.on_submit_layer_clicked, q_layout=q2_layout: 
                    func(i, j, k, q_layout)
                )
                qt_layout.addWidget(
                    selectLayer_QPushButton)
            else:
                selectLayer_QPushButton.clicked.connect(
                    lambda func=self.on_torch_func_clicked, i=layer, j=self.LAYERS, k=self.on_submit_layer_clicked, q_layout=q2_layout, dic = arch_dict: func(
                        i, j, k, q_layout,arch_dict)
                )
                qt_layout.addWidget(
                    selectLayer_QPushButton)
    def fill_pretrained_model(self):
        #TO DO
        for i in self.PRETRAINED_MODELS:
            self.Pretrained_model_ComboBox.addItem(i)