# import the necessary packages
import torch
from torch import nn

class CNN(nn.Module):
    def __init__(self):     
        super(CNN,self).__init__()
        {%- for layer in cookiecutter.layers.list %}
        self.{{layer.name}} = nn.{{layer.type}}( {% for param in layer.params %}
            {{param}} = {{layer.params[param]}},
        {%- endfor %}
        )
        {% endfor %}

    def forward(self, x):
        {% for layer in cookiecutter.layers.list -%}
        x = self.{{layer.name}}(x)
        {% endfor %}
        return x