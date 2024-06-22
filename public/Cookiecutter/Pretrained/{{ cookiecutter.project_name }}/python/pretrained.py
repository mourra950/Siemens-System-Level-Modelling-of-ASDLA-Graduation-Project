# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from torchvision import models, transforms, datasets
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
{% if cookiecutter.misc_params.dataset.value == "CustomDataset" %}
class CustomDataset(Dataset):
    def __init__(self, root, transform=None, download=None, train=None):
        self.root = root
        self.transform = transform
        self.data = self.load_data()

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root, self.data[idx]['filename'])
        image = Image.open(img_name).convert('RGB')
        label = int(self.data[idx]['label'])

        if self.transform:
            image = self.transform(image)

        return image, label

    def load_data(self):
        json_file = glob.glob(os.path.join(self.root,"*.json"))[0]
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data
{%- endif %}

def train(callback, logdir):
    # initialization
    unique_name = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    base_log_dir = logdir
    log_dir = os.path.join(base_log_dir, unique_name)

    writer = SummaryWriter(log_dir=log_dir, comment="Pretrained_Model")
    HEIGHT = {{cookiecutter.misc_params.height}}
    WIDTH = {{cookiecutter.misc_params.width}}
    BATCH_SIZE = {{cookiecutter.misc_params.batch_size}}
    EPOCHS = {{cookiecutter.misc_params.num_epochs}}
    TRAIN_SPLIT = 0.75
    VAL_SPLIT = 0.15
    TEST_SPLIT = 0.1
    device = torch.device("{{cookiecutter.misc_params.device.value}}")
    model = models.{{cookiecutter.pretrained.value}}(weights='DEFAULT')

    for name, param in model.named_parameters():
        print(param.shape)
        batch = param.shape[0]
        channels = param.shape[1]
        break

    for param in model.parameters():
        param.requires_grad = False

    transform = transforms.Compose(
        [
            v2.Resize((HEIGHT, WIDTH)),
            # Convert images to RGB format
            v2.Grayscale(num_output_channels=channels),
            # Convert images to PyTorch tensors
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
            v2.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
        ]
    )

    {% if cookiecutter.misc_params.dataset.value == "CustomDataset" %}
    train_dataset = {{cookiecutter.misc_params.dataset.value}}(root=r"{{cookiecutter.misc_params.dataset_path}}",
                                                      train=True, download=True, transform=transform)
    {% else %}
    train_dataset = datasets.{{cookiecutter.misc_params.dataset.value}}(root=r"{{cookiecutter.misc_params.dataset_path}}",
                                                      train=True, download=True, transform=transform)
    {%- endif %}
    test_dataset = datasets.{{cookiecutter.misc_params.dataset.value}}(root=r"{{cookiecutter.misc_params.dataset_path}}",
                                                                       train=False, download=True, transform=transform)

    train_dataloader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True, pin_memory=True
    )
    test_dataloader = DataLoader(
        test_dataset, batch_size=BATCH_SIZE, shuffle=False, pin_memory=True
    )

    loss_fn = nn.{{cookiecutter.loss_func.type}}(
    {% for key, value in cookiecutter.loss_func.params|dictsort %}
        {{key}}={{value}},
    {% endfor %}
    )

    class_names = train_dataset.classes

    try:
        model.aux.logits = False
    except:
        pass
    # model.fc.in_features
    (name, layer) = list(model.named_children())[-1]
    if type(layer) == type(nn.Sequential()):
        (i, j) = list(layer.named_children())[-1]
        model.__dict__['_modules'][name].__dict__['_modules'][i] = nn.Linear(
            j.in_features, len(class_names), device=device)
    else:
        model.__dict__['_modules'][name] = nn.Linear(
            layer.in_features, len(class_names), device=device
        )

    model = model.to(device)

    # Create the chosen optimizer with parameters from the data dictionary
    optimizer = optim.{{cookiecutter.optimizer.type}}(
        [{"params": model.parameters(), "initial_lr": {{cookiecutter.optimizer.params.lr}}}]
        {%- for key, value in cookiecutter.optimizer.params|dictsort %}
        {%- if value is sequence and value is not string -%}, {{key}}=({{value | join(', ')}})
        {%- else -%}, {{key}}={{value}}
        {%- endif %}
        {%- endfor %}
    )

    train_size = len(train_dataset)

    {% if cookiecutter.scheduler.type != "None" %}
    # Create the chosen scheduler with parameters
    scheduler = {{cookiecutter.scheduler.type}}(optimizer,
                                                {%- for key, value in cookiecutter.scheduler.params|dictsort %}
        {%- if value is sequence and value is not string -%}
        {{key}}=({{value | join(', ')}}),
        {%- else -%}
        {{key}}={{value}},
        {%- endif %}
        {%- endfor %}
    )
    {% endif %}
    for e in range(0, EPOCHS):
        model.train()
        totalTrainLoss = 0
        trainCorrect = 0
        data_iter = iter(train_dataloader)
        images, labels = next(data_iter)
        grid = torchvision.utils.make_grid(images)
        writer.add_image("Input Images", grid, e)
        for i, (x, y) in enumerate(train_dataloader):
            (x, y) = (x.to(device), y.to(device))
            pred = model(x)
            loss = loss_fn(pred, y)
            writer.add_scalar("Loss/train", loss.item(),
                              e * len(train_dataloader) + i)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            totalTrainLoss += loss.item()
            trainCorrect += (pred.argmax(1) ==
                             y).type(torch.float).sum().item()
            progress = ((e * len(train_dataloader) + i) /
                        (EPOCHS * len(train_dataloader))) * 100
            callback(progress)

        writer.add_scalar("Train/Accuracy", trainCorrect /
                          len(train_dataloader.dataset), e)
        writer.add_scalar("Train/Loss", totalTrainLoss, e)

        # Skip scheduler step if {{cookiecutter.scheduler.type}} is None
        {% if cookiecutter.scheduler.type != "None" %}
        scheduler.step()
        {% endif %}

        model.eval()
        print(
            f"Epoch {e+1}, Train Accuracy: {trainCorrect / len(train_dataloader.dataset)}")

    dummy_input = torch.randn(3, channels, HEIGHT, WIDTH).to(
        device)  # Example input tensor
    writer.add_graph(model, dummy_input)

    with torch.no_grad():
        model.eval()
        preds = []
        testCorrect = 0

        for x, y in test_dataloader:
            x = x.to(device)
            y = y.to(device)
            pred = model(x)
            preds.extend(pred.argmax(axis=1).cpu().numpy())
            testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()

    trainAccuracy = trainCorrect / len(train_dataloader.dataset)
    testAccuracy = testCorrect / len(test_dataloader.dataset)

    print("Train Accuracy:", trainAccuracy)
    print("Test Accuracy:", testAccuracy)

    scripted = torch.jit.script(model)
    try:
        torch.jit.save(scripted, model_output)
    except e:
        print(e)
    writer.close()


if __name__ == "__main__":
    train()
