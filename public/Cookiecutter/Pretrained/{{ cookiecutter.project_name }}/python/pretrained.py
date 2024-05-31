# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torchvision.transforms import v2
from torch.optim import lr_scheduler
from torch.utils.tensorboard import SummaryWriter
import torchvision
import re
import datetime
import os

basedir = os.path.dirname(__file__)
model_output = os.path.normpath(
    os.path.join(basedir, "../SystemC/Pt/model.pt"))
test_output = os.path.normpath(os.path.join(basedir, "../test.txt"))


def get_min_size():

    min_size = torchvision.models.get_model_weights(models.{{cookiecutter.transfer_model}}).DEFAULT.meta['min_size']
    return min_size


def train(callback):
    # initiallization
    unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_log_dir = r"{{cookiecutter.log_dir}}"
    log_dir = os.path.join(base_log_dir, unique_name)

    writer = SummaryWriter(log_dir=log_dir)
    HEIGHT = {{cookiecutter.misc_params.height}}
    WIDTH = {{cookiecutter.misc_params.width}}
    BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
    EPOCHS = {{cookiecutter.misc_params.num_epochs}}
    TRAIN_SPLIT = 0.75
    VAL_SPLIT = 0.15
    TEST_SPLIT = 0.1
    device = torch.device("{{cookiecutter.misc_params.device}}")
    model = models.{{cookiecutter.transfer_model}}(weights='DEFAULT')
    for name, param in model.named_parameters():
        print(param.shape)
        batch = param.shape[0]
        channels = param.shape[1]
        break
    height, width = get_min_size()
    if height < HEIGHT:
        height = HEIGHT
    if width < WIDTH:
        width = WIDTH

    for param in model.parameters():
        param.requires_grad = False
    transform = transforms.Compose(
        [
            v2.Resize((height, width)),
            # Convert images to RGB format
            v2.Grayscale(num_output_channels=channels),
            # Convert images to PyTorch tensors
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
            v2.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
        ]
    )

    train_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
                                train=True, download=True, transform=transform)
    test_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
                               train=False, download=True, transform=transform)
    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
    )
    test_dataloader = DataLoader(
        test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
    )
    loss_fn = nn.{{ cookiecutter.misc_params.loss_func.type }}(
    {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
    {{ key }}={{ value }},
    {% endfor %}
    )
    class_names = train_dataset.classes


    # num_ftrs = model.named_children()[-1].in_features
    # # Assuming 'model' is already defined
    named_children_list = list(model.named_children())
    last_layer_name, last_layer = named_children_list[-1]
    num_ftrs = last_layer.in_features
    try:
        model.aux.logits = False
    except:
        pass
    # model.fc.in_features
    (name, layer) = list(model.named_children())[-1]
    if type(layer) == type(nn.Sequential()):
        for i, j in list(layer.named_children()):
            if type(j) == type(nn.Linear(in_features=15, out_features=15)):
                model.__dict__[name] = nn.Linear(
                    j.in_features, len(class_names), device=device
                )
    else:
        model.__dict__[name] = nn.Linear(
            layer.in_features, len(class_names), device=device
        )

    model = model.to(device)

    # Create the chosen optimizer with parameters from the data dictionary
    optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
        model.parameters(),
        {% for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
        {%- if value is sequence and value is not string -%}
        {{key}}=({{value | join(', ')}}),
        {%- else -%}
        {{key}}={{value}},
        {%- endif %}
        {% endfor %}
    )

    train_size = len(train_dataset)

    
        # Read lr_scheduler type and params from JSON config
    lr_scheduler_type = "{{cookiecutter.misc_params.scheduler.type}}"
    lr_scheduler_params = {{cookiecutter.misc_params.scheduler.params}}
    
    # Dynamically create the lr_scheduler
    scheduler = getattr(lr_scheduler, lr_scheduler_type)(optimizer, **lr_scheduler_params)


    for e in range(0, EPOCHS):

        model.train()
        # initialize the total training and validation loss
        totalTrainLoss = 0
        totalValLoss = 0
        # initialize the number of correct predictions in the training and validation step
        trainCorrect = 0
        valCorrect = 0
        # loop over the training set
        for i, (x, y) in enumerate(train_dataloader):
            # send the input to the device
            (x, y) = (x.to(device), y.to(device))
            # perform a forward pass and calculate the training loss
            pred = model(x)
            loss = loss_fn(pred, y)
            writer.add_scalar("Loss/train", loss, e)

            # zero out the gradients, perform the backpropagation step, and update the weights
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            # add the loss to the total training loss so far and calculate the number of correct predictions
            totalTrainLoss += loss
            trainCorrect += (pred.argmax(1) ==
                             y).type(torch.float).sum().item()
            progress = ((e * train_size + i) / (EPOCHS * train_size)) * 100
            callback(progress)
        writer.add_scalar("Train/Accuracy", trainCorrect, e)
        writer.add_scalar("Train/Loss", totalTrainLoss, e)
        scheduler.step()  
        model.eval()
        print(trainCorrect)

    with torch.no_grad():
        model.eval()
        # initialize a list to store our predictions
        preds = []
        testCorrect = 0
        for x, y in test_dataloader:
            x = x.to(device)
            y = y.to(device)

            pred = model(x)
            preds.extend(pred.argmax(axis=1).cpu().numpy())
            testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
            # print(testCorrect)

    # calculate the training, validation, and test accuracy
    trainAccuracy = trainCorrect / len(train_dataloader.dataset)
    testAccuracy = testCorrect / len(test_dataloader.dataset)

    print("Train Accuracy:", trainAccuracy)
    print("Test Accuracy:", testAccuracy)
    tensors = torch.jit.script(model)
    tensors.save(model_output)
    writer.close()


if __name__ == "__main__":
    train()
