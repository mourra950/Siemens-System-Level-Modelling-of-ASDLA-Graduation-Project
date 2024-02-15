
# import the necessary packages
from torch import nn

class CNN(nn.Module):
    def __init__(self):     
        super(CNN,self).__init__()
        self.conv2d_1 = nn.Conv2d( 
            out_channels = 128,
            kernel_size = 3,
            stride = 1,
            padding = 0,
            dilation = 1,
            groups = 1,
            bias = True,
            padding_mode = "zeros",
            in_channels = 3,
        )
        
        self.relu_1 = nn.ReLU( 
            inplace = False,
        )
        
        self.flatten_1 = nn.Flatten( 
            start_dim = 0,
            end_dim = -1,
        )
        
        self.linear_1 = nn.Linear( 
            out_features = 100,
            bias = True,
            in_features = 86528,
        )
        
        self.linear_2 = nn.Linear( 
            out_features = 4,
            bias = True,
            in_features = 100,
        )
        

    def forward(self, x):
        x = self.conv2d_1(x)
        x = self.relu_1(x)
        x = self.flatten_1(x)
        x = self.linear_1(x)
        x = self.linear_2(x)
        
        return x