from abc import ABC

from DNN import DNN
from Layer import Layer
import json
from util.TemplateRenderer import convertJinjaToCode

from torch.utils.tensorboard import SummaryWriter
import torch

class Cnn(DNN, ABC):
    batch_size = None
    learning_rate = None
    csv_path = None
    num_epochs = None
    optimizer = None
    loss_fun = None
    train = True
    layers = []
    jinja_layers = []
    conv_lyr, mxpool_lyr, depthwise_lyr, avgpool_lyr, flatten_lyr, fc_lyr, pointwise_lyr = 'A' * 7

    def parse_json(self):
        with open("input/arch.json", 'r') as f:
            data = json.load(f)

        for layer in data['layers']:
            name = layer['name']
            filters = layer['filters']
            channels = layer['channels']
            height = layer['height']
            width = layer['width']
            kernel_size = layer['kernel_size']
            stride = layer['stride']
            padding = layer['padding']
            units = layer['units']
            layer = Layer(channels, filters, width, height, units, stride, padding, name, kernel_size)
            self.layers.append(layer)
            
        self.batch_size = data['params'][0]['batch_size']
        self.learning_rate = data['params'][0]['learning_rate']
        self.optimizer = data['params'][0]['optimizer']
        self.csv_path = data['params'][0]['csv_path']
        self.loss_fun = data['params'][0]['loss_fun']
        self.num_epochs = data['params'][0]['num_epochs']

    def create_layers(self):
        for layer in self.layers:
            if 'conv' in layer.name:
                ascii = ord(self.conv_lyr)
                current_layer = [{
                    'name': f'conv{self.conv_lyr}',
                    'type': 'Conv2d',
                    'params': {
                        'in_channels': layer.channels,
                        'out_channels': layer.filters,
                        'kernel_size': layer.kernel_size,
                        'padding': layer.padding,
                        'stride': layer.stride
                    }
                }]
                ascii += 1
                self.conv_lyr = chr(ascii)
                
            if 'max' in layer.name:
                current_layer = [{
                    'name': f'max{self.mxpool_lyr}',
                    'type': 'MaxPool2d',
                    'params': {
                        'kernel_size': layer.kernel_size,
                        'padding': layer.padding,
                        'stride': layer.stride
                    }
                }]
                ascii = ord(self.mxpool_lyr)
                ascii += 1
                self.mxpool_lyr = chr(ascii)

            if 'avg' in layer.name:
                current_layer = [{
                    'name': f'avg{self.avgpool_lyr}',
                    'type': 'AvgPool2d',
                    'params': {
                        'kernel_size': layer.kernel_size,
                        'padding': layer.padding,
                        'stride': layer.stride
                    }
                }]
                ascii = ord(self.avgpool_lyr)
                ascii += 1
                self.avgpool_lyr = chr(ascii)

            if 'depthwise' in layer.name:
                current_layer = [
                {
                    'name': f'depth_conv{self.depthwise_lyr}',
                    'type': 'Conv2d',
                    'params': {
                        'in_channels': layer.channels,
                        'out_channels': layer.channels,
                        'kernel_size': layer.kernel_size,
                        'padding': layer.padding,
                        'stride': layer.stride,
                        'groups': layer.channels
                    }
                },
                {
                    'name': f'point_conv{self.pointwise_lyr}',
                    'type': 'Conv2d',
                    'params': {
                        'in_channels': layer.channels,
                        'out_channels': layer.filters,
                        'kernel_size': 1,
                        'padding': 0,
                        'stride': 1,
                    }
                }]
                ascii = ord(self.depthwise_lyr)
                ascii += 1
                self.depthwise_lyr = chr(ascii)
                self.pointwise_lyr = chr(ascii)

            if 'FC' in layer.name:
                current_layer = [{
                    'name': f'fc{self.fc_lyr}',
                    'type': 'Linear',
                    'params': {
                        'in_features': f'{layer.channels}*{layer.height}*{layer.width}',
                        'out_features': layer.filters,
                    }
                }]
                ascii = ord(self.fc_lyr)
                ascii += 1
                self.fc_lyr = chr(ascii)

            self.jinja_layers.extend(current_layer)


        # Add TensorBoard visualization for each layer
            writer.add_graph(torch.nn.Sequential(*current_layer),
                             torch.rand(1, layer.channels, layer.height, layer.width))

        convertJinjaToCode('templates/model.py.jinja', 'output/new_model.py', {
            'layers': self.jinja_layers
        })

    def train_build(self):
        convertJinjaToCode('templates/train.py.jinja', 'output/new_train.py', {
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'epochs': self.num_epochs,
            'optimizer': self.optimizer,
            'loss_func': self.loss_fun
        })

    def BuildModel(self):
        self.parse_json()
        self.create_layers()
        if self.train == True:
            self.train_build()
        
        # Close the SummaryWriter
        writer.close()



model = Cnn()
model.BuildModel()