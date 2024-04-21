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
        self.pretrained_model_combobox = self.ui.findChild(
            QComboBox, "Pretrained_model_ComboBox"
        )
        self.selected_pretrained_model = None
        self.pretrained_model_combobox.currentIndexChanged.connect(
            self.on_combobox_change
        )

    def on_combobox_change(self):
        # Save the selected value in a variable
        self.selected_pretrained_model = self.pretrained_model_combobox.currentText()

        # choose Json File
        self.path = ""
        # self.ui = loader.load(os.path.join(basedir, "MainWindow.ui"), None)
        # self.ui.setWindowTitle("Testing File Picker")

        self.Create_transfer_Model_QPushButton = self.ui.findChild(
            QPushButton, "Create_transfer_Model_QPushButton"
        )

        self.Create_transfer_Model_QPushButton.clicked.connect(self.getFile)

        # self.ui.show()

    def getFile(self):
        path, _ = QFileDialog.getOpenFileName(
            None, "Open file", basedir, "JSON Files (*.json)"
        )
        self.path = Path(path)
        # If a file was selected, save the file path
        if path:
            return path

    # Render Json File Data
    template_dir = "./templates"

    env = Environment(loader=FileSystemLoader(template_dir))

    template_filename = "pretrained.py.jinja"
    template = env.get_template(template_filename)

    json_file_path = getFile()

    if json_file_path:

        with open(json_file_path, "r") as json_file:
            data = json.load(json_file)
        result_file = template.render(
            layers=data["layers"], misc_params=data["misc_params"]
        )
