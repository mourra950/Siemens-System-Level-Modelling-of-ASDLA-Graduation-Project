from utils.Cookiecutter import Cookiecutter
import os
from PySide6.QtWidgets import QPushButton, QFileDialog, QComboBox
from PySide6.QtCore import QProcess
from PySide6.QtUiTools import QUiLoader
import cookiecutter.main
import cookiecutter.prompt
from jinja2 import Environment, FileSystemLoader
import json
import collections
from cookiecutter.main import cookiecutter
basedir = os.path.dirname(__file__)
loader = QUiLoader()


class DataOfTransfer:
    def __init__(self):
        self.selected_pretrained_model = self.pretrained_model_combobox.currentText()

    def on_combobox_change(self):
        self.selected_pretrained_model = self.pretrained_model_combobox.currentText()

    def save_json_transfer(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )
        print("tata")
        self.architecture["transfer_model"] = self.selected_pretrained_model
        self.architecture["mnist_path"] = self.mnist_path
        self.architecture["log_dir"] = self.log_path

        if path:
            with open(path, 'w') as f:
                f.write(json.dumps(self.architecture, indent=4))
            print("JSON file saved successfully.")

    # Render Json File Data

    def render_transfer_learning(self):
        path_output = self.Cookiecutter.render_cookiecutter_template(
            self.transfer_jinja_json, self.transfer_cookie_json, self.transfer_template_dir
        )

        if path_output:
            ###########################
            # Mourra uncomment and test
            ###########################
            # try:
            #     self.show_files(path_output)
            # except:
            #     print("ERRORRRRR")
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
