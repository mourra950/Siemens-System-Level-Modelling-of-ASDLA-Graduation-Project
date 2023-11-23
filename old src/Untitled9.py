#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import torch.nn as nn
import torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc = nn.Linear(2, 2)

    def forward(self, x):
        x = self.fc(x)
        return x

# Create a simple net
net = SimpleNet()

# Define a loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.01)

# Create some random data
x = torch.randn(100, 2)
y = torch.randint(2, (100,))

# Train the network
for epoch in range(1000):
    optimizer.zero_grad()
    output = net(x)
    loss = criterion(output, y)
    loss.backward()
    optimizer.step()

# Print the final accuracy
_, predicted = torch.max(output, 1)
accuracy = (predicted == y).sum().item() / len(y)
print('Final accuracy:', accuracy)


# In[ ]:




