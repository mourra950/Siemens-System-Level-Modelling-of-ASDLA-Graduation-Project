from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
params_list = [
    'out_channels', 'in_channels', 'add_bias_kv', 'add_zero_attn', 'affine', 'alpha', 'approximate', 'batch_first', "beta", "bias", "bidirectional", "bidirectional", "ceil_mode", "count_include_pad", "cutoffs", "dilation", "dim", "div_value", "divisor_override", "dropout", "elementwise_affine", "embed_dim", "eps", "groups", "head_bias", "hidden_size", "in_features", "init", "inplace", "input_size", "k", "kdim", "kernel_size", "lambd", "lower", "max_val", "min_val", "mode", "momentum", "n_classes", "negative_slope", "nonlinearity", "normalized_shape", "num_features", "num_groups", "num_heads", "num_layers", "num_parameters", "output_ratio", "output_size", "padding", "padding_mode", "proccess_group", "proj_size", "return_indices", "size", "stride", "threshold", "track_running_stats", "upper", "vdim"
]

template_dir = "./templates"

env = Environment(loader=FileSystemLoader(template_dir))

template_filename = "residualBlock.py.jinja"
template = env.get_template(template_filename)
layers = [
    {'name': 'conv1', 'type': 'Conv2d', 'params': {'in_channels': 64, 'out_channels': 128, 'kernel_size': 1, 'stride': 1, 'padding': 0}},
    {'name': 'bn1', 'type': 'BatchNorm2d', 'params': {'num_features': 128}},
    {'name':'relu1','type':'Relu'}
]

result_file = template.render(
    layers=layers
)

# Create or overwrite a file named train.py in output file and outputs the result from the rendered jinja template

f = open("./output/train.py", "w")
f.write(result_file)
f.close()
