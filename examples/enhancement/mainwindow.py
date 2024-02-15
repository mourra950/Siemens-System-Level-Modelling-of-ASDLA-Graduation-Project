from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import json
from util.AutoExtraction import *
from paths import *


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        uic.loadUi(main_ui_path, self)

        self.architecture = {
            'layers': [],
            'misc_params': {
                'width': 1,
                'height': 1,
                'channels': 1,
            }
        }
        self.added_layers_layouts = []

        self.inputWidth_QLineEdit = self.findChild(QLineEdit, 'inputWidth_QLineEdit')
        self.inputHeight_QLineEdit = self.findChild(QLineEdit, 'inputHeight_QLineEdit')
        self.batchSize_QLineEdit = self.findChild(QLineEdit, 'batchSize_QLineEdit')
        self.learningRate_QLineEdit = self.findChild(QLineEdit, 'learningRate_QLineEdit')
        self.numEpochs_QLineEdit = self.findChild(QLineEdit, 'numEpochs_QLineEdit')

        self.inputType_RGB_QRadioButton = self.findChild(QRadioButton, 'inputType_RGB_QRadioButton')
        self.inputType_grayScale_QRadioButton = self.findChild(QRadioButton, 'inputType_grayScale_QRadioButton')

        self.layer_QComboBox = self.findChild(QComboBox, 'layer_QComboBox')
        self.optimizer_QComboBox = self.findChild(QComboBox, 'optimizer_QComboBox')
        self.lossFunc_QComboBox = self.findChild(QComboBox, 'lossFunc_QComboBox')

        self.layer_QComboBox.addItem("Convolution")
        self.layer_QComboBox.addItem("Max Pool")
        self.layer_QComboBox.addItem("Average Pool")
        self.layer_QComboBox.addItem("Depthwise Convolution")
        self.layer_QComboBox.addItem("Flatten")
        self.layer_QComboBox.addItem("Fully Connected")

        self.optimizer_QComboBox.addItem('Adadelta')
        self.optimizer_QComboBox.addItem('Adagrad')
        self.optimizer_QComboBox.addItem('Adam')

        self.lossFunc_QComboBox.addItem('L1Loss')
        self.lossFunc_QComboBox.addItem('MSELoss')
        self.lossFunc_QComboBox.addItem('CrossEntropyLoss')
        self.lossFunc_QComboBox.addItem('NLLLoss')

        self.layersList_QVBoxLayout = self.findChild(QVBoxLayout, 'layersList_QVBoxLayout')
        self.addedLayers_QVBoxLayout = self.findChild(QVBoxLayout, 'addedLayers_QVBoxLayout')

        self.submitParams_QPushButton = self.findChild(QPushButton, 'submitParams_QPushButton')
        self.submitArch_QPushButton = self.findChild(QPushButton, 'submitArch_QPushButton')

        self.torch_layers = extract_torch_layers()
        for layer in self.torch_layers:
            selectLayer_QPushButton = QPushButton(layer)
            selectLayer_QPushButton.clicked.connect(
                lambda ch, i=layer: self.on_layer_button_clicked(i)
            )
            self.layersList_QVBoxLayout.addWidget(selectLayer_QPushButton)

        self.submitParams_QPushButton.clicked.connect(self.on_submit_params_clicked)
        self.submitArch_QPushButton.clicked.connect(self.on_submit_arch_clicked)


    def on_layer_button_clicked(self, layer_name):
        paramsWindow_QDialog = QDialog()
        paramsWindow_QDialog.setMinimumWidth(330)
        allParamsColumn_QVBoxLayout = QVBoxLayout()
        params_value_widgets = []
        params_names = []

        for param in self.torch_layers[layer_name]:            
            if param['type'] == bool:
                paramValue_QWidget = QCheckBox()
                paramValue_QWidget.setChecked(param['defaultvalue'])
            else:
                paramValue_QWidget = QLineEdit()
                if (
                    param['defaultvalue'] != inspect._empty
                    and
                    param['defaultvalue'] != None
                    and not
                    callable(param['defaultvalue'])
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
            lambda ch, i=layer_name, j=params_names, k=params_value_widgets, l=paramsWindow_QDialog \
                : self.on_submit_layer_clicked(i,j,k,l)
        )
        allParamsColumn_QVBoxLayout.addWidget(submitLayer_QPushButton)
        paramsWindow_QDialog.setLayout(allParamsColumn_QVBoxLayout)
        paramsWindow_QDialog.setWindowTitle(f"{layer_name}")
        paramsWindow_QDialog.exec()        


    def on_submit_layer_clicked(self, layer_type, params_names, params_value_widgets, paramsWindow_QDialog):
        layer = {
            'type': layer_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            if isinstance(params_value_widgets[i], QCheckBox):
                param_value = params_value_widgets[i].isChecked()
            else:
                param_value = params_value_widgets[i].text().strip()
                try:
                    param_value = int(param_value)
                except:
                    pass

            if param_value != '':
                layer['params'][params_names[i]] = param_value

        self.create_layer_node(layer, -1)
        paramsWindow_QDialog.close()


    def create_layer_node(self, layer, index):
        addedLayerRow_QHBoxLayout = QHBoxLayout()

        delete_QPushButton = QPushButton()
        delete_QPushButton.setMaximumWidth(40)
        delete_QPushButton.setIcon(QIcon(delete_icon_path))
        delete_QPushButton.clicked.connect(
            lambda ch, i=addedLayerRow_QHBoxLayout : \
                self.on_delete_layer_clicked(i)
        )
        addedLayerRow_QHBoxLayout.addWidget(QLabel(layer['type']))
        addedLayerRow_QHBoxLayout.addWidget(delete_QPushButton)

        if index == -1:
            self.addedLayers_QVBoxLayout.addLayout(addedLayerRow_QHBoxLayout)
            self.architecture['layers'].append(layer)
            self.added_layers_layouts.append(addedLayerRow_QHBoxLayout)
        else:
            self.addedLayers_QVBoxLayout.insertLayout(index, addedLayerRow_QHBoxLayout)
            self.architecture['layers'].insert(index, layer)
            self.added_layers_layouts.insert(index, addedLayerRow_QHBoxLayout)


    def on_delete_layer_clicked(self, addedLayerRow_QHBoxLayout):
        for i in range(len(self.added_layers_layouts)):
            if addedLayerRow_QHBoxLayout == self.added_layers_layouts[i]:
                self.architecture['layers'].pop(i)
                self.clearLayout(self.added_layers_layouts[i])
                self.addedLayers_QVBoxLayout.removeItem(self.added_layers_layouts[i])
                self.added_layers_layouts.pop(i)
                break


    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())


    def on_submit_arch_clicked(self):
        self.validate_and_correct_layers()
        with open(arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))


    def validate_and_correct_layers(self):
        width = self.architecture['misc_params']['width']
        height = self.architecture['misc_params']['height']
        channels = self.architecture['misc_params']['channels']
        features_after_1st_FC = None
        flattened = False
        layer_freqs = dict()
        i = 0

        while i < len(self.architecture['layers']):
            layer = self.architecture['layers'][i]
            params = layer['params']
            layer_type = layer['type']
            self.add_layer_name(layer, layer_freqs)

            if layer_type == 'Conv2d':
                params['in_channels'] = channels
                width = (width - params['kernel_size'] + 2*params['padding']) // params['stride'] + 1
                height = (height - params['kernel_size'] + 2*params['padding']) // params['stride'] + 1
                channels = params['out_channels']
            elif layer_type == 'MaxPool2d' or layer_type == 'AvgPool2d':
                width = (width - params['kernel_size']) // params['stride'] + 1
                height = (height - params['kernel_size']) // params['stride'] + 1
            elif layer_type == 'Linear':
                if not flattened:
                    flattened = True
                    flatten = {
                        'type': 'Flatten',
                        'params': {
                            'start_dim': 0,
                            'end_dim': -1
                        }
                    }
                    if i > 0 and self.architecture['layers'][i-1]['type'] == 'Flatten':
                        self.architecture['layers'][i-1]['params'] = flatten['params']
                    else:
                        self.create_layer_node(flatten, i)
                        self.add_layer_name(flatten, layer_freqs)
                        i+=1
                if features_after_1st_FC is not None:
                    params['in_features'] = features_after_1st_FC
                else:
                    params['in_features'] = int(channels * width * height)
                features_after_1st_FC = params['out_features']
            elif layer_type == 'BatchNorm2d':
                params['num_features'] = channels
            elif layer_type == 'Flatten':
                if params['start_dim'] == 0 and params['end_dim'] == -1:
                    flattened = True
            i+=1


    def add_layer_name(self, layer, layer_freqs):
        if layer['type'] in layer_freqs:
            layer_freqs[layer['type']] += 1
        else:
            layer_freqs[layer['type']] = 1
        layer['name'] = f'{layer["type"].lower()}_{layer_freqs[layer["type"]]}'


    def on_submit_params_clicked(self):
        self.architecture['misc_params']['width'] = int(self.inputWidth_QLineEdit.text())
        self.architecture['misc_params']['height'] = int(self.inputHeight_QLineEdit.text())
        if self.inputType_RGB_QRadioButton.isChecked():
            self.architecture['misc_params']['channels'] = 3
        elif self.inputType_grayScale_QRadioButton.isChecked():
            self.architecture['misc_params']['channels'] = 1

        self.architecture['misc_params']['batch_size'] = int(self.batchSize_QLineEdit.text())
        self.architecture['misc_params']['learning_rate'] = float(self.learningRate_QLineEdit.text())
        self.architecture['misc_params']['num_epochs'] = int(self.numEpochs_QLineEdit.text())
        optimizer = self.optimizer_QComboBox.currentText()
        loss_func = self.lossFunc_QComboBox.currentText()