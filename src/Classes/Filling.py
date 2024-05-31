from PySide6.QtWidgets import (
    QPushButton
)
import torch


class FillingQt:
    def __init__(self) -> None:
        self.fill_placeholders(
            self.qt_layersList_QVBoxLayout, self.LAYERS, self.qt_addedLayers_QVBoxLayout
        )
        self.fill_layers(
            self.res_layersList_QVBoxLayout,
            self.LAYERS_WITHOUT_RES,
            self.res_addedLayers_QVBoxLayout,
            self.Resarchitecture,
        )

    def fill_placeholders(self, qt_layout, layers, q2_lay):
        self.fill_layers(qt_layout, layers, q2_lay, self.architecture)
        self.fill_optimizers()
        self.fill_lossfunctions()
        self.fill_schedulers()
        self.fill_pretrained_model()

    def fill_optimizers(self):
        for optimizer in self.OPTIMIZERS:
            selectOptimizer_QPushButton = QPushButton(optimizer)
            selectOptimizer_QPushButton.clicked.connect(
                lambda i=optimizer, j=self.OPTIMIZERS, k=self.on_select_optimizer_clicked: self.on_torch_func_clicked(
                    i, j, k, None, None
                )
            )
            self.qt_optimizersList_QVBoxLayout.addWidget(selectOptimizer_QPushButton)

    def fill_lossfunctions(self):
        for lossfunc in self.LOSSFUNC:
            selectLossFunc_QPushButton = QPushButton(lossfunc)
            selectLossFunc_QPushButton.clicked.connect(
                lambda i=lossfunc, j=self.LOSSFUNC, k=self.on_select_lossfunc_clicked: self.on_torch_func_clicked(
                    i, j, k, None, None
                )
            )
            self.qt_lossFuncsList_QVBoxLayout.addWidget(selectLossFunc_QPushButton)

    def fill_schedulers(self):
        for scheduler in self.SCHEDULERS:
            selectScheduler_QPushButton = QPushButton(scheduler)
            selectScheduler_QPushButton.clicked.connect(
                lambda i=scheduler, j=self.SCHEDULERS, k=self.on_select_scheduler_clicked: self.on_torch_func_clicked(
                    i, j, k, None, None
                )
            )

            self.qt_schedulersList_QVBoxLayout.addWidget(selectScheduler_QPushButton)
            print(self.qt_schedulersList_QVBoxLayout)

    def fill_layers(self, qt_layout, layers, q2_layout, arch_dict):
        for layer in layers:
            selectLayer_QPushButton = QPushButton(layer)
            if layer == "Residual Block":
                selectLayer_QPushButton.clicked.connect(
                    lambda i=layer, j=self.LAYERS, k=self.on_submit_layer_clicked, q_layout=q2_layout: self.on_res_block_clicked(
                        i, j, k, q_layout
                    )
                )
                qt_layout.addWidget(selectLayer_QPushButton)
            else:
                selectLayer_QPushButton.clicked.connect(
                    lambda i=layer, j=self.LAYERS, k=self.on_submit_layer_clicked, q_layout=q2_layout, dic=arch_dict: self.on_torch_func_clicked(
                        i, j, k, q_layout, dic
                    )
                )
                qt_layout.addWidget(selectLayer_QPushButton)

    def fill_pretrained_model(self):
        for i in self.PRETRAINED_MODELS:
            self.pretrained_model_combobox.addItem(i)

    def fill_cuda_devices(self, combo_box):
        device_names = []
        if torch.cuda.is_available():
            cuda_devices = torch.cuda.device_count()
            for i in range(cuda_devices):
                properties = torch.cuda.get_device_properties(i)
                device_name = properties.name
                device_names.append((i, device_name))

        combo_box.clear()
        for device_index, device_info in device_names:
            combo_box.addItem(device_info, device_index)

        combo_box.addItem("CPU", "CPU")
