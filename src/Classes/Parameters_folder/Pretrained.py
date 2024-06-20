from PySide6.QtWidgets import QLineEdit, QSpinBox, QComboBox, QPushButton
from utils.AutoExtraction import AutoExtraction
from Classes.Children import Children
from Qt.WidgetData import WidgetData
from Qt.Dialogue import LayerDialog
from Classes.Parameters_folder.Miscellaneous import Miscellaneous
import torchvision


class Pretrained:

    def __init__(self) -> None:
        self.Children = Children()
        self.Miscellaneous = Miscellaneous()
        self.LayerDialog = LayerDialog()
        self.PRETRAINED_MODELS = AutoExtraction().PRETRAINED_MODELS
        self.WidgetUtility = WidgetData()
        self.fill_pretrained_model()
        self.Children.qt_pretrained_model_combobox.currentIndexChanged.connect(
            self.on_combobox_change
        )
        self.pretrained = {
            "value": self.Children.qt_pretrained_model_combobox.currentText(),
            "index": self.Children.qt_pretrained_model_combobox.currentIndex()
        }

        self.selected_pretrained_model = self.Children.qt_pretrained_model_combobox.currentText()

    def get_min_size(self, model_name):
        min_size = torchvision.models.get_model_weights(
            torchvision.models.__dict__[model_name]).DEFAULT.meta['min_size']
        return min_size

    def on_combobox_change(self):
        self.pretrained = {
            "value": self.Children.qt_pretrained_model_combobox.currentText(),
            "index": self.Children.qt_pretrained_model_combobox.currentIndex()
        }
        
        Height, Width = self.get_min_size(self.pretrained["value"])
        if Height > self.Miscellaneous.miscellaneous['height']:
            self.Miscellaneous.miscellaneous_params['height'].setValue(Height)
        if Width > self.Miscellaneous.miscellaneous['width']:
            self.Miscellaneous.miscellaneous_params['width'].setValue(Width)

    def load_from_config(self, json_data: dict):
        if len(json_data["pretrained"]) != 0:
            self.Children.qt_pretrained_model_combobox.setCurrentIndex(
                json_data['pretrained']['index']
            )

    def fill_pretrained_model(self):
        for i in self.PRETRAINED_MODELS:
            self.Children.qt_pretrained_model_combobox.addItem(i, i)
