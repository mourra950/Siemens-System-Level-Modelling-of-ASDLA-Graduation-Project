
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torchvision.transforms import v2
from torch.optim import lr_scheduler
import torchvision
import re

import os

basedir = os.path.dirname(__file__)
model_output = os.path.normpath(
    os.path.join(basedir, '../SystemC/Pt/model.pt'))
test_output = os.path.normpath(os.path.join(basedir, '../test.txt'))


def main():
    ...


def test_c():
    with open(test_output, "w+") as Output:
        Output.write("ahmed")

exec_globals = {'torch': torch, 'torchvision': torchvision}

def get_min_size():
    torch_layers_names = dir(torchvision.models.{{cookiecutter.transfer_model}})
    for layer_name in torch_layers_names:
        obj = getattr(torchvision.models.{{cookiecutter.transfer_model}}, layer_name)
        match = re.search(r'~torchvision\.models\.(\w+)', str(obj))
        if match:
            extracted_part = match.group(1)
            print(extracted_part)
            exec(f"t=torchvision.models.{extracted_part}.DEFAULT.meta['min_size']",exec_globals)
            print("minimum size", exec_globals['t'])
            return exec_globals['t']


def train():
    # initiallization
    HEIGHT = {{cookiecutter.misc_params.height}}
    WIDTH = {{cookiecutter.misc_params.width}}
    BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
    EPOCHS = {{cookiecutter.misc_params.num_epochs}}
    TRAIN_SPLIT = 0.75
    VAL_SPLIT = 0.15
    TEST_SPLIT = 0.1
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    model = models.{{cookiecutter.transfer_model}}(weights='DEFAULT')
    for name, param in model.named_parameters():
        print(param.shape)
        batch = param.shape[0]
        channels = param.shape[1]
        break
    height, width = get_min_size()
    if (height < HEIGHT):
        height = HEIGHT
    if (width < WIDTH):
        width = WIDTH

    for param in model.parameters():
        param.requires_grad = False
    transform = transforms.Compose([
        v2.Resize((height, width)),
        # Convert images to RGB format
        v2.Grayscale(num_output_channels=channels),
        # Convert images to PyTorch tensors
        v2.ToImage(), v2.ToDtype(torch.float32, scale=True)
    ])
    train_dataset = mnist.MNIST(root='C:/Users/DELL/Desktop/Project',
                                train=True, download=True, transform=transform)
    test_dataset = mnist.MNIST(root='C:/Users/DELL/Desktop/Project',
                               train=False, download=True, transform=transform)
    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True)
    test_dataloader = DataLoader(
        test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)
    loss_fn = nn.CrossEntropyLoss()
    class_names = train_dataset.classes

    # num_ftrs = model.named_children()[-1].in_features
    
    # model.fc.in_features
    (name, layer) = list(model.named_children())[-1]
    exec_d = {'torch': torch, 'torchvision': torchvision,
              'model': model, 'a': layer.in_features, 'nn': nn}
    exec(f"model.{name}=nn.Linear(a, {len(class_names)}) ", exec_d)
    model = model.to(device)

    # Create the chosen optimizer with parameters from the data dictionary
    optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
        model.parameters(),
        {% for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
        {{key}}={{value}},
        {% endfor %}
    )

    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

    # Parameters of newly constructed modules have requires_grad=True by default

    # optimizer = torch.optim.SGD(model.parameters(), lr=1e-3)

    for e in range(0, EPOCHS):
        # print(EPOCHS)
        # set the model in training mode
        model.train()
        # initialize the total training and validation loss
        totalTrainLoss = 0
        totalValLoss = 0
        # initialize the number of correct predictions in the training and validation step
        trainCorrect = 0
        valCorrect = 0
        # loop over the training set
        for (x, y) in train_dataloader:
            # send the input to the device
            (x, y) = (x.to(device), y.to(device))
            # perform a forward pass and calculate the training loss
            pred = model(x)
            loss = loss_fn(pred, y)
            # zero out the gradients, perform the backpropagation step, and update the weights
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # add the loss to the total training loss so far and calculate the number of correct predictions
            totalTrainLoss += loss
            trainCorrect += (pred.argmax(1) == y).type(
                torch.float).sum().item()
        model.eval()
        print(trainCorrect)

    with torch.no_grad():
        model.eval()
        # initialize a list to store our predictions
        preds = []
        testCorrect = 0
        for (x, y) in test_dataloader:
            x = (x.to(device))
            y = (y.to(device))

            pred = model(x)
            preds.extend(pred.argmax(axis=1).cpu().numpy())
            testCorrect += (pred.argmax(1) == y).type(
                torch.float).sum().item()
            # print(testCorrect)

    # calculate the training, validation, and test accuracy
    trainAccuracy = trainCorrect / len(train_dataloader.dataset)
    testAccuracy = testCorrect / len(test_dataloader.dataset)

    print("Train Accuracy:", trainAccuracy)
    print("Test Accuracy:", testAccuracy)
    tensors = torch.jit.script(model)
    tensors.save(model_output)


if __name__ == "__main__":
    train()
