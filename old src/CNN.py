from abc import ABC

from DNN import DNN
from Layer import Layer
import json
import subprocess


class Cnn(DNN, ABC):
    batch_size = None
    learning_rate = None
    csv_path = None
    num_epochs = None
    optimizer = None
    loss_fun = None
    train = True
    layers = []
    (
        conv_lyr,
        mxpool_lyr,
        depthwise_lyr,
        avgpool_lyr,
        flatten_lyr,
        fc_lyr,
        pointwise_lyr,
    ) = (
        "a" * 7
    )
    torch_code = f"""
                        # import the necessary packages
                        from torch import nn\n
    """
    training_code = f"""
    # import the necessary packages
    import torch
    from torch import nn
    from torch.utils.data import DataLoader , TensorDataset
    from torchvision.datasets import mnist
    from torchvision.transforms import ToTensor
    from model import CNN
    from torch.optim import Adadelta
    from torch.optim import Adam\n
    """

    def parse_json(self):
        with open(
            "C:/Users/mourr/OneDrive/Desktop/gradProject-behairy/GP/arch.json", "r"
        ) as f:
            data = json.load(f)

        for layer in data["layers"]:
            name = layer["name"]
            filters = layer["filters"]
            channels = layer["channels"]
            height = layer["height"]
            width = layer["width"]
            kernel_size = layer["kernel_size"]
            stride = layer["stride"]
            padding = layer["padding"]
            units = layer["units"]
            layer = Layer(
                channels,
                filters,
                width,
                height,
                units,
                stride,
                padding,
                name,
                kernel_size,
            )
            self.layers.append(layer)
            # print(layer.name)
        self.batch_size = data["params"][0]["batch_size"]
        self.learning_rate = data["params"][0]["learning_rate"]
        self.optimizer = data["params"][0]["optimizer"]
        self.csv_path = data["params"][0]["csv_path"]
        self.loss_fun = data["params"][0]["loss_fun"]
        self.num_epochs = data["params"][0]["num_epochs"]

    def create_layers(self):
        self.forward = "    def forward(self,x):\n"
        self.torch_code += f"""class CNN(nn.Module):
        def __init__(self):     
        super(CNN,self).__init__()\n"""
        print(self.layers[0])
        for layer in self.layers:
            if "conv" in layer.name:
                ascii = ord(self.conv_lyr)
                self.torch_code += f"""        self.conv{self.conv_lyr}=nn.Conv2d(in_channels={layer.channels},out_channels={layer.filters},kernel_size={layer.kernel_size},padding={layer.padding},stride={layer.stride})\n"""
                if self.layers.index(layer) == 0:
                    self.forward += f"      out=self.conv{self.conv_lyr}(x)\n"
                else:
                    self.forward += f"      out=self.conv{self.conv_lyr}(out)\n"
                ascii += 1
                self.conv_lyr = chr(ascii)
            if "max" in layer.name:
                ascii = ord(self.mxpool_lyr)
                self.torch_code += f"""        self.max{self.mxpool_lyr}=nn.MaxPool2d({layer.kernel_size},stride={layer.stride},padding={layer.padding})\n"""
                if self.layers.index(layer) == 0:
                    self.forward += f"      out=self.max{self.mxpool_lyr}(x)\n"
                else:
                    self.forward += f"      out=self.max{self.mxpool_lyr}(out)\n"
                ascii += 1
                self.mxpool_lyr = chr(ascii)
            if "avg" in layer.name:
                ascii = ord(self.avgpool_lyr)
                self.torch_code += f"""        self.avg{self.avgpool_lyr}=nn.AvgPool2d({layer.kernel_size},stride={layer.stride},padding={layer.padding})\n"""
                if self.layers.index(layer) == 0:
                    self.forward += f"      out=self.avg{self.avgpool_lyr}(x)\n"
                else:
                    self.forward += f"      out=self.avg{self.avgpool_lyr}(out)\n"
                ascii += 1
                self.avgpool_lyr = chr(ascii)
            if "depthwise" in layer.name:
                ascii = ord(self.depthwise_lyr)
                self.torch_code += f"""        self.depth_conv{self.depthwise_lyr}=nn.Conv2d(in_channels={layer.channels},out_channels={layer.channels},kernel_size={layer.kernel_size},padding={layer.padding},stride={layer.stride},groups={layer.channels})\nself.point_conv{self.pointwise_lyr}=nn.Conv2d(in_channels={layer.channels},out_channels={layer.filters},kernel_size=1,padding=0,stride=1)\n"""
                if self.layers.index(layer) == 0:
                    self.forward += f"      out=self.depth_conv{self.conv_lyr}(x)\nself.point_conv{self.pointwise_lyr}(x)\n"
                else:
                    self.forward += f"      out=self.depth_conv{self.conv_lyr}(x)\nself.point_conv{self.pointwise_lyr}(out)\n"

                ascii += 1
                self.depthwise_lyr = chr(ascii)
                self.pointwise_lyr = chr(ascii)
            if "FC" in layer.name:
                ascii = ord(self.fc_lyr)
                self.torch_code += f"""        self.fc{self.fc_lyr}=nn.Linear(in_features={layer.channels}*{layer.height}*{layer.width},out_features={layer.filters})\n"""
                if self.fc_lyr == "a":
                    self.forward += f"""      out= out.view(out.shape[0], -1)\n"""
                if self.layers.index(layer) == 0:
                    self.forward += f"      out=self.fc{self.fc_lyr}(x)\n"
                else:
                    self.forward += f"      out=self.fc{self.fc_lyr}(out)\n"
                ascii += 1
                self.fc_lyr = chr(ascii)
        self.torch_code += "        self.relu=nn.ReLU()\n"
        self.forward += "      return out\n\n"
        self.torch_code += self.forward
        file = open("model.py", "w")
        file.write(self.torch_code)

    def train_build(self):
        self.training_code += f'''
#df = pd.read_csv(f'csv_path', header=None)
#x = df.iloc[:, :-1]
#y = df.iloc[:, -1]
#x = torch.tensor(x.values)
#y = torch.tensor(y.values)
#dataset=TensorDataset(x,y)
#size = len(df)
#initiallization
LR = {self.learning_rate}
BATCH_SIZE = {self.batch_size}
EPOCHS = {self.num_epochs}
TRAIN_SPLIT = 0.75
VAL_SPLIT = 0.15
TEST_SPLIT = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN()
#size=dataset.__len__()
#train_dataset, val_dataset, test_dataset = random_split(dataset, [size*TRAIN_SPLIT, size*VAL_SPLIT, size*TEST_SPLIT],generator=torch.Generator().manual_seed(42))
train_dataset = mnist.MNIST(root='./train', train=True, transform=ToTensor())
test_dataset = mnist.MNIST(root='./test', train=False, transform=ToTensor())
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
#val_dataloader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
opt = {self.optimizer}(model.parameters(), lr={self.learning_rate})
lossFn = nn.{self.loss_fun}()
for e in range(0, EPOCHS):
    # set the model in training mode
    model.train()
    # initialize the total training and validation loss
    totalTrainLoss = 0
    totalValLoss = 0
    # initialize the number of correct predictions in the training
    # and validation step
    trainCorrect = 0
    valCorrect = 0
    # loop over the training set
    for (x, y) in train_dataloader:
        # send the input to the device
        (x, y) = (x.to(device), y.to(device))
        # perform a forward pass and calculate the training loss
        pred = model(x)
        loss = lossFn(pred, y)
        # zero out the gradients, perform the backpropagation step,
        # and update the weights
        opt.zero_grad()
        loss.backward()
        opt.step()
        # add the loss to the total training loss so far and
        # calculate the number of correct predictions
        totalTrainLoss += loss
        trainCorrect += (pred.argmax(1) == y).type(
            torch.float).sum().item()
    model.eval()
    print(trainCorrect)
"""
# switch off autograd for evaluation
with torch.no_grad():
		# set the model in evaluation mode
		model.eval()
		# loop over the validation set
		for (x, y) in val_dataloader:
			# send the input to the device
			(x, y) = (x.to(device), y.to(device))
			# make the predictions and calculate the validation loss
			pred = model(x)
			totalValLoss += lossFn(pred, y)
			# calculate the number of correct predictions
			valCorrect += (pred.argmax(1) == y).type(
				torch.float).sum().item()  
	# calculate the training and validation accuracy
	trainCorrect = trainCorrect / len(trainDataLoader.dataset)
	valCorrect = valCorrect / len(valDataLoader.dataset)
	"""
with torch.no_grad():
	model.eval()
	# initialize a list to store our predictions
	preds = []
	testCorrect=0
	for(x,y) in test_dataloader:
		x=(x.to(device))
		pred =model(x)
		preds.extend(pred.argmax(axis=1).cpu().numpy())
		testCorrect += (pred.argmax(1) == y).type(
				torch.float).sum().item()
		print(testCorrect)
		

# calculate the training, validation, and test accuracy
trainAccuracy = trainCorrect / len(train_dataloader.dataset)
valAccuracy = valCorrect / len(val_dataloader.dataset)
testAccuracy = testCorrect / len(test_dataloader.dataset)

print("Train Accuracy:", trainAccuracy)
print("Validation Accuracy:", valAccuracy)
print("Test Accuracy:", testAccuracy)

torch.save(model, "model.pt")

    
'''
        file = open("train.py", "w")
        file.write(self.training_code)

    def BuildModel(self):
        self.parse_json()
        self.create_layers()
        if self.train == True:
            self.train_build()


model = Cnn()
model.BuildModel()
