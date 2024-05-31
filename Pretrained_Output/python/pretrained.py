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
model_output = os.path.normpath(os.path.join(basedir, "../SystemC/Pt/model.pt"))
test_output = os.path.normpath(os.path.join(basedir, "../test.txt"))


# def get_min_size():

#     min_size = torchvision.models.get_model_weights(models.resnet18).DEFAULT.meta['min_size']
#     return min_size


def train(callback):
    # initiallization
    unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_log_dir = r"d:\nada\nada\GP\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\data\tensorboardlogs"
    log_dir = os.path.join(base_log_dir, unique_name)

    writer = SummaryWriter(log_dir=log_dir)
    HEIGHT = 1
    WIDTH = 1
    BATCH_SIZE = 32
    EPOCHS = 1
    TRAIN_SPLIT = 0.75
    VAL_SPLIT = 0.15
    TEST_SPLIT = 0.1
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    # model = models.resnet18(weights='DEFAULT')
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
            v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]
    )
    # KAN HENA
    #     <<<<<<< HEAD
    #     train_dataset = mnist.MNIST(root='C:/Users/DELL/Desktop/Project',
    #                                 train=True, download=True, transform=transform)
    #     test_dataset = mnist.MNIST(root='C:/Users/DELL/Desktop/Project',
    # =======
    #     train_dataset = mnist.MNIST(root=r"d:\nada\nada\GP\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\data\mnist",
    #                                 train=True, download=True, transform=transform)
    #     test_dataset = mnist.MNIST(root=r"d:\nada\nada\GP\Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project\data\mnist",
    # >>>>>>> 8d19423ff966d255a053b84d555490f48460a7c8
    #                                train=False, download=True, transform=transform)
    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
    )
    test_dataloader = DataLoader(
        test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
    )
    # loss_fn = nn.CrossEntropyLoss(
    #     
    #     ignore_index=1,
    #     
    #     label_smoothing=0.0,
    #     
    #     reduction='mean',
    #     
    # )
    class_names = train_dataset.classes

    # num_ftrs = model.named_children()[-1].in_features
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
    # optimizer = optim.Adam(
    #     model.parameters(),
    #     
    ##     amsgrad=False,
    #
    #     
    ##     betas=(0.9, 0.999),
    #
    #     
    ##     eps=1e-08,
    #
    #     
    ##     lr=0.001,
    #
    #     
    ##     weight_decay=0.0,
    #
    #     
    # )

    train_size = len(train_dataset)

    # Decay LR by a factor of 0.1 every 7 epochs
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer, step_size=7, gamma=0.1)

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
            trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
            progress = ((e * train_size + i) / (EPOCHS * train_size)) * 100
            callback(progress)
        writer.add_scalar("Train/Accuracy", trainCorrect, e)
        writer.add_scalar("Train/Loss", totalTrainLoss, e)
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