from PySide6.QtWidgets import QVBoxLayout, QProgressBar
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, QProcess, QTimer


class TensorView:
    def __init__(self) -> None:
        self.Tensorboard_Process = QProcess()
        self.Tensorboard_Process.start("tensorboard", ["--logdir", self.log_path])

        self.reload_timer = QTimer()
        self.progress_timer = QTimer()
        self.setup_timers()

        # get the tensorboard object from the ui
        self.tensorQt = self.ui.findChild(QVBoxLayout, "TensorView")
        # create and add the webview object qt
        self.tensorWeb = QWebEngineView()
        self.tensorQt.addWidget(self.tensorWeb)
        self.tensorWeb.setUrl(QUrl("http://localhost:6006/"))
        self.tensorWeb.hide()

        # Initialize progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        self.progress_bar.setStyleSheet(
            """
            QProgressBar {
                border: 2px solid grey;
                border-radius: 5px;
                text-align: center;
            }

            QProgressBar::chunk {
                background-color: orange;
                width: 20px;
            }
        """
        )
        self.tensorQt.addWidget(self.progress_bar)

    def setup_timers(self):
        self.reload_timer.setSingleShot(True)
        self.reload_timer.timeout.connect(self.first_reload)
        self.reload_timer.start(10000)  # Reload once after 10 seconds

        self.progress_timer.setInterval(
            250
        )  # Set interval to 500 milliseconds (0.5 seconds)
        self.progress_timer.timeout.connect(self.increment_progress_bar)
        self.progress_timer.start()

    def first_reload(self):
        self.tensorWeb.reload()

    def update_progress_bar(self, progress):
        print(progress)
        if progress == 100:
            self.progress_bar.hide()
            self.tensorWeb.show()

    def increment_progress_bar(self):
        current_value = self.progress_bar.value()
        if current_value < 100:
            self.progress_bar.setValue(current_value + 1)
        else:
            self.progress_timer.stop()
            self.tensorWeb.show()
