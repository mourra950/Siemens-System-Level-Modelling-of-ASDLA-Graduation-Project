import inspect
import torchvision.transforms as transforms
from torchvision.datasets import CIFAR10, MNIST
from torch.nn import Conv1d
from PySide6.QtWidgets import QGroupBox,QVBoxLayout,QFrame,QApplication,QScrollArea, QMainWindow, QPushButton, QLabel, QFileDialog,QListWidget,QListView
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
import os
import sys
from pathlib import Path

basedir = os.path.dirname(__file__)
loader = QUiLoader()

class MainUI(QtCore.QObject):
    def __init__(self):
        super().__init__()
        self.path=""
        self.ui = loader.load(
        os.path.join(basedir, "test.ui"), None
        )
        self.ui.setWindowTitle("Testing generating scripts")

        self.listWidget = self.ui.findChild(QListWidget,'listWidget')
        self.listview = self.ui.findChild(QListView,'listView')
        self.Area = self.ui.findChild(QScrollArea,'scrollArea')
        self.Vbox=self.ui.findChild(QVBoxLayout,'verticalLayout_6')

        testButton=QPushButton(text="Test")
        # test.addItem
        try:
            for i in range(30):
                self.listWidget.addItems(["One", "Two", "Three"])
                button = QPushButton(f"Button {i+1}")
                self.Vbox.addWidget(button)

        
        except:
            print('UNO')
        try:
            self.listview.addItems(["One", "Two", "Threee"])
        except:
            print('DOS')
        

        # for _ in range(30):
        #     self.Area.addItem(testButton)
            
        # self.pushButton1 = self.ui.findChild(QPushButton, 'pushButton1')
        # self.pushButton2 = self.ui.findChild(QPushButton, 'pushButton2')
        # self.label1 = self.ui.findChild(QLabel, 'label1')

        # self.pushButton1.clicked.connect(self.getFile)
        # self.pushButton2.clicked.connect(self.getDirectory)


        self.ui.show()



    def getFile(self):
        path,_ = QFileDialog.getOpenFileName(None,'Open file',basedir,"JSON Files (*.json)")
        self.path = Path(path)
        print(self.path)
        self.label1.setText(str(self.path))



    def getDirectory(self):
        dir_name = Path(QFileDialog.getExistingDirectory(None, "Select a Directory"))
        print(dir_name)
        self.path = dir_name
        self.label1.setText(str(self.path))


def main():
  
   app = QApplication(sys.argv)
   window = MainUI()
   app.exec()


if __name__ == '__main__':
    main()


def print_dataset_arguments(dataset_class):
    print(f"{dataset_class.__name__} dataset arguments:")
    for name, parameter in inspect.getmembers(object=dataset_class):
        if name != 'self':
            print(f"{name}: {parameter}" )

# # Example: CIFAR10
# # print_dataset_arguments(CIFAR10)
# print("===================================")
# for i in MNIST.__dict__:
#     print(i)
#     print(MNIST.__dict__[i])
# print("===================================")

# for name, parameter in inspect.signature(MNIST.__init__).parameters.items():
#     print(name)

# # Example: MNIST
# # print_dataset_arguments(MNIST)
# print("===================================")

# print(MNIST.__dict__['__parameters__'])
# # Example: Convulation

# # print_dataset_arguments(Conv1d)
# print("===================================")