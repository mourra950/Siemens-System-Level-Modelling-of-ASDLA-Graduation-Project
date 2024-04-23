import json
from PySide6.QtWidgets import (
    QMessageBox,
    QLineEdit,
    QSpinBox,
    QFileDialog
)


class DataSubmission:
    # def __init__(self) -> None:
    #     self.set_data_onChange('width', self.qt_inputWidth_QSpinBox)
    #     self.set_data_onChange('height', self.qt_inputHeight_QSpinBox)
    #     self.set_data_onChange('channels',  self.qt_inputType_QSpinBox)
    #     self.set_data_onChange('batch_size', self.qt_batchSize_QSpinBox)
    #     self.set_data_onChange('num_epochs', self.qt_numEpochs_QSpinBox)
    #     self.set_data_onChange('width', self.qt_inputWidth_QSpinBox)
    #     self.architecture['misc_params']['optimizer'] = self.selected_optimizer
    #     self.architecture['misc_params']['loss_func'] = self.selected_lossfunc
    #     self.save_json()
    # def set_data_onChange( param_name, widget):
    #     t=QSpinBox()
    #     t.connect.
    #     widget.on
        
    def on_submit_params_clicked(self):
        self.fetch_data_params('width', self.qt_inputWidth_QSpinBox)
        self.fetch_data_params('height', self.qt_inputHeight_QSpinBox)
        self.fetch_data_params('channels',  self.qt_inputType_QSpinBox)
        self.fetch_data_params('batch_size', self.qt_batchSize_QSpinBox)
        self.fetch_data_params('num_epochs', self.qt_numEpochs_QSpinBox)
        self.fetch_data_params('width', self.qt_inputWidth_QSpinBox)
        self.architecture['misc_params']['optimizer'] = self.selected_optimizer
        self.architecture['misc_params']['loss_func'] = self.selected_lossfunc
        self.save_json()

    def fetch_data_params(self, param_name, widget):
        try:
            if (type(widget) == QSpinBox):
                self.architecture['misc_params'][param_name] = widget.value()
            elif (type(widget) == QLineEdit):
                self.architecture['misc_params'][param_name] = widget.text()
        except:
            print(f"error in {param_name}")

    def on_submit_arch_clicked(self):
        self.validate_and_correct_layers(self.architecture)
        self.save_json()

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
            print("error", e)
            dlg.setText(str(e))
            dlg.exec()
        self.create_layer_node(layer, -1, qt_layout, arch_dict)
        paramsWindow_QDialog.close()

    def save_json(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON File", self.basedir, "JSON Files (*.json)")
        if path:
            with open(path, 'w') as f:
                f.write(json.dumps(self.architecture, indent=2))
            print("JSON file saved successfully.")
