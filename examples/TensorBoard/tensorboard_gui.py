import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from tensorboard import program
import threading


# Function to run TensorBoard in a separate thread
def run_tensorboard(logdir):
    tb = program.TensorBoard()
    tb.configure(argv=[None, "--logdir", logdir])
    url = tb.launch()
    sys.stdout.write(f"TensorBoard started at {url}\n")
    sys.stdout.flush()


# PyQt6 GUI class
class TensorBoardGUI(QMainWindow):
    def __init__(self, logdir):
        super(TensorBoardGUI, self).__init__()

        self.logdir = logdir

        self.setWindowTitle("TensorBoard GUI")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.start_tensorboard_button = QPushButton("Start TensorBoard", self)
        self.start_tensorboard_button.clicked.connect(self.start_tensorboard)
        self.layout.addWidget(self.start_tensorboard_button)

    def start_tensorboard(self):
        # Start TensorBoard in a separate thread
        threading.Thread(
            target=run_tensorboard, args=(self.logdir,), daemon=True
        ).start()


if __name__ == "__main__":
    # Set the path to your TensorBoard log directory
    log_directory = "./logs"

    app = QApplication(sys.argv)
    main_window = TensorBoardGUI(log_directory)
    main_window.show()
    sys.exit(app.exec())


# import os
# import sys
# from PyQt6.QtCore import Qt, QProcess
# from PyQt6.QtWidgets import (
#     QApplication,
#     QMainWindow,
#     QVBoxLayout,
#     QWidget,
#     QPushButton,
#     QLabel,
# )


# class TensorBoardGUI(QMainWindow):
#     def __init__(self, tensorboard_logdir):
#         super().__init__()

#         self.tensorboard_logdir = tensorboard_logdir
#         self.tensorboard_process = None  # Added to track TensorBoard process

#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("TensorBoard GUI")

#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         layout = QVBoxLayout(self.central_widget)

#         self.start_tensorboard_button = QPushButton("Start TensorBoard", self)
#         self.start_tensorboard_button.clicked.connect(self.startTensorBoard)
#         layout.addWidget(self.start_tensorboard_button)

#         self.status_label = QLabel("TensorBoard Status: Not Running", self)
#         layout.addWidget(self.status_label)

#     def startTensorBoard(self):
#         tensorboard_command = ["tensorboard", "--logdir", self.tensorboard_logdir]
#         self.tensorboard_process = QProcess(self)
#         self.tensorboard_process.started.connect(self.tensorBoardStarted)
#         self.tensorboard_process.start("tensorboard", tensorboard_command)

#     def tensorBoardStarted(self):
#         self.status_label.setText("TensorBoard Status: Running")
#         local_host_link = "http://localhost:6006/"  # You can adjust the port if needed
#         print(
#             f"TensorBoard is running. Open the following link in your browser:\n{local_host_link}"
#         )

#     def closeEvent(self, event):
#         # Terminate TensorBoard process when closing the GUI
#         if (
#             self.tensorboard_process
#             and self.tensorboard_process.state() == QProcess.ProcessState.Running
#         ):
#             self.tensorboard_process.terminate()


# def run_tensorboard_gui():
#     current_folder = os.path.abspath(os.path.dirname(__file__))
#     tensorboard_logdir = os.path.join(current_folder, "logs")

#     app = QApplication(sys.argv)
#     mainWin = TensorBoardGUI(tensorboard_logdir)
#     mainWin.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     run_tensorboard_gui()
