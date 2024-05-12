# import the necessary packages
from torch import nn

class CNN(nn.Module):
    def __init__(self):     
        super(CNN,self).__init__()
        {%- for layer in cookiecutter.layers.list %}
        self.{{layer.name}} = nn.{{layer.type}}( {% for param in layer.params %}
            {%- if layer.params[param] is string %}
            {{param}} = {{layer.params[param]|tojson}},
            {%- else %}
            {{param}} = {{layer.params[param]}},
            {%- endif -%}
            {%- endfor %}
        )
        {% endfor %}

    def forward(self, x):
        {% for layer in cookiecutter.layers.list -%}
        x = self.{{layer.name}}(x)
        {% endfor %}
        return x