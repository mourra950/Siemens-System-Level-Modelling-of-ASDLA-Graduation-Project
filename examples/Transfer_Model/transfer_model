import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, transforms, datasets
from torch.utils.data import DataLoader
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


# Define a simple dataset for demonstration purposes
class CustomDataset:
    def __init__(self, data, labels, transform=None):
        self.data = data
        self.labels = labels
        self.transform = transform

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        sample = {"image": self.data[idx], "label": self.labels[idx]}

        if self.transform:
            sample["image"] = self.transform(sample["image"])

        return sample


# Simple ResNet model modification
def modify_resnet_model(num_classes):
    resnet_model = models.resnet50(pretrained=True)

    for param in resnet_model.parameters():
        param.requires_grad = False

    resnet_model.fc = nn.Sequential(
        nn.Linear(resnet_model.fc.in_features, 256),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(256, num_classes),
    )

    return resnet_model


# GUI class for getting user input
class TransferLearningGUI(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize variables to store user input
        self.num_classes = None
        self.learning_rate = None
        self.num_epochs = None
        self.data_path = None

        # Initialize the GUI
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Input field for number of classes
        label1 = QLabel("Number of Classes:")
        self.classes_input = QLineEdit(self)
        layout.addWidget(label1)
        layout.addWidget(self.classes_input)

        # Input field for learning rate
        label2 = QLabel("Learning Rate:")
        self.lr_input = QLineEdit(self)
        layout.addWidget(label2)
        layout.addWidget(self.lr_input)

        # Input field for number of epochs
        label3 = QLabel("Number of Epochs:")
        self.epochs_input = QLineEdit(self)
        layout.addWidget(label3)
        layout.addWidget(self.epochs_input)

        # Button to select MINISET directory
        btn_select_data = QPushButton("Select MINISET Directory", self)
        btn_select_data.clicked.connect(self.show_dialog)
        layout.addWidget(btn_select_data)

        # Button to initiate training
        btn_train = QPushButton("Train", self)
        btn_train.clicked.connect(self.train_model)
        layout.addWidget(btn_train)

        self.setLayout(layout)

    def show_dialog(self):
        # Open a file dialog to select the MINISET directory
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec():
            self.data_path = dialog.selectedFiles()[0]

    def train_model(self):
        try:
            # Retrieve user input from GUI
            self.num_classes = int(self.classes_input.text())
            self.learning_rate = float(self.lr_input.text())
            self.num_epochs = int(self.epochs_input.text())

            # Define data transformations
            transform = transforms.Compose(
                [
                    transforms.Resize((224, 224)),
                    transforms.ToTensor(),
                ]
            )

            # Create an instance of MNIST for MNIST dataset
            miniset_dataset = datasets.MNIST(
                root=self.data_path, train=True, download=True, transform=transform
            )
            train_data_loader = DataLoader(miniset_dataset, batch_size=32, shuffle=True)

            # Modify the ResNet model
            resnet_model = modify_resnet_model(self.num_classes)

            # Define loss function and optimizer
            criterion = nn.CrossEntropyLoss()
            optimizer = optim.Adam(resnet_model.fc.parameters(), lr=self.learning_rate)

            # Move the model to GPU if available
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            resnet_model = resnet_model.to(device)

            # Training loop
            for epoch in range(self.num_epochs):
                for inputs, labels in train_data_loader:
                    inputs, labels = inputs.to(device), labels.to(device)

                    optimizer.zero_grad()

                    outputs = resnet_model(inputs)
                    loss = criterion(outputs, labels)
                    loss.backward()
                    optimizer.step()

                print(f"Epoch {epoch + 1}/{self.num_epochs}, Loss: {loss.item()}")

            print("Training complete!")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Start the PyQt application
    app = QApplication([])
    window = TransferLearningGUI()
    window.show()
    app.exec()


"""
def modify_resnet_model(num_classes):
    resnet_model = models.resnet50(pretrained=True)

    # Change the first convolutional layer to accept 1 channel
    resnet_model.conv1 = nn.Conv2d(1, 64, kernel_size=(7, 7), stride=(2, 2), padding=(3, 3), bias=False)

    for param in resnet_model.parameters():
        param.requires_grad = False

    resnet_model.fc = nn.Sequential(
        nn.Linear(resnet_model.fc.in_features, 256),
        nn.ReLU(),
        nn.Dropout(0.5),
        nn.Linear(256, num_classes)
    )

    return resnet_model

"""
