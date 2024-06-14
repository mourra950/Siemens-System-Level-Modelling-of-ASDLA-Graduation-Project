import subprocess
import threading
from PySide6.QtWidgets import QMessageBox, QSpinBox

message = ""


class Connections:
    def __init__(self) -> None:
        self.qt_submitParams_QPushButton.clicked.connect(
            self.on_submit_params_clicked)

        self.qt_submitArch_QPushButton.clicked.connect(
            self.on_submit_arch_clicked)

        self.qt_manual_generate.clicked.connect(self.generate_manual_project)
        self.qt_generateFiles_QPushButton.clicked.connect(
            self.on_generate_files_clicked
        )
        self.submitRes_QPushButton.clicked.connect(
            self.res_on_submit_residual_block_clicked
        )
        self.pretrained_model_combobox.currentIndexChanged.connect(
            self.on_combobox_change
        )
        self.Create_transfer_Model_QPushButton.clicked.connect(
            self.save_json_transfer)
        self.Create_transfer_learning_model_QPushButton.clicked.connect(
            self.render_transfer_learning
        )
        self.qt_selectedDevice_QComboBox.currentIndexChanged.connect(
            self.fill_cuda_devices(self.qt_selectedDevice_QComboBox)
        )

    def testCreate(self):
        global message
        t = threading.Thread(target=self.run_systemc)
        t.start()
        t.join()
        q = QMessageBox(text=f"{message}")
        q.exec()
