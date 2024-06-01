# # import the necessary packages
# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader
# from torchvision.datasets import mnist
# from torchvision import models, transforms
# from torchvision.transforms import v2
# from torch.optim import lr_scheduler
# from torch.optim.lr_scheduler import *
# from torch.utils.tensorboard import SummaryWriter
# import torchvision
# import re
# import datetime
# import os

# basedir = os.path.dirname(__file__)
# model_output = os.path.normpath(
#     os.path.join(basedir, "../SystemC/Pt/model.pt"))
# test_output = os.path.normpath(os.path.join(basedir, "../test.txt"))


# def get_min_size():

#     min_size = torchvision.models.get_model_weights(models.{{cookiecutter.transfer_model}}).DEFAULT.meta['min_size']
#     return min_size


# def train(callback):
#     # initiallization
#     unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#     base_log_dir = r"{{cookiecutter.log_dir}}"
#     log_dir = os.path.join(base_log_dir, unique_name)

#     writer = SummaryWriter(log_dir=log_dir)
#     HEIGHT = {{cookiecutter.misc_params.height}}
#     WIDTH = {{cookiecutter.misc_params.width}}
#     BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
#     EPOCHS = {{cookiecutter.misc_params.num_epochs}}
#     TRAIN_SPLIT = 0.75
#     VAL_SPLIT = 0.15
#     TEST_SPLIT = 0.1
#     device = torch.device("{{cookiecutter.misc_params.device}}")
#     model = models.{{cookiecutter.transfer_model}}(weights='DEFAULT')
#     for name, param in model.named_parameters():
#         print(param.shape)
#         batch = param.shape[0]
#         channels = param.shape[1]
#         break
#     height, width = get_min_size()
#     if height < HEIGHT:
#         height = HEIGHT
#     if width < WIDTH:
#         width = WIDTH

#     for param in model.parameters():
#         param.requires_grad = False
#     transform = transforms.Compose(
#         [
#             v2.Resize((height, width)),
#             # Convert images to RGB format
#             v2.Grayscale(num_output_channels=channels),
#             # Convert images to PyTorch tensors
#             v2.ToImage(),
#             v2.ToDtype(torch.float32, scale=True),
#             v2.Normalize(mean=[0.485, 0.456, 0.406],
#                          std=[0.229, 0.224, 0.225]),
#         ]
#     )

#     train_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                 train=True, download=True, transform=transform)
#     test_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                train=False, download=True, transform=transform)
#     train_dataloader = DataLoader(
#         train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
#     )
#     test_dataloader = DataLoader(
#         test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
#     )
#     loss_fn = nn.{{ cookiecutter.misc_params.loss_func.type }}(
#     {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
#     {{ key }}={{ value }},
#     {% endfor %}
#     )
#     class_names = train_dataset.classes


#     # num_ftrs = model.named_children()[-1].in_features
#     # # Assuming 'model' is already defined
#     # named_children_list = list(model.named_children())
#     # last_layer_name, last_layer = named_children_list[-1]
#     # num_ftrs = last_layer.in_features
#     # try:
#     #     model.aux.logits = False
#     # except:
#     #     pass
#     # # model.fc.in_features
#     # (name, layer) = list(model.named_children())[-1]
#     # if type(layer) == type(nn.Sequential()):
#     #     for i, j in list(layer.named_children()):
#     #         if type(j) == type(nn.Linear(in_features=15, out_features=15)):
#     #             model.__dict__[name] = nn.Linear(
#     #                 j.in_features, len(class_names), device=device
#     #             )
#     # else:
#     #     model.__dict__[name] = nn.Linear(
#     #         layer.in_features, len(class_names), device=device
#     #     )

#     # model = model.to(device)
    
#     # Assuming 'model' is already defined
#     named_children_list = list(model.named_children())
#     last_layer_name, last_layer = named_children_list[-1]

#     # Extracting number of features from the last layer
#     if isinstance(last_layer, nn.Sequential):
#         last_layer_children = list(last_layer.children())
#         last_layer = last_layer_children[-1]
#     num_ftrs = last_layer.in_features

#     # Attempting to modify the model's architecture
#     try:
#         model.aux.logits = False
#     except AttributeError:
#         pass

#     # Defining the number of output classes
#     num_classes = len(class_names)

#     # Modifying the last layer of the model
#     if isinstance(last_layer, nn.Sequential):
#         for child_name, child_layer in last_layer.named_children():
#             if isinstance(child_layer, nn.Linear):
#                 model.__dict__[last_layer_name].add_module(
#                     child_name,
#                     nn.Linear(child_layer.in_features, num_classes).to(device)
#                 )
#     else:
#         model.__dict__[last_layer_name] = nn.Linear(
#             last_layer.in_features, num_classes
#         ).to(device)

#     # Moving the model to the specified device
#     model = model.to(device)


#     # # Create the chosen optimizer with parameters from the data dictionary
#     # optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
#     #     model.parameters(),
#     #     {% for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
#     #     {%- if value is sequence and value is not string -%}
#     #     {{key}}=({{value | join(', ')}}),
#     #     {%- else -%}
#     #     {{key}}={{value}},
#     #     {%- endif %}
#     #     {% endfor %}
#     # )
    
#     # Create the chosen optimizer with parameters from the data dictionary
#     optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
#         [ {"params": model.parameters(), "initial_lr": {{cookiecutter.misc_params.optimizer.params.lr}}} ]
#         {%- for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
#         {%- if value is sequence and value is not string -%}
#         , {{key}}=({{value | join(', ')}})
#         {%- else -%}
#         , {{key}}={{value}}
#         {%- endif %}
#         {%- endfor %}
#     )

    


#     train_size = len(train_dataset)

    
#     #     # Read lr_scheduler type and params from JSON config
#     # lr_scheduler_type = "{{cookiecutter.misc_params.scheduler.type}}"
#     # lr_scheduler_params = {{cookiecutter.misc_params.scheduler.params}}
    
#     # # Dynamically create the lr_scheduler
#     # scheduler = getattr(lr_scheduler, lr_scheduler_type)(optimizer, **lr_scheduler_params)
#     # Read lr_scheduler type and params from JSON config

#     # Create the scheduler directly

#     # # Extract scheduler type and parameters from the data dictionary
#     # scheduler_type = {{cookiecutter.misc_params.scheduler.type}}
#     # scheduler_params = {
#     #     {% for key, value in cookiecutter.misc_params.scheduler.params|dictsort %}
#     #     {%- if value is sequence and value is not string -%}
#     #     "{{key}}": ({{value | join(', ')}}),
#     #     {%- else -%}
#     #     "{{key}}": {{value}},
#     #     {%- endif %}
#     #     {% endfor %}
#     # }

#     # # Create the chosen scheduler with parameters
#     # scheduler = scheduler_type(optimizer, **scheduler_params)
    
#     # Create the chosen scheduler with parameters
#     scheduler = {{cookiecutter.misc_params.scheduler.type}}(optimizer,
#         {%- for key, value in cookiecutter.misc_params.scheduler.params|dictsort %}
#             {%- if value is sequence and value is not string -%}
#             {{key}}=({{value | join(', ')}}),
#             {%- else -%}
#             {{key}}={{value}},
#             {%- endif %}
#         {%- endfor %}
#     )






#     for e in range(0, EPOCHS):

#         model.train()
#         # initialize the total training and validation loss
#         totalTrainLoss = 0
#         totalValLoss = 0
#         # initialize the number of correct predictions in the training and validation step
#         trainCorrect = 0
#         valCorrect = 0
#         # loop over the training set
#         for i, (x, y) in enumerate(train_dataloader):
#             # send the input to the device
#             (x, y) = (x.to(device), y.to(device))
#             # perform a forward pass and calculate the training loss
#             pred = model(x)
#             loss = loss_fn(pred, y)
#             writer.add_scalar("Loss/train", loss, e)

#             # zero out the gradients, perform the backpropagation step, and update the weights
#             optimizer.zero_grad()
#             loss.backward()
#             optimizer.step()
#             # add the loss to the total training loss so far and calculate the number of correct predictions
#             totalTrainLoss += loss
#             trainCorrect += (pred.argmax(1) ==
#                              y).type(torch.float).sum().item()
#             progress = ((e * train_size + i) / (EPOCHS * train_size)) * 100
#             callback(progress)
#         writer.add_scalar("Train/Accuracy", trainCorrect, e)
#         writer.add_scalar("Train/Loss", totalTrainLoss, e)
#         scheduler.step()  
#         model.eval()
#         print(trainCorrect)

#     with torch.no_grad():
#         model.eval()
#         # initialize a list to store our predictions
#         preds = []
#         testCorrect = 0
#         for x, y in test_dataloader:
#             x = x.to(device)
#             y = y.to(device)

#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
#             # print(testCorrect)

#     # calculate the training, validation, and test accuracy
#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     print("Train Accuracy:", trainAccuracy)
#     print("Test Accuracy:", testAccuracy)
#     tensors = torch.jit.script(model)
#     tensors.save(model_output)
#     writer.close()


# if __name__ == "__main__":
#     train()



# # import the necessary packages
# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader
# from torchvision.datasets import mnist
# from torchvision import models, transforms
# from torchvision.transforms import v2
# from torch.optim import lr_scheduler
# from torch.optim.lr_scheduler import *
# from torch.utils.tensorboard import SummaryWriter
# import torchvision
# import datetime
# import os

# basedir = os.path.dirname(__file__)
# model_output = os.path.normpath(
#     os.path.join(basedir, "../SystemC/Pt/model.pt"))

# def get_min_size():
#     min_size = torchvision.models.get_model_weights(models.{{cookiecutter.transfer_model}}).DEFAULT.meta['min_size']
#     return min_size

# def train(callback):
#     # initialization
#     unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#     base_log_dir = r"{{cookiecutter.log_dir}}"
#     log_dir = os.path.join(base_log_dir, unique_name)

#     writer = SummaryWriter(log_dir=log_dir)
#     HEIGHT = {{cookiecutter.misc_params.height}}
#     WIDTH = {{cookiecutter.misc_params.width}}
#     BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
#     EPOCHS = {{cookiecutter.misc_params.num_epochs}}
#     TRAIN_SPLIT = 0.75
#     VAL_SPLIT = 0.15
#     TEST_SPLIT = 0.1
#     device = torch.device("{{cookiecutter.misc_params.device}}")
#     model = models.{{cookiecutter.transfer_model}}(weights='DEFAULT')
    
#     for name, param in model.named_parameters():
#         print(param.shape)
#         batch = param.shape[0]
#         channels = param.shape[1]
#         break

#     height, width = get_min_size()
#     if height < HEIGHT:
#         height = HEIGHT
#     if width < WIDTH:
#         width = WIDTH

#     for param in model.parameters():
#         param.requires_grad = False
        
#     transform = transforms.Compose(
#         [
#             v2.Resize((height, width)),
#             # Convert images to RGB format
#             v2.Grayscale(num_output_channels=channels),
#             # Convert images to PyTorch tensors
#             v2.ToImage(),
#             v2.ToDtype(torch.float32, scale=True),
#             v2.Normalize(mean=[0.485, 0.456, 0.406],
#                          std=[0.229, 0.224, 0.225]),
#         ]
#     )

#     train_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                 train=True, download=True, transform=transform)
#     test_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                train=False, download=True, transform=transform)
                               
#     train_dataloader = DataLoader(
#         train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
#     )
#     test_dataloader = DataLoader(
#         test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
#     )
    
#     loss_fn = nn.{{ cookiecutter.misc_params.loss_func.type }}(
#     {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
#     {{ key }}={{ value }},
#     {% endfor %}
#     )
    
#     class_names = train_dataset.classes
    
#     # Modify the model's architecture
#     named_children_list = list(model.named_children())
#     last_layer_name, last_layer = named_children_list[-1]

#     # Extracting number of features from the last layer
#     if isinstance(last_layer, nn.Sequential):
#         last_layer_children = list(last_layer.children())
#         last_layer = last_layer_children[-1]
#     num_ftrs = last_layer.in_features

#     try:
#         model.aux.logits = False
#     except AttributeError:
#         pass

#     num_classes = len(class_names)

#     if isinstance(last_layer, nn.Sequential):
#         for child_name, child_layer in last_layer.named_children():
#             if isinstance(child_layer, nn.Linear):
#                 model.__dict__[last_layer_name].add_module(
#                     child_name,
#                     nn.Linear(child_layer.in_features, num_classes).to(device)
#                 )
#     else:
#         model.__dict__[last_layer_name] = nn.Linear(
#             last_layer.in_features, num_classes
#         ).to(device)

#     model = model.to(device)
    
#     # Create the chosen optimizer with parameters from the data dictionary
#     optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
#         [ {"params": model.parameters(), "initial_lr": {{cookiecutter.misc_params.optimizer.params.lr}}} ]
#         {%- for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
#         {%- if value is sequence and value is not string -%}
#         , {{key}}=({{value | join(', ')}})
#         {%- else -%}
#         , {{key}}={{value}}
#         {%- endif %}
#         {%- endfor %}
#     )

#     train_size = len(train_dataset)

#     # Create the chosen scheduler with parameters
#     scheduler = {{cookiecutter.misc_params.scheduler.type}}(optimizer,
#         {%- for key, value in cookiecutter.misc_params.scheduler.params|dictsort %}
#             {%- if value is sequence and value is not string -%}
#             {{key}}=({{value | join(', ')}}),
#             {%- else -%}
#             {{key}}={{value}},
#             {%- endif %}
#         {%- endfor %}
#     )

#     for e in range(0, EPOCHS):
#         model.train()
#         totalTrainLoss = 0
#         trainCorrect = 0

#         for i, (x, y) in enumerate(train_dataloader):
#             (x, y) = (x.to(device), y.to(device))
#             pred = model(x)
#             loss = loss_fn(pred, y)
#             writer.add_scalar("Loss/train", loss, e)

#             optimizer.zero_grad()
#             loss.backward()
#             optimizer.step()
            
#             totalTrainLoss += loss.item()
#             trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
#             progress = ((e * train_size + i) / (EPOCHS * train_size)) * 100
#             callback(progress)
        
#         writer.add_scalar("Train/Accuracy", trainCorrect / len(train_dataloader.dataset), e)
#         writer.add_scalar("Train/Loss", totalTrainLoss, e)
#         scheduler.step()  
#         model.eval()
#         print(f"Epoch {e+1}, Train Accuracy: {trainCorrect / len(train_dataloader.dataset)}")

#     with torch.no_grad():
#         model.eval()
#         preds = []
#         testCorrect = 0
        
#         for x, y in test_dataloader:
#             x = x.to(device)
#             y = y.to(device)
#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     print("Train Accuracy:", trainAccuracy)
#     print("Test Accuracy:", testAccuracy)

#################################################################################################
# worked version with resnet perfectly
#################################################################################################

# # import the necessary packages
# import torch
# from torch import nn, optim
# from torch.utils.data import DataLoader
# from torchvision.datasets import mnist
# from torchvision import models, transforms
# from torchvision.transforms import v2
# from torch.optim import lr_scheduler
# from torch.optim.lr_scheduler import *
# from torch.utils.tensorboard import SummaryWriter
# import torchvision
# import datetime
# import os

# basedir = os.path.dirname(__file__)
# model_output = os.path.normpath(
#     os.path.join(basedir, "../SystemC/Pt/model.pt"))

# def get_min_size():
#     min_size = torchvision.models.get_model_weights(models.{{cookiecutter.transfer_model}}).DEFAULT.meta['min_size']
#     return min_size

# def train(callback):
#     # initialization
#     unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
#     base_log_dir = r"{{cookiecutter.log_dir}}"
#     log_dir = os.path.join(base_log_dir, unique_name)

#     writer = SummaryWriter(log_dir=log_dir)
#     HEIGHT = {{cookiecutter.misc_params.height}}
#     WIDTH = {{cookiecutter.misc_params.width}}
#     BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
#     EPOCHS = {{cookiecutter.misc_params.num_epochs}}
#     TRAIN_SPLIT = 0.75
#     VAL_SPLIT = 0.15
#     TEST_SPLIT = 0.1
#     device = torch.device("{{cookiecutter.misc_params.device}}")
#     model = models.{{cookiecutter.transfer_model}}(weights='DEFAULT')
    
#     for name, param in model.named_parameters():
#         print(param.shape)
#         batch = param.shape[0]
#         channels = param.shape[1]
#         break

#     height, width = get_min_size()
#     if height < HEIGHT:
#         height = HEIGHT
#     if width < WIDTH:
#         width = WIDTH

#     for param in model.parameters():
#         param.requires_grad = False
        
#     transform = transforms.Compose(
#         [
#             v2.Resize((height, width)),
#             # Convert images to RGB format
#             v2.Grayscale(num_output_channels=3),  # Ensure 3 channels for ResNet
#             # Convert images to PyTorch tensors
#             v2.ToImage(),
#             v2.ToDtype(torch.float32, scale=True),
#             v2.Normalize(mean=[0.485, 0.456, 0.406],
#                          std=[0.229, 0.224, 0.225]),
#         ]
#     )

#     train_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                 train=True, download=True, transform=transform)
#     test_dataset = mnist.MNIST(root=r"{{cookiecutter.mnist_path}}",
#                                train=False, download=True, transform=transform)
                               
#     train_dataloader = DataLoader(
#         train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
#     )
#     test_dataloader = DataLoader(
#         test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
#     )
    
#     loss_fn = nn.{{ cookiecutter.misc_params.loss_func.type }}(
#     {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
#     {{ key }}={{ value }},
#     {% endfor %}
#     )
    
#     class_names = train_dataset.classes
    
#     # Modify the model's architecture
#     named_children_list = list(model.named_children())
#     last_layer_name, last_layer = named_children_list[-1]

#     # Extracting number of features from the last layer
#     if isinstance(last_layer, nn.Sequential):
#         last_layer_children = list(last_layer.children())
#         last_layer = last_layer_children[-1]
#     num_ftrs = last_layer.in_features

#     try:
#         model.aux.logits = False
#     except AttributeError:
#         pass

#     num_classes = len(class_names)

#     if isinstance(last_layer, nn.Sequential):
#         for child_name, child_layer in last_layer.named_children():
#             if isinstance(child_layer, nn.Linear):
#                 model.__dict__[last_layer_name].add_module(
#                     child_name,
#                     nn.Linear(child_layer.in_features, num_classes).to(device)
#                 )
#     else:
#         model.__dict__[last_layer_name] = nn.Linear(
#             last_layer.in_features, num_classes
#         ).to(device)

#     model = model.to(device)
    
#     # Create the chosen optimizer with parameters from the data dictionary
#     optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
#         [ {"params": model.parameters(), "initial_lr": {{cookiecutter.misc_params.optimizer.params.lr}}} ]
#         {%- for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
#         {%- if value is sequence and value is not string -%}
#         , {{key}}=({{value | join(', ')}})
#         {%- else -%}
#         , {{key}}={{value}}
#         {%- endif %}
#         {%- endfor %}
#     )

#     train_size = len(train_dataset)

#     # Create the chosen scheduler with parameters
#     scheduler = {{cookiecutter.misc_params.scheduler.type}}(optimizer,
#         {%- for key, value in cookiecutter.misc_params.scheduler.params|dictsort %}
#             {%- if value is sequence and value is not string -%}
#             {{key}}=({{value | join(', ')}}),
#             {%- else -%}
#             {{key}}={{value}},
#             {%- endif %}
#         {%- endfor %}
#     )

#     for e in range(0, EPOCHS):
#         model.train()
#         totalTrainLoss = 0
#         trainCorrect = 0

#         for i, (x, y) in enumerate(train_dataloader):
#             (x, y) = (x.to(device), y.to(device))
#             pred = model(x)
#             loss = loss_fn(pred, y)
#             writer.add_scalar("Loss/train", loss.item(), e * len(train_dataloader) + i)

#             optimizer.zero_grad()
#             loss.backward()
#             optimizer.step()
            
#             totalTrainLoss += loss.item()
#             trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
#             progress = ((e * len(train_dataloader) + i) / (EPOCHS * len(train_dataloader))) * 100
#             callback(progress)
        
#         writer.add_scalar("Train/Accuracy", trainCorrect / len(train_dataloader.dataset), e)
#         writer.add_scalar("Train/Loss", totalTrainLoss, e)
#         scheduler.step()  
#         model.eval()
#         print(f"Epoch {e+1}, Train Accuracy: {trainCorrect / len(train_dataloader.dataset)}")

#     with torch.no_grad():
#         model.eval()
#         preds = []
#         testCorrect = 0
        
#         for x, y in test_dataloader:
#             x = x.to(device)
#             y = y.to(device)
#             pred = model(x)
#             preds.extend(pred.argmax(axis=1).cpu().numpy())
#             testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

#     trainAccuracy = trainCorrect / len(train_dataloader.dataset)
#     testAccuracy = testCorrect / len(test_dataloader.dataset)

#     print("Train Accuracy:", trainAccuracy)
#     print("Test Accuracy:", testAccuracy)
    
#     tensors = torch.jit.script(model)
#     tensors

#     tensors.save(model_output)
#     writer.close()

# if __name__ == "__main__":
#     train(lambda x: print(f"Progress: {x:.2f}%"))


##############################################################################################
# version works with resnet, vgg, alexnet, mobilenet and inception
##############################################################################################
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision.datasets import mnist
from torchvision import models, transforms
from torchvision.transforms import v2
from torch.optim import lr_scheduler
from torch.optim.lr_scheduler import *
from torch.utils.tensorboard import SummaryWriter
import torchvision
import datetime
import os

basedir = os.path.dirname(__file__)
model_output = os.path.normpath(
    os.path.join(basedir, "../SystemC/Pt/model.pt"))

# def get_min_size():
#     min_size = torchvision.models.get_model_weights(models.{{cookiecutter.transfer_model}}).DEFAULT.meta['min_size']
#     return min_size

def get_min_size(model_name):
    # Function to get the minimum input size required by the model
    if model_name.startswith('vgg'):
        return 224, 224
    elif model_name.startswith('resnet') or model_name.startswith('alexnet'):
        return 224, 224
    elif model_name.startswith('alexnet'):
           return 227, 227    
    elif model_name.startswith('mobilenet'):
        return 224, 224
    elif model_name.startswith('inception'):
        return 299, 299
    else:
        return 224, 224  # Default size

from torchvision.datasets import MNIST  # Added import for MNIST dataset

def train(callback):
    # initialization
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
    
    model_name = "{{cookiecutter.transfer_model}}"
    
    # Choose the model architecture dynamically
    model = getattr(models, model_name)(pretrained=True)

    # Modify the last layer for the specific classification task
    num_classes = 10  # Modify according to the number of classes in your dataset
    if hasattr(model, 'classifier'):  # VGG, AlexNet
        in_features = model.classifier[-1].in_features
        model.classifier[-1] = nn.Linear(in_features, num_classes)
    elif hasattr(model, 'fc'):  # ResNet, MobileNet
        in_features = model.fc.in_features
        model.fc = nn.Linear(in_features, num_classes)
    elif hasattr(model, 'last_linear'):  # Inception
        in_features = model.last_linear.in_features
        model.last_linear = nn.Linear(in_features, num_classes)
    else:
        raise ValueError("Unsupported model architecture")

    model = model.to(device)
    
    transform = transforms.Compose([
    transforms.Resize((HEIGHT, WIDTH)),  # Resize the input images
    transforms.Grayscale(num_output_channels=3),  # Convert to RGB format
    transforms.ToTensor(),               # Convert images to PyTorch tensors
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),  # Normalize
])



    train_dataset = MNIST(root=r"{{cookiecutter.mnist_path}}", train=True, download=True, transform=transform)
    test_dataset = MNIST(root=r"{{cookiecutter.mnist_path}}", train=False, download=True, transform=transform)
    
    train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True)
    test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True)
    
    loss_fn = nn.{{ cookiecutter.misc_params.loss_func.type }}(
        {% for key, value in cookiecutter.misc_params.loss_func.params|dictsort %}
        {{ key }}={{ value }},
        {% endfor %}
    )
    
    optimizer = optim.{{cookiecutter.misc_params.optimizer.type}}(
        [ {"params": model.parameters(), "initial_lr": {{cookiecutter.misc_params.optimizer.params.lr}}} ]
        {%- for key, value in cookiecutter.misc_params.optimizer.params|dictsort %}
        {%- if value is sequence and value is not string -%}
        , {{key}}=({{value | join(', ')}})
        {%- else -%}
        , {{key}}={{value}}
        {%- endif %}
        {%- endfor %}
    )

    scheduler = {{cookiecutter.misc_params.scheduler.type}}(optimizer,
        {%- for key, value in cookiecutter.misc_params.scheduler.params|dictsort %}
            {%- if value is sequence and value is not string -%}
            {{key}}=({{value | join(', ')}}),
            {%- else -%}
            {{key}}={{value}},
            {%- endif %}
        {%- endfor %}
    )

    for e in range(0, EPOCHS):
        model.train()
        total_train_loss = 0
        train_correct = 0

        for i, (x, y) in enumerate(train_dataloader):
            x, y = x.to(device), y.to(device)
            if model_name.startswith("inception"):
                output, _ = model(
                    x
                )  # Get only the main output, ignoring the auxiliary logits
                pred = output  # Update pred to be the main output
                loss = loss_fn(output, y)
            else:
                pred = model(x)
                loss = loss_fn(pred, y)
            writer.add_scalar("Loss/train", loss.item(), e * len(train_dataloader) + i)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_train_loss += loss.item()
            train_correct += (pred.argmax(1) == y).type(torch.float).sum().item()
            progress = ((e * len(train_dataloader) + i) / (EPOCHS * len(train_dataloader))) * 100
            callback(progress)
        
        writer.add_scalar("Train/Accuracy", train_correct / len(train_dataloader.dataset), e)
        writer.add_scalar("Train/Loss", total_train_loss, e)
        scheduler.step()  
        model.eval()
        print(f"Epoch {e+1}, Train Accuracy: {train_correct / len(train_dataloader.dataset)}")

    with torch.no_grad():
        model.eval()
        preds = []
        test_correct = 0
        
        for x, y in test_dataloader:
            x, y = x.to(device), y.to(device)
            pred = model(x)
            preds.extend(pred.argmax(axis=1).cpu().numpy())
            test_correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    train_accuracy = train_correct / len(train_dataloader.dataset)
    test_accuracy = test_correct / len(test_dataloader.dataset)

    print("Train Accuracy:", train_accuracy)
    print("Test Accuracy:", test_accuracy)
    
    tensors = torch.jit.script(model)
    tensors.save(model_output)
    writer.close()

if __name__ == "__main__":
    train(lambda x: print(f"Progress: {x:.2f}%"))
