class Connections:
    def __init__(self) -> None:
        self.qt_submitParams_QPushButton.clicked.connect(
            self.on_submit_params_clicked)
        self.qt_submitArch_QPushButton.clicked.connect(
            self.on_submit_arch_clicked)
        self.qt_generateFiles_QPushButton.clicked.connect(
            self.on_generate_files_clicked)