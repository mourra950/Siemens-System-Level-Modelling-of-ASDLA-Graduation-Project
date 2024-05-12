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
        env = Environment(loader=FileSystemLoader(self.jinja_templates))

        template_filename = "pretrained.py.jinja"
        template = env.get_template(template_filename)

        path_json, _ = QFileDialog.getOpenFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )

        if path_json:
            data = None
            with open(path_json, "r") as json_file:
                data = json.load(json_file)
            path_output = QFileDialog.getExistingDirectory(
                None, "Pick a folder to save the output", basedir
            )
            data = self.cookicutterpreproccess(data,self.transfer_cookie_json)
            self.generate_project(
                self.transfer_template_dir, path_output, data)

            self.Pretrained_Process = QProcess()
            self.Pretrained_Process.readyReadStandardOutput.connect(
                self.handle_stdout)
            self.Pretrained_Process.readyReadStandardError.connect(
                self.handle_stderr)
            self.Pretrained_Process.start(
                "python", [path_output+"/Pretrained_Output/main.py"])

    # def train_transfer_model(self):
        # path, _ = QFileDialog.getOpenFileName(
        #     None, "Save JSON file", basedir, "JSON Files (*.json)"
        # )
        # data = None

        # if path:
        #     with open(path, "r") as json_file:
        #         data = json.load(json_file)
        # # path, _ = QFileDialog.getOpenFileName(
        # #     None, "Run File", basedir, "Python (main.py)"
        # # )
        # # env = Environment(loader=FileSystemLoader(self.jinja_templates))

        # # template_filename = "cookiecutter.json.jinja"
        # # template = env.get_template(template_filename)
        # # with open("C:/Users/mourr/OneDrive/Desktop/TestJson/First Test/Test.json", "r") as json_file:
        # #     data = json.load(json_file)
        # # data = self.remove_empty_arrays(data)
        # # result_file = template.render(
        # #     my_dict=json.dumps(data, indent=4)
        # # )
        # # print(result_file)
        # # with open("E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/public/Cookiecutter/Pretrained/cookiecutter.json", "w") as json_file:
        # #     json_file.write(str(result_file))
        # self.generate_project("E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/public/Cookiecutter/Pretrained/",
        #                       "E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/public/Cookiecutter/build", data)
        # # self.test = QProcess()
        # # self.test.readyReadStandardOutput.connect(self.handle_stdout)
        # # self.test.readyReadStandardError.connect(self.handle_stderr)
        # # self.test.start("python", [
        # #                 "e:\Github\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\src\main.py"])

    def handle_stderr(self):
        result = bytes(
            self.Pretrained_Process.readAllStandardError()).decode("utf8")
        print(result)

    def handle_stdout(self):
        result = bytes(
            self.Pretrained_Process.readAllStandardOutput()).decode("utf8")
        print(result)

    def remove_empty_arrays(self, d):
        return {k: v for k, v in d.items() if v != []}

    def generate_project(self, template_path, output_path, data):
        cookiecutter(template_path, output_dir=output_path,
                     no_input=True,  overwrite_if_exists=True, extra_context=data)

    def cookicutterpreproccess(self, data,path):
        env = Environment(loader=FileSystemLoader(self.jinja_templates))

        template_filename = "cookiecutter.json.jinja"
        template = env.get_template(template_filename)

        data = self.remove_empty_arrays(data)
        result_file = template.render(
            my_dict=json.dumps(data, indent=4)
        )
        with open(path, "w") as json_file:
            json_file.write(str(result_file))
        return data
    def manual_generate(self):
        path_json, _ = QFileDialog.getOpenFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )

        if path_json:
            data = None
            with open(path_json, "r") as json_file:
                data = json.load(json_file)
            path_output = QFileDialog.getExistingDirectory(
                None, "Pick a folder to save the output", basedir
            )
            data = self.cookicutterpreproccess(data,self.manual_cookie_json)
            self.generate_project(
                self.manual_template_dir, path_output, data)

            self.Pretrained_Process = QProcess()
            self.Pretrained_Process.readyReadStandardOutput.connect(
                self.handle_stdout)
            self.Pretrained_Process.readyReadStandardError.connect(
                self.handle_stderr)
            # self.Pretrained_Process.start(
            #     "python", [path_output+"/Pretrained_Output/main.py"])
