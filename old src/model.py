
# import the necessary packages
from torch import nn
class CNN(nn.Module):
    def __init__(self):     
        super(CNN,self).__init__()
    {% for i in layers %}
        {% if i == 'conva' %} 
        self.conva=nn.Conv2d(in_channels=1,out_channels=6,kernel_size=5,padding=0,stride=1)
        {% elif i == 'maxa' %} 
        
        self.maxa=nn.MaxPool2d(2,stride=2,padding=0)
        {% elif i == 'convb' %} 
        
        self.convb=nn.Conv2d(in_channels=6,out_channels=25,kernel_size=5,padding=0,stride=1)
        {% elif i == 'maxb' %} 
        
        self.maxb=nn.MaxPool2d(2,stride=2,padding=0)
        {% elif i == 'fca' %} 
        
        self.fca=nn.Linear(in_features=400*1*1,out_features=10)
        {% elif i == 'relu' %} 
        
        self.relu=nn.ReLU()
        {% endif %}

    {% endfor %}
    def forward(self,x):
      out=self.conva(x)
      out=self.maxa(out)
      out=self.convb(out)
      out=self.maxb(out)
      out= out.view(out.shape[0], -1)
      out=self.fca(out)
      return out

