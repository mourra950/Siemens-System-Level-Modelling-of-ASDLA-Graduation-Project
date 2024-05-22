
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torch.optim import lr_scheduler
from torch.utils.tensorboard import SummaryWriter
import torchvision
from torchvision import datasets, transforms

from .model import CNN
from tqdm import tqdm

import os

basedir = os.path.dirname(__file__)
model_output = os.path.normpath(
    os.path.join(basedir, '../SystemC/Pt/model.pt'))
test_output = os.path.normpath(os.path.join(basedir, '../test.txt'))

exec_globals = {'torch': torch, 'torchvision': torchvision}


def train():
    # initiallization
    writer = SummaryWriter(log_dir=r'{{cookiecutter.log_dir}}')
    HEIGHT = {{cookiecutter.misc_params.height}}
    WIDTH = {{cookiecutter.misc_params.width}}
    BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
    EPOCHS = {{cookiecutter.misc_params.num_epochs}}
    TRAIN_SPLIT = 0.75
    VAL_SPLIT = 0.15
    TEST_SPLIT = 0.1
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    model = CNN()
    model = model.to(device)

    transform = transforms.ToTensor()

    train_dataset = datasets.MNIST(root=r"{{cookiecutter.mnist_path}}",
                                train=True, download=True, transform=transform)
    
    train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    loss_fn = nn.{{cookiecutter.misc_params.loss_func.type}}(
        {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
            {{key}}={{value}},
        {% endfor %}
    )
    optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
        model.parameters(),
        {% for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
        {%- if value is sequence and value is not string -%}
        {{key}}=({{value|join(', ')}}),
        {%- else -%}
        {{key}}={{value}},
        {%- endif %}
        {% endfor %}
    )

    for e in range(0, EPOCHS):
        model.train()

        totalTrainLoss = 0
        trainCorrect = 0

        for (x, y) in tqdm(train_dataloader):
            (x, y) = (x.to(device), y.to(device))

            pred = model(x)
            loss = loss_fn(pred, y)
            writer.add_scalar("Loss/train", loss, e)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            totalTrainLoss += loss
            trainCorrect += (pred.argmax(1) == y).type(
                torch.float).sum().item()
        writer.add_scalar("Train/Accuracy", trainCorrect, e)
        writer.add_scalar("Train/Loss", totalTrainLoss, e)
        model.eval()
        print(trainCorrect)
    scripted = torch.jit.script(model)
    try:
        torch.jit.save(scripted, model_output)
    except e:
        print(e)
    

if __name__ == '__main__':
    train()