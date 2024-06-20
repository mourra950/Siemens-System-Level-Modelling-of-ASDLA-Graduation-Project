import subprocess
import threading
from PySide6.QtWidgets import QMessageBox, QSpinBox, QFileDialog, QLineEdit, QComboBox
from PySide6.QtGui import QAction
import json
message = ""


class Connections:
    def __init__(self) -> None:
        self.Children.qt_submitParams_QPushButton.clicked.connect(
            self.on_submit_params_clicked)

        self.Children.qt_submitArch_QPushButton.clicked.connect(
            self.on_submit_params_clicked)

        self.Children.qt_manual_generate.clicked.connect(
            self.generate_manual_project)

        self.Children.qt_Create_transfer_Model_QPushButton.clicked.connect(
            self.on_submit_params_clicked
        )
        self.Children.qt_Create_transfer_learning_model_QPushButton.clicked.connect(
            self.render_transfer_learning
        )
        self.Children.qt_selectedDevice_QComboBox.currentIndexChanged.connect(
            self.fill_cuda_devices(self.Children.qt_selectedDevice_QComboBox)
        )
        self.Children.qt_dataset_path_QPushButton.clicked.connect(
            self.on_dataset_path_clicked
        )
        self.Children.qt_Log_Directory_btn.clicked.connect(
            self.on_log_dir_clicked)

    def set_data_load(self, param_name, widget, new_value):
        self.connections[param_name] = widget
        if type(widget) == QSpinBox:
            widget.valueChanged.connect(
                lambda: self.fetch_data_params(param_name, widget)
            )
        elif type(widget) == QLineEdit:
            widget.textChanged.connect(
                lambda: self.fetch_data_params(param_name, widget)
            )

        elif type(widget) == QComboBox:
            widget.currentIndexChanged.connect(
                lambda: self.fetch_data_params(param_name, widget)
            )

    def on_log_dir_clicked(self):
        path = QFileDialog.getExistingDirectory(
            None, "Select a Directory")
        if path:
            self.Children.qt_logdirlineedit.setText(path)

    def on_dataset_path_clicked(self):
        path = QFileDialog.getExistingDirectory(
            None, "Select a Directory")
        if path:
            self.Children.qt_dataset_path_QLineEdit.setText(path)
