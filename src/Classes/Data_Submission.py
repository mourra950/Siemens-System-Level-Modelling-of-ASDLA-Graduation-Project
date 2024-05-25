import json
import os
from PySide6.QtWidgets import (
    QMessageBox,
    QLineEdit,
    QSpinBox,
    QFileDialog
)
from PySide6.QtCore import QProcess
from jinja2 import Environment, FileSystemLoader
from cookiecutter.main import cookiecutter

basedir = os.path.dirname(__file__)


class DataSubmission:
    def __init__(self) -> None:
        self.set_data_onChange('width', self.qt_inputWidth_QSpinBox)
        self.set_data_onChange('height', self.qt_inputHeight_QSpinBox)
        self.set_data_onChange('channels',  self.qt_inputType_QSpinBox)
        self.set_data_onChange('batch_size', self.qt_batchSize_QSpinBox)
        self.set_data_onChange('num_epochs', self.qt_numEpochs_QSpinBox)
        # self.qt_manual_generate.clicked.connect(self.manual_generate)

    def set_data_onChange(self, param_name, widget):
        if (type(widget) == QSpinBox):
            widget.valueChanged.connect(
                lambda: self.fetch_data_params(param_name, widget))
        elif (type(widget) == QLineEdit):
            widget.textChanged.connect(
                lambda: self.fetch_data_params(param_name, widget))

    def on_submit_params_clicked(self):
        self.save_json()

    def fetch_data_params(self, param_name, widget):
        try:
            if (type(widget) == QSpinBox):
                self.architecture['misc_params'][param_name] = widget.value()
                print(widget.value(), param_name)
            elif (type(widget) == QLineEdit):
                self.architecture['misc_params'][param_name] = widget.text()
                print(widget.text(), param_name)
        except:
            print(f"error in {param_name}")

    def on_submit_arch_clicked(self):
        self.validate_and_correct_layers(
            self.qt_addedLayers_QVBoxLayout, self.architecture)
        arch_json_file_path = self.save_json()


    def generate_arch(self):
        arch_json_file_path, _ = QFileDialog.getOpenFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )
        self.generate_manual_project()

    def handle_stderr(self):
        result = bytes(
            self.Manual_Process.readAllStandardError()).decode("utf8")
        print(result)

    def handle_stdout(self):
        result = bytes(
            self.Manual_Process.readAllStandardOutput()).decode("utf8")
        print(result)

    def generate_manual_project(self):
        path_output = self.Cookiecutter.render_cookiecutter_template(
            self.manual_jinja_json,  self.manual_cookie_json, self.manual_template_dir
        )
        if path_output:
            self.Manual_Process = QProcess()
            self.Manual_Process.readyReadStandardOutput.connect(
                self.handle_stdout)
            self.Manual_Process.readyReadStandardError.connect(
                self.handle_stderr)
            self.Manual_Process.start(
                "python", [path_output+"/Manual_Output/main.py"])

    def on_submit_layer_clicked(self, layer_type, params_names, params_value_widgets, paramsWindow_QDialog, qt_layout, arch_dict):
        # Initialize message error box
        dlg = QMessageBox()
        dlg.setWindowTitle("error!")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)
        # mourra look at that
        # self.count+=1
        layer = {
            'type': layer_type,
            'params': dict(),
            # 'name':self.count
        }

        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])
            if param_value != '':
                layer['params'][params_names[i]] = param_value
        # cond=self.test_layer(layer_type, params_names, params_value_widgets)
        cond = True
        if cond:
            self.create_layer_node(layer, -1, qt_layout, arch_dict)    
            paramsWindow_QDialog.close()

    # save json for manual arch
    def save_json(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON File", self.basedir, "JSON Files (*.json)")
        if path:
            self.architecture["mnist_path"] = self.mnist_path
            self.architecture["log_dir"] = self.log_path
            # test for deep and shallow to avoid errors
            architecture = self.architecture.copy()
            self.StaticAnalysis.analyze(self.architecture["layers"])
            architecture["layers"] = {"list": self.architecture["layers"]}

            with open(path, 'w') as f:
                f.write(json.dumps(architecture, indent=4))
            print("JSON file saved successfully.")

        return path
