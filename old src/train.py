# import the necessary packages
import torch
from torch import nn
from torch.utils.data import DataLoader, TensorDataset
from torchvision.datasets import mnist
from torchvision.transforms import ToTensor
from model import CNN
from torch.optim import Adadelta
from torch.optim import Adam

# df = pd.read_csv(f'csv_path', header=None)
# x = df.iloc[:, :-1]
# y = df.iloc[:, -1]
# x = torch.tensor(x.values)
# y = torch.tensor(y.values)
# dataset=TensorDataset(x,y)
# size = len(df)
# initiallization
LR = 0.01
BATCH_SIZE = 256
EPOCHS = 1
TRAIN_SPLIT = 0.75
VAL_SPLIT = 0.15
TEST_SPLIT = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN()
# size=dataset.__len__()
# train_dataset, val_dataset, test_dataset = random_split(dataset, [size*TRAIN_SPLIT, size*VAL_SPLIT, size*TEST_SPLIT],generator=torch.Generator().manual_seed(42))
train_dataset = mnist.MNIST(root="./train", train=True, transform=ToTensor())
test_dataset = mnist.MNIST(root="./test", train=False, transform=ToTensor())
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
# val_dataloader = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)
test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
opt = Adadelta(model.parameters(), lr=0.01)
lossFn = nn.L1Loss()
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
    for x, y in train_dataloader:
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
        trainCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
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
    testCorrect = 0
    for x, y in test_dataloader:
        x = x.to(device)
        pred = model(x)
        preds.extend(pred.argmax(axis=1).cpu().numpy())
        testCorrect += (pred.argmax(1) == y).type(torch.float).sum().item()
        print(testCorrect)


# calculate the training, validation, and test accuracy
trainAccuracy = trainCorrect / len(train_dataloader.dataset)
valAccuracy = valCorrect / len(val_dataloader.dataset)
testAccuracy = testCorrect / len(test_dataloader.dataset)

print("Train Accuracy:", trainAccuracy)
print("Validation Accuracy:", valAccuracy)
print("Test Accuracy:", testAccuracy)

torch.save(model, "model.pt")
