
# import the necessary packages
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset
from torchvision.datasets import mnist
from torchvision.transforms import ToTensor
from model import CNN


# initiallization
LR = None # <--
BATCH_SIZE = None # <--
EPOCHS = None # <--
TRAIN_SPLIT = 0.75
VAL_SPLIT = 0.15
TEST_SPLIT = 0.1
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = CNN()

train_dataset = mnist.MNIST(root='./train', train=True, download=True, transform=ToTensor())
test_dataset = mnist.MNIST(root='./test', train=False, download=True, transform=ToTensor())
train_dataloader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)
opt = optim.None(model.parameters(), lr=LR) # <--
lossFn = nn.None() # <--

for e in range(0, EPOCHS):
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
        loss = lossFn(pred, y)
        # zero out the gradients, perform the backpropagation step, and update the weights
        opt.zero_grad()
        loss.backward()
        opt.step()
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
	testCorrect=0
	for(x,y) in test_dataloader:
		x=(x.to(device))
		pred = model(x)
		preds.extend(pred.argmax(axis=1).cpu().numpy())
		testCorrect += (pred.argmax(1) == y).type(
				torch.float).sum().item()
		print(testCorrect)
		

# calculate the training, validation, and test accuracy
trainAccuracy = trainCorrect / len(train_dataloader.dataset)
testAccuracy = testCorrect / len(test_dataloader.dataset)

print("Train Accuracy:", trainAccuracy)
print("Test Accuracy:", testAccuracy)

torch.save(model, "model.pt")