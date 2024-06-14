
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torch.optim import lr_scheduler
from torch.utils.tensorboard import SummaryWriter
import torchvision
from torchvision.transforms import v2
from torchvision import datasets, transforms

from python.model import CNN
import datetime
import os

basedir = os.path.dirname(__file__)
model_output = os.path.normpath(
    os.path.join(basedir, '../SystemC/Pt/model.pt'))
test_output = os.path.normpath(os.path.join(basedir, '../test.txt'))


def train(callback):
    unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_log_dir = r'{{cookiecutter.log_dir}}'
    log_dir = os.path.join(base_log_dir, unique_name)

    writer = SummaryWriter(log_dir=log_dir)
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

    transform = v2.Compose(
        [v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])

    train_dataset = datasets.MNIST(root=r"{{cookiecutter.mnist_path}}",
                                   train=True, download=True, transform=transform)

    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True)
    loss_fn = nn.{{cookiecutter.misc_params.loss_func.type}}(
        {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
        {%- if key == "device" -%}
            {{key}}=device,
            {%- else -%}
            {{key}}={{value}},
        {%- endif %}
        {% endfor %}
    )
    optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
        model.parameters(),
        {% for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
        {%- if value is sequence and value is not string -%}
        {{key}}=({{value | join(', ')}}),
        {%- else -%}
            {%- if key == "device" -%}
            {{key}}=device,
            {%- else -%}
            {{key}}={{value}},
            {%- endif %}
        {%- endif %}
        {% endfor %}
    )
    train_size = len(train_dataset)
    for e in range(0, EPOCHS):
        model.train()

        totalTrainLoss = 0
        trainCorrect = 0

        for i, (x, y) in enumerate(train_dataloader):
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

            progress = ((e*train_size + i) / (EPOCHS*train_size)) * 100
            callback(progress)
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
