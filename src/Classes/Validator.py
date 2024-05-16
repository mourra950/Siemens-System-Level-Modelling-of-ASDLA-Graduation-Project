class Validator:
    def validate_and_correct_layers(self, architecture):
        width = architecture['misc_params']['width']
        height = architecture['misc_params']['height']
        channels = architecture['misc_params']['channels']
        if self.debug:
            print(
                f'width: {width}, height: {height}, channels: {channels},architecture: {architecture}')
        features_after_1st_FC = None
        flattened = False
        layer_freqs = dict()
        i = 0

        while i < len(architecture['layers']):
            layer = architecture['layers'][i]
            params = layer['params']
            layer_type = layer['type']
            self.add_layer_name(layer, layer_freqs)

            if layer_type == 'Conv2d':
                params['in_channels'] = channels
                width = (width - params['kernel_size'] + 2 *
                         params['padding']) // params['stride'] + 1
                height = (height - params['kernel_size'] +
                          2*params['padding']) // params['stride'] + 1
                channels = params['out_channels']
            elif layer_type == 'MaxPool2d' or layer_type == 'AvgPool2d':
                width = (width - params['kernel_size']) // params['stride'] + 1
                height = (height - params['kernel_size']
                          ) // params['stride'] + 1
            elif layer_type == 'Linear':
                if not flattened:
                    flattened = True
                    flatten = {
                        'type': 'Flatten',
                        'params': {
                            'start_dim': 0,
                            'end_dim': -1
                        }
                    }
                    if i > 0 and architecture['layers'][i-1]['type'] == 'Flatten':
                        architecture['layers'][i -
                                               1]['params'] = flatten['params']
                    else:
                        self.create_layer_node(flatten, i)
                        self.add_layer_name(flatten, layer_freqs)
                        i += 1
                if features_after_1st_FC is not None:
                    params['in_features'] = features_after_1st_FC
                else:
                    params['in_features'] = int(channels * width * height)
                features_after_1st_FC = params['out_features']
            elif layer_type == 'BatchNorm2d':
                params['num_features'] = channels
            elif layer_type == 'Flatten':
                if params['start_dim'] == 0 and params['end_dim'] == -1:
                    flattened = True
            i += 1

    def add_layer_name(self, layer, layer_freqs):
        if layer['type'] in layer_freqs:
            layer_freqs[layer['type']] += 1
        else:
            layer_freqs[layer['type']] = 1
        layer['name'] = f'{layer["type"].lower()}_{layer_freqs[layer["type"]]}'
