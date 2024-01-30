from util.TemplateRenderer import convertJinjaToCode

layers = [
    {'name': 'conv1', 'type': 'Conv2d', 'params': {'in_channels': 64, 'out_channels': 128, 'kernel_size': 1, 'stride': 1, 'padding': 0}},
    {'name': 'bn1', 'type': 'BatchNorm2d', 'params': {'num_features': 128}},
    {'name':'relu1','type':'ReLU'}
]

layers1 = [
    {
        'name': 'conv1',
        'type': 'Conv2d',
        'params': {
            'kernel_size': 1,
            'stride': 1,
            'padding': 0
        }
    },
    {
        'name': 'bn1',
        'type': 'BatchNorm2d',
        'params': {}
    },
    
    {
        'name': 'conv2',
        'type': 'Conv2d',
        'params': {
            'kernel_size': 3,
            'stride': 1,
            'padding': 1
        }
    },
    {
        'name': 'bn2',
        'type': 'BatchNorm2d',
        'params': {}
    },

    {
        'name': 'conv3',
        'type': 'Conv2d',
        'params': {
            'kernel_size': 1,
            'stride': 1,
            'padding': 0
        }
    },
    {
        'name': 'bn3',
        'type': 'BatchNorm2d',
        'params': {}
    },

    {
        'name': 'relu',
        'type': 'ReLU',
        'params': {}
    },
]

convertJinjaToCode('templates/residualBlock.py.jinja', 'output/residual.py',
    {
        'layers': layers1
    }                   
)