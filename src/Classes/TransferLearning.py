import os
from PySide6.QtWidgets import QPushButton, QFileDialog, QComboBox
from pathlib import Path
from PySide6.QtUiTools import QUiLoader
from jinja2 import Environment, FileSystemLoader
import json


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
        self.architecture["transfer_model"] = self.selected_pretrained_model
        if path:
            with open(path, 'w') as f:
                f.write(json.dumps(self.architecture, indent=2))
            print("JSON file saved successfully.")


    # Render Json File Data
    def render_transfer_learning(self):
        env = Environment(loader=FileSystemLoader(self.jinja_templates))

        template_filename = "pretrained.py.jinja"
        template = env.get_template(template_filename)

        path, _ = QFileDialog.getOpenFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )

        if path:
            data=None
            with open(path, "r") as json_file:
                data = json.load(json_file)
                print(data)
                print(type(data))
                
            result_file = template.render(
                layers=data["layers"],
                misc_params=data["misc_params"],
                transfer_model=data["transfer_model"],
            )

        # Create or overwrite a file named train.py in output file and outputs the result from the rendered jinja template
        save_path = QFileDialog.getExistingDirectory(
            None, "Pick a folder to save the output", basedir
        )
        print(save_path)
        with open(save_path+"/Test.py", "w+") as Output:
            Output.write(result_file)
