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
        super().__init__()

        # Read chosen model

        self.selected_pretrained_model = self.pretrained_model_combobox.currentText()

    def on_combobox_change(self):
        # Save the selected value in a variable
        self.selected_pretrained_model = self.pretrained_model_combobox.currentText()
        # choose Json File
        # self.ui = loader.load(os.path.join(basedir, "MainWindow.ui"), None)
        # self.ui.setWindowTitle("Testing File Picker")

        # self.ui.show()

    def save_json_transfer(self):
        path, _ = QFileDialog.getSaveFileName(
            None, "Save JSON file", basedir, "JSON Files (*.json)"
        )
        print(self.selected_pretrained_model)
        self.architecture["transfer_model"] = self.selected_pretrained_model
        if path:
            with open(path, 'w') as f:
                f.write(json.dumps(self.architecture, indent=2))
            print("JSON file saved successfully.")

    
# Render Json File Data
def test_t(self):
    template_dir = "./templates"

    env = Environment(loader=FileSystemLoader(template_dir))

    template_filename = "pretrained.py.jinja"
    template = env.get_template(template_filename)

    json_file_path = self.getFile()

    if json_file_path:

        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        result_file = template.render(
            layers=data["layers"],
            misc_params=data["misc_params"],
            transfer_model=data["transfer_model"],
        )

    # Create or overwrite a file named train.py in output file and outputs the result from the rendered jinja template

    f = open("./output/train.py", "w")
    f.write(result_file)
    f.close()
