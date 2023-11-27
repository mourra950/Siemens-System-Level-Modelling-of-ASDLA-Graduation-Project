from jinja2 import Environment, FileSystemLoader
import os

# define model hyperparameters
parameters = {
    'learning_rate': 0.01,
    'batch_size': 256,
    'epochs': 1,
    'optimizer': 'Adadelta',
    'loss_func': 'L1Loss'
}

# define the template path
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')
template_filename = 'train.py.jinja'

# define the environment and get the template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_filename)

# render the template using the defined parameters
train_code = template.render(parameters)
print(train_code)

# define the output path
output_dir = os.path.join(base_dir, 'output')
output_filename = 'train.py'
output_path = os.path.join(output_dir, output_filename)

# save the rendered template as a .py file
with open(output_path, 'w') as f:
    f.write(train_code)