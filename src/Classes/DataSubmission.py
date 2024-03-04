import json



class DataSubmission:
    def on_submit_params_clicked(self):
        print("ana weselt")
        self.architecture['misc_params']['width'] = int(
            self.inputWidth_QLineEdit.text())
        self.architecture['misc_params']['height'] = int(
            self.inputHeight_QLineEdit.text())
        # mourra law sama7t kamel le3b fee el zarayer dih
        # if self.inputType_RGB_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 3
        # elif self.inputType_grayScale_QRadioButton.isChecked():
        #     self.architecture['misc_params']['channels'] = 1

        self.architecture['misc_params']['batch_size'] = int(
            self.batchSize_QLineEdit.text())
        self.architecture['misc_params']['num_epochs'] = int(
            self.numEpochs_QLineEdit.text())
        self.architecture['misc_params']['optimizer'] = self.selected_optimizer
        self.architecture['misc_params']['loss_func'] = self.selected_lossfunc

        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))

    def on_submit_arch_clicked(self):
        print("ana weselt")
        self.validate_and_correct_layers(self.architecture)
        #et2aked eno beycareate
        with open(self.arch_json_path, 'w') as f:
            f.write(json.dumps(self.architecture, indent=2))
