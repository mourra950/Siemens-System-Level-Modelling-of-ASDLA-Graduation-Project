import json
import torch
from PySide6.QtWidgets import (
    QDialog, QMessageBox, QLineEdit, QSpinBox
)


class DataSubmission:

    def on_submit_params_clicked(self):
        self.fetch_data_params('width', self.qt_inputWidth_QSpinBox)
        self.fetch_data_params('height', self.qt_inputHeight_QSpinBox)
        self.fetch_data_params('channels',  self.qt_inputType_QSpinBox)
        self.fetch_data_params('batch_size', self.qt_batchSize_QSpinBox)
        self.fetch_data_params('num_epochs', self.qt_numEpochs_QSpinBox)
        self.fetch_data_params('width', self.qt_inputWidth_QSpinBox)
        self.architecture['misc_params']['optimizer'] = self.selected_optimizer
        self.architecture['misc_params']['loss_func'] = self.selected_lossfunc

        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))

    def fetch_data_params(self, param_name, widget):
        try:
            if (type(widget) == QSpinBox):
                self.architecture['misc_params'][param_name] = widget.value()
            elif (type(widget) == QLineEdit):
                self.architecture['misc_params'][param_name] = widget.text()
        except:
            print(f"error in {param_name}")
        ...

    def on_submit_arch_clicked(self):
        print("ana weselt arch")
        self.validate_and_correct_layers(self.architecture)
        # et2aked eno beycareate
        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))

    def on_submit_layer_clicked(self, layer_type, params_names, params_value_widgets, paramsWindow_QDialog, qt_layout, arch_dict):
        # Initialize message error box
        dlg = QMessageBox()
        dlg.setWindowTitle("error!")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)

        tempstring = f"torch.nn.{layer_type}("
        layer = {
            'type': layer_type,
            'params': dict()
        }

        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])
            if param_value != '':
                tempstring += f"{params_names[i]}={param_value},"
                # print(layer['params'],params_names[i],param_value,layer_type)
                layer['params'][params_names[i]] = param_value
        tempstring += ")"
        print(tempstring)
        try:
            exec(tempstring)
        except Exception as e:
            # print(type(str(e)))
            print("error", e)
            dlg.setText(str(e))
            dlg.exec()
        self.create_layer_node(layer, -1, qt_layout, arch_dict)
        paramsWindow_QDialog.close()
