from utils.Cookiecutter import Cookiecutter
import os
from PySide6.QtWidgets import QPushButton, QFileDialog, QComboBox
from PySide6.QtCore import QProcess
from PySide6.QtUiTools import QUiLoader
import cookiecutter.main
import cookiecutter.prompt
import torchvision
from torchvision import models
from jinja2 import Environment, FileSystemLoader
import json
import collections
from cookiecutter.main import cookiecutter
basedir = os.path.dirname(__file__)
loader = QUiLoader()


class DataOfTransfer:
    def __init__(self):
        self.selected_pretrained_model = self.Children.qt_pretrained_model_combobox.currentText()

    def on_combobox_change(self):
        self.selected_pretrained_model = self.Children.qt_pretrained_model_combobox.currentText()

    def get_min_size(self, model_name):
        min_size = torchvision.models.get_model_weights(
            models.__dict__[model_name]).DEFAULT.meta['min_size']
        return min_size

    def save_json_transfer(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON file", self.SysPath.jsondir, "JSON Files (*.json)"
        )

        self.architecture["transfer_model"] = self.selected_pretrained_model
        Height, Width = self.get_min_size(self.selected_pretrained_model)
        if Height > self.architecture["misc_params"]["height"]:
            self.architecture["misc_params"]["height"] = Height
        if Width > self.architecture["misc_params"]["width"]:
            self.architecture["misc_params"]["width"] = Width
        self.architecture["log_dir"] = self.SysPath.log_path
        try:
            self.architecture["misc_params"]["device_index"] = int(self.architecture["misc_params"]["device"].split(":")[
                1])
        except:
            print('cpu')
        if path:
            self.SysPath.jsondir = path
            with open(path, 'w') as f:
                f.write(json.dumps(self.architecture, indent=4))
            print("JSON file saved successfully.")

    # Render Json File Data

    def render_transfer_learning(self):
        path_output = self.Cookiecutter.render_cookiecutter_template(
            self.SysPath.transfer_jinja_json, self.SysPath.transfer_cookie_json, self.SysPath.transfer_template_dir
        )

        if path_output:
            try:
                self.show_files(path_output)
            except:
                if self.debug:
                    print("ERRORRRRR")
            self.Pretrained_Process = QProcess()
            self.Pretrained_Process.readyReadStandardOutput.connect(
                self.handle_stdout_transfer_learning)
            self.Pretrained_Process.readyReadStandardError.connect(
                self.handle_stderr_transfer_learning)
            self.Pretrained_Process.start(
                "python", [path_output+"/Pretrained_Output/main.py"])

    def handle_stderr_transfer_learning(self):
        result = bytes(
            self.Pretrained_Process.readAllStandardError()).decode("utf8")
        print(result)

    def handle_stdout_transfer_learning(self):
        result = bytes(
            self.Pretrained_Process.readAllStandardOutput()).decode("utf8")
        print(result)
