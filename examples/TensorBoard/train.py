# from tensorboard import summary
# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader, TensorDataset
# from torchvision.datasets import mnist
# from torchvision.transforms import ToTensor
# from torch.utils.tensorboard import SummaryWriter
# import torch.nn.functional as F


# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
#         self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
#         self.fc1 = nn.Linear(64 * 5 * 5, 128)
#         self.fc2 = nn.Linear(128, 10)

#     def forward(self, x):
#         x = F.relu(F.max_pool2d(self.conv1(x), 2))
#         x = F.relu(F.max_pool2d(self.conv2(x), 2))
#         x = x.view(-1, 64 * 5 * 5)
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x


# # Initialization
# LR = 0.001  # Set your learning rate
# BATCH_SIZE = 64  # Set your batch size
# EPOCHS = 10  # Set the number of epochs
# TRAIN_SPLIT = 0.75
# VAL_SPLIT = 0.15
# TEST_SPLIT = 0.1
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Create the model, dataloaders, optimizer, and loss function
# model = CNN()
# model.to(device)

# # Use torchsummary to print a summary of the model
# summary(model, (1, 28, 28), device="cuda" if torch.cuda.is_available() else "cpu")

# train_dataset = mnist.MNIST(
#     root="./train", train=True, download=True, transform=ToTensor()
# )
# test_dataset = mnist.MNIST(
#     root="./test", train=False, download=True, transform=ToTensor()
# )
# train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
# test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# opt = optim.Adam(model.parameters(), lr=LR)
# lossFn = nn.CrossEntropyLoss()

# # TensorBoard setup
# writer = SummaryWriter()

# # Training loop
# for e in range(0, EPOCHS):
#     model.train()
#     totalTrainLoss = 0
#     trainCorrect = 0

#     for i, (x, y) in enumerate(train_dataloader):
#         (x, y) = (x.to(device), y.to(device))

#         pred = model(x)
#         loss = lossFn(pred, y)

#         opt.zero_grad()
#         loss.backward()
#         opt.step()

#         totalTrainLoss += loss.item()
#         trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate training accuracy and loss
#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     avgTrainLoss = totalTrainLoss / len(train_dataloader)

#     # Write to TensorBoard
#     writer.add_scalar("Train/Accuracy", trainAccuracy, e)
#     writer.add_scalar("Train/Loss", avgTrainLoss, e)

#     # Visualization of final layers
#     if e == EPOCHS - 1:
#         for name, param in model.named_parameters():
#             writer.add_histogram(name, param.clone().cpu().data.numpy(), e)

#     # Evaluation on test set
#     model.eval()
#     preds = []
#     testCorrect = 0

#     with torch.no_grad():
#         for x, y in test_dataloader:
#             x = x.to(device)
#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate test accuracy
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     # Write test accuracy to TensorBoard
#     writer.add_scalar("Test/Accuracy", testAccuracy, e)

# # Save the model
# torch.save(model, "model.pt")

# # Close the TensorBoard writer
# writer.close()


# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader, TensorDataset
# from torchvision.datasets import mnist
# from torchvision.transforms import ToTensor
# from torch.utils.tensorboard import SummaryWriter
# import torchvision.models as models
# import torchvision.transforms as transforms
# from torch.autograd import Variable
# from PIL import Image
# import torchvision
# import torch.nn.functional as F


# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
#         self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
#         self.fc1 = nn.Linear(64 * 5 * 5, 128)
#         self.fc2 = nn.Linear(128, 10)

#     def forward(self, x):
#         x = F.relu(F.max_pool2d(self.conv1(x), 2))
#         x = F.relu(F.max_pool2d(self.conv2(x), 2))
#         x = x.view(-1, 64 * 5 * 5)
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x


# # Initialization
# LR = 0.001  # Set your learning rate
# BATCH_SIZE = 64  # Set your batch size
# EPOCHS = 10  # Set the number of epochs
# TRAIN_SPLIT = 0.75
# VAL_SPLIT = 0.15
# TEST_SPLIT = 0.1
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Create the model, dataloaders, optimizer, and loss function
# model = CNN()
# model.to(device)

# train_dataset = mnist.MNIST(
#     root="./train", train=True, download=True, transform=ToTensor()
# )
# test_dataset = mnist.MNIST(
#     root="./test", train=False, download=True, transform=ToTensor()
# )
# train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
# test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# opt = optim.Adam(model.parameters(), lr=LR)
# lossFn = nn.CrossEntropyLoss()

# # TensorBoard setup
# writer = SummaryWriter()

# # Training loop
# for e in range(0, EPOCHS):
#     model.train()
#     totalTrainLoss = 0
#     trainCorrect = 0

#     for i, (x, y) in enumerate(train_dataloader):
#         (x, y) = (x.to(device), y.to(device))

#         pred = model(x)
#         loss = lossFn(pred, y)

#         opt.zero_grad()
#         loss.backward()
#         opt.step()

#         totalTrainLoss += loss.item()
#         trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate training accuracy and loss
#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     avgTrainLoss = totalTrainLoss / len(train_dataloader)

#     # Write to TensorBoard
#     writer.add_scalar("Train/Accuracy", trainAccuracy, e)
#     writer.add_scalar("Train/Loss", avgTrainLoss, e)

#     # Export the model to ONNX for TensorBoard visualization
#     if e == EPOCHS - 1:
#         dummy_input = torch.randn(1, 1, 28, 28).to(device)  # Example input tensor
#         onnx_path = "model.onnx"
#         torch.onnx.export(model, dummy_input, onnx_path)
#         writer.add_graph_onnx(onnx_path)

#         # Visualize the ONNX model using netron
#         import netron

#         netron.start(onnx_path)

#     # Visualization of final layers
#     if e == EPOCHS - 1:
#         for name, param in model.named_parameters():
#             writer.add_histogram(name, param.clone().cpu().data.numpy(), e)

#     # Evaluation on test set
#     model.eval()
#     preds = []
#     testCorrect = 0

#     with torch.no_grad():
#         for x, y in test_dataloader:
#             x = x.to(device)
#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate test accuracy
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     # Write test accuracy to TensorBoard
#     writer.add_scalar("Test/Accuracy", testAccuracy, e)

# # Save the model
# torch.save(model, "model.pt")

# # Close the TensorBoard writer
# writer.close()


# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader
# from torchvision.datasets import mnist
# from torchvision.transforms import ToTensor
# from torch.utils.tensorboard import SummaryWriter
# import torch.nn.functional as F


# class CNN(nn.Module):
#     def __init__(self):
#         super(CNN, self).__init__()
#         self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
#         self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
#         self.fc1 = nn.Linear(64 * 5 * 5, 128)
#         self.fc2 = nn.Linear(128, 10)

#     def forward(self, x):
#         x = F.relu(F.max_pool2d(self.conv1(x), 2))
#         x = F.relu(F.max_pool2d(self.conv2(x), 2))
#         x = x.view(-1, 64 * 5 * 5)
#         x = F.relu(self.fc1(x))
#         x = self.fc2(x)
#         return x


# # Initialization
# LR = 0.001  # Set your learning rate
# BATCH_SIZE = 64  # Set your batch size
# EPOCHS = 10  # Set the number of epochs
# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# # Create the model, dataloaders, optimizer, and loss function
# model = CNN()
# model.to(device)

# train_dataset = mnist.MNIST(
#     root="./train", train=True, download=True, transform=ToTensor()
# )
# test_dataset = mnist.MNIST(
#     root="./test", train=False, download=True, transform=ToTensor()
# )
# train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
# test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

# opt = optim.Adam(model.parameters(), lr=LR)
# lossFn = nn.CrossEntropyLoss()

# # TensorBoard setup
# writer = SummaryWriter()

# print("Training started...")
# # Training loop
# for e in range(0, EPOCHS):
#     print(f"Epoch {e + 1}/{EPOCHS}")
#     model.train()
#     totalTrainLoss = 0
#     trainCorrect = 0

#     for i, (x, y) in enumerate(train_dataloader):
#         (x, y) = (x.to(device), y.to(device))

#         pred = model(x)
#         loss = lossFn(pred, y)

#         opt.zero_grad()
#         loss.backward()
#         opt.step()

#         totalTrainLoss += loss.item()
#         trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate training accuracy and loss
#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     avgTrainLoss = totalTrainLoss / len(train_dataloader)

#     # Write to TensorBoard
#     writer.add_scalar("Train/Accuracy", trainAccuracy, e)
#     writer.add_scalar("Train/Loss", avgTrainLoss, e)

#     # Visualization of final layers
#     if e == EPOCHS - 1:
#         for name, param in model.named_parameters():
#             writer.add_histogram(name, param.clone().cpu().data.numpy(), e)

#     # Evaluation on test set
#     model.eval()
#     preds = []
#     testCorrect = 0

#     with torch.no_grad():
#         for x, y in test_dataloader:
#             x = x.to(device)
#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     # Calculate test accuracy
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     # Write test accuracy to TensorBoard
#     writer.add_scalar("Test/Accuracy", testAccuracy, e)

# print("Training completed.")

# # Export the model to ONNX for TensorBoard visualization
# dummy_input = torch.randn(1, 1, 28, 28).to(device)  # Example input tensor
# onnx_path = "model.onnx"
# torch.onnx.export(model, dummy_input, onnx_path)
# writer.add_graph(model, dummy_input)


# # Save the model
# torch.save(model, "model.pt")

# # Close the TensorBoard writer
# writer.close()


import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision.transforms import ToTensor
from torch.utils.tensorboard import SummaryWriter
import torch.nn.functional as F
import torchvision
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt


class CNN(nn.Module):
    """
    Convolutional Neural Network (CNN) for MNIST Digit Classification

    Attributes:
    - conv1 (nn.Conv2d): First convolutional layer
    - conv2 (nn.Conv2d): Second convolutional layer
    - fc1 (nn.Linear): First fully connected layer
    - fc2 (nn.Linear): Second fully connected layer

    Methods:
    - forward(x): Forward pass of the CNN

    """

    def __init__(self):
        super(CNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3)
        self.fc1 = nn.Linear(64 * 5 * 5, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = F.relu(F.max_pool2d(self.conv1(x), 2))
        x = F.relu(F.max_pool2d(self.conv2(x), 2))
        x = x.view(-1, 64 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


# Initialization
LR = 0.001  # Set your learning rate
BATCH_SIZE = 64  # Set your batch size
EPOCHS = 10  # Set the number of epochs
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Create the model, dataloaders, optimizer, and loss function
model = CNN()
model.to(device)

train_dataset = mnist.MNIST(
    root="./train", train=True, download=True, transform=ToTensor()
)
test_dataset = mnist.MNIST(
    root="./test", train=False, download=True, transform=ToTensor()
)
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

opt = optim.Adam(model.parameters(), lr=LR)
lossFn = nn.CrossEntropyLoss()

# TensorBoard setup
writer = SummaryWriter()

print("Training started...")
# Training loop
for e in range(0, EPOCHS):
    print(f"Epoch {e + 1}/{EPOCHS}")
    model.train()
    totalTrainLoss = 0
    trainCorrect = 0

    for i, (x, y) in enumerate(train_dataloader):
        (x, y) = (x.to(device), y.to(device))

        pred = model(x)
        loss = lossFn(pred, y)

        opt.zero_grad()
        loss.backward()
        opt.step()

        totalTrainLoss += loss.item()
        trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

    # Calculate training accuracy and loss
    trainAccuracy = trainCorrect / len(train_dataloader.dataset)
    avgTrainLoss = totalTrainLoss / len(train_dataloader)

    # Write to TensorBoard
    writer.add_scalar("Train/Accuracy", trainAccuracy, e)
    writer.add_scalar("Train/Loss", avgTrainLoss, e)

    # Visualization of final layers
    if e == EPOCHS - 1:
        for name, param in model.named_parameters():
            writer.add_histogram(name, param.clone().cpu().data.numpy(), e)

    # Evaluation on test set
    model.eval()
    preds = []
    testCorrect = 0

    with torch.no_grad():
        for x, y in test_dataloader:
            x = x.to(device)
            pred = model(x)
            preds.extend(pred.argmax(axis=1).cpu().numpy())
            testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

    # Calculate test accuracy
    testAccuracy = testCorrect / len(test_dataloader.dataset)

    # Write test accuracy to TensorBoard
    writer.add_scalar("Test/Accuracy", testAccuracy, e)

    # Example of adding input images to TensorBoard
    data_iter = iter(test_dataloader)
    images, labels = next(data_iter)
    grid = torchvision.utils.make_grid(images)
    writer.add_image("Input Images", grid, e)

    # Example of adding learning rate to TensorBoard
    writer.add_scalar("Learning Rate", LR, e)

    # Example of adding model weights to TensorBoard
    for name, param in model.named_parameters():
        if "conv" in name:  # Filter convolutional layers
            writer.add_histogram(name, param.clone().cpu().data.numpy(), e)

# Confusion Matrix Visualization
with torch.no_grad():
    all_preds = []
    all_labels = []
    for x, y in test_dataloader:
        x = x.to(device)
        pred = model(x)
        all_preds.extend(pred.argmax(axis=1).cpu().numpy())
        all_labels.extend(y.cpu().numpy())

cm = confusion_matrix(all_labels, all_preds)
plt.figure(figsize=(10, 8))
sns.heatmap(
    cm, annot=True, fmt="d", cmap="Blues", xticklabels=range(10), yticklabels=range(10)
)
writer.add_figure("Confusion Matrix", plt.gcf(), EPOCHS)

print("Training completed.")

# Export the model to ONNX for TensorBoard visualization
dummy_input = torch.randn(1, 1, 28, 28).to(device)  # Example input tensor
onnx_path = "model.onnx"
torch.onnx.export(model, dummy_input, onnx_path)
writer.add_graph(model, dummy_input)

# Save the model
torch.save(model, "model.pt")

# Close the TensorBoard writer
writer.close()
