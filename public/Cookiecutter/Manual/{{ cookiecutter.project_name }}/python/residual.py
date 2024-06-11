import torch
import torch.nn as nn


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels):
        super(ResidualBlock, self).__init__()
        {%- set last_conv_idx = [] -%}
        {%- for layer in cookiecutter.residual.layers.list -%}
        {%- if layer.type == 'Conv2d' -%}
        {%- set temp = last_conv_idx.append(loop.index) -%}
        {%- endif -%}
        {%- endfor -%}

        {% for layer in cookiecutter.residual.layers.list %}
        self.{{ layer.name }} = nn.{{ layer.type }}(
            {%- if layer.type == 'Conv2d' and last_conv_idx|length == 1 %}
            in_channels=in_channels,
            out_channels=in_channels,
            {%- elif layer.type == 'Conv2d' and loop.index+1 == last_conv_idx[0] and last_conv_idx|length > 1 %}
            in_channels=in_channels,
            out_channels=out_channels,
            {%- elif layer.type == 'Conv2d' and loop.index+1 == last_conv_idx[-1] and last_conv_idx|length > 1 %}
            in_channels=out_channels,
            out_channels=in_channels,
            {% elif layer.type == 'Conv2d' %}
            in_channels=out_channels,
            out_channels=out_channels,

            {%- elif layer.type == 'BatchNorm2d' and loop.index+1 < last_conv_idx[-1] %}
            num_features=out_channels, 
            {%- elif layer.type == 'BatchNorm2d' and loop.index+1 > last_conv_idx[-1] %}
            num_features=in_channels, 
            {%- endif -%}

            {% for param in layer.params -%}
            {%- if param != 'out_channels' %}
            {{ param }}={{ layer.params[param] }},
            {%- endif %}
            {%- endfor %}
        )
        {%- endfor %}


    def forward(self, x):
        identity = x
        {% for layer in cookiecutter.residual.layers.list %}
        x = self.{{ layer.name }}(x)
        {% endfor %}
        x += identity

        return x