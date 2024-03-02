import torch
import torch.nn as nn
class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        self.conv1 = nn.Conv2d(
            in_channels=in_channels,out_channels=out_channels, 
            kernel_size=1,stride=1,padding=0,
        )
        self.bn1 = nn.BatchNorm2d(
            num_features=out_channels,
        )
        self.conv2 = nn.Conv2d(
            in_channels=out_channels,out_channels=out_channels,kernel_size=3,stride=1,padding=1,
        )
        self.bn2 = nn.BatchNorm2d(
            num_features=out_channels,
        )
        self.conv3 = nn.Conv2d(
            in_channels=out_channels,out_channels=in_channels, 
            kernel_size=1,stride=1,padding=0,
        )
        self.bn3 = nn.BatchNorm2d(
            num_features=in_channels,
        )
        self.relu = nn.ReLU(
        )


    def forward(self, x):
        identity = x
        
        x = self.conv1(x)
        
        x = self.bn1(x)
        
        x = self.conv2(x)
        
        x = self.bn2(x)
        
        x = self.conv3(x)
        
        x = self.bn3(x)
        
        x = self.relu(x)
        
        x += identity

        return x