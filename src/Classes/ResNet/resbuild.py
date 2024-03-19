from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout, QLabel, QCheckBox, QDialog, QSpinBox, QRadioButton,QMainWindow,QFrame
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6 import QtCore
import inspect
import json
import sys


class ResBuildWindow():
    def __init__(self) -> None:
        ...

    def res_on_submit_residual_block_clicked(self):
        # self.validate_and_correct_layers()
        with open(self.ResJson, 'w') as f:
            f.write(json.dumps(self.Resarchitecture, indent=2))
        self.ResCreation.close()


    # def validate_and_correct_layers(self):
    #     width = self.architecture['misc_params']['width']
    #     height = self.architecture['misc_params']['height']
    #     channels = self.architecture['misc_params']['channels']
    #     features_after_1st_FC = None
    #     flattened = False
    #     layer_freqs = dict()
    #     i = 0

    #     while i < len(self.architecture['layers']):
    #         layer = self.architecture['layers'][i]
    #         params = layer['params']
    #         layer_type = layer['type']
    #         self.add_layer_name(layer, layer_freqs)

    #         if layer_type == 'Conv2d':
    #             params['in_channels'] = channels
    #             width = (width - params['kernel_size'] + 2*params['padding']) // params['stride'] + 1
    #             height = (height - params['kernel_size'] + 2*params['padding']) // params['stride'] + 1
    #             channels = params['out_channels']
    #         elif layer_type == 'MaxPool2d' or layer_type == 'AvgPool2d':
    #             width = (width - params['kernel_size']) // params['stride'] + 1
    #             height = (height - params['kernel_size']) // params['stride'] + 1
    #         elif layer_type == 'Linear':
    #             if not flattened:
    #                 flattened = True
    #                 flatten = {
    #                     'type': 'Flatten',
    #                     'params': {
    #                         'start_dim': 0,
    #                         'end_dim': -1
    #                     }
    #                 }
    #                 if i > 0 and self.architecture['layers'][i-1]['type'] == 'Flatten':
    #                     self.architecture['layers'][i-1]['params'] = flatten['params']
    #                 else:
    #                     self.create_layer_node(flatten, i)
    #                     self.add_layer_name(flatten, layer_freqs)
    #                     i+=1
    #             if features_after_1st_FC is not None:
    #                 params['in_features'] = features_after_1st_FC
    #             else:
    #                 params['in_features'] = int(channels * width * height)
    #             features_after_1st_FC = params['out_features']
    #         elif layer_type == 'BatchNorm2d':
    #             params['num_features'] = channels
    #         elif layer_type == 'Flatten':
    #             if params['start_dim'] == 0 and params['end_dim'] == -1:
    #                 flattened = True
    #         i+=1







        # self.architecture['misc_params']['width'] = int(self.inputWidth_QLineEdit.text())
        # self.architecture['misc_params']['height'] = int(self.inputHeight_QLineEdit.text())
        # if self.inputType_RGB_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 3
        # elif self.inputType_grayScale_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 1

        # self.architecture['misc_params']['batch_size'] = int(self.batchSize_QLineEdit.text())
        # self.architecture['misc_params']['num_epochs'] = int(self.numEpochs_QLineEdit.text())
        # self.architecture['misc_params']['optimizer'] = self.selected_optimizer
        # self.architecture['misc_params']['loss_func'] = self.selected_lossfunc

        # with open(to_absolute(arch_json_path), 'w') as f:
        #     f.write(json.dumps(self.architecture, indent=2))

    


