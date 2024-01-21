from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
import os
params_list = [
    'out_channels', 'in_channels', 'add_bias_kv', 'add_zero_attn', 'affine', 'alpha', 'approximate', 'batch_first', "beta", "bias", "bidirectional", "bidirectional", "ceil_mode", "count_include_pad", "cutoffs", "dilation", "dim", "div_value", "divisor_override", "dropout", "elementwise_affine", "embed_dim", "eps", "groups", "head_bias", "hidden_size", "in_features", "init", "inplace", "input_size", "k", "kdim", "kernel_size", "lambd", "lower", "max_val", "min_val", "mode", "momentum", "n_classes", "negative_slope", "nonlinearity", "normalized_shape", "num_features", "num_groups", "num_heads", "num_layers", "num_parameters", "output_ratio", "output_size", "padding", "padding_mode", "proccess_group", "proj_size", "return_indices", "size", "stride", "threshold", "track_running_stats", "upper", "vdim"
]

template_dir = "./templates"

env = Environment(loader=FileSystemLoader(template_dir))

template_filename = "template.py.jinja"
template = env.get_template(template_filename)

channel = 2
result_file = template.render(
    layers=[{'layer': 'Conv1d', 'params': {
        'in_channels': '3', 'out_channels': '8'}}, {'layer': 'Conv1d', 'params': {
            'in_channels': '5'}}],
    params_list=params_list
)

# Create or overwrite a file named train.py in output file and outputs the result from the rendered jinja template

f = open("./output/train.py", "w")
f.write(result_file)
f.close()
