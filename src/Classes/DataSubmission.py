import json
import torch
from PySide6.QtWidgets import (
   QDialog,QMessageBox,QLineEdit
)

class DataSubmission:
    def on_submit_params_clicked(self):
        print("ana weselt params")
        # t=QLineEdit()
        # t.text
        self.architecture['misc_params']['width'] = int(
            self.qt_inputWidth_QLineEdit.text())
        self.architecture['misc_params']['height'] = int(
            self.qt_inputHeight_QLineEdit.text())
        # mourra law sama7t kamel le3b fee el zarayer dih
        # if self.inputType_RGB_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 3
        # elif self.inputType_grayScale_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 1

        self.architecture['misc_params']['batch_size'] = int(
            self.qt_batchSize_QLineEdit.text())
        self.architecture['misc_params']['num_epochs'] = int(
            self.qt_numEpochs_QLineEdit.text())
        self.architecture['misc_params']['optimizer'] = self.selected_optimizer
        self.architecture['misc_params']['loss_func'] = self.selected_lossfunc

        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))

    def on_submit_arch_clicked(self):
        print("ana weselt arch")
        self.validate_and_correct_layers(self.architecture)
        #et2aked eno beycareate
        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))

    def on_submit_layer_clicked(self, layer_type, params_names, params_value_widgets, paramsWindow_QDialog,qt_layout, arch_dict):
        #Initialize message error box
        dlg = QMessageBox()
        dlg.setWindowTitle("error!")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)
       
        tempstring=f"torch.nn.{layer_type}("
        layer = {
            'type': layer_type,
            'params': dict()
        }
        
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])
            if param_value != '':
                tempstring+=f"{params_names[i]}={param_value},"
                # print(layer['params'],params_names[i],param_value,layer_type)
                layer['params'][params_names[i]] = param_value
        tempstring+=")"
        print(tempstring)
        try:
            exec(tempstring)
        except Exception as e:
            # print(type(str(e)))
            print("error",e)
            dlg.setText(str(e))
            dlg.exec()
        self.create_layer_node(layer, -1,qt_layout, arch_dict)
        paramsWindow_QDialog.close()
            
        
