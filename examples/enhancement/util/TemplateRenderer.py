from jinja2 import Environment, FileSystemLoader
import os

from util.PathManager import to_absolute


def convert_jinja_to_code(template_relative_path: str, output_relative_path: str, parameters: dict) -> None:
    # get the template path
    template_absolute_path = to_absolute(template_relative_path)
    template_filename = os.path.basename(template_absolute_path)
    template_dir = os.path.dirname(template_absolute_path)

    # define the environment and get the template
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template(template_filename)
    
    # render the template using the defined parameters
    train_code = template.render(parameters)

    # get the output path
    output_absolute_path = to_absolute(output_relative_path)

    # save the rendered template as a .py file
    with open(output_absolute_path, 'w') as f:
        f.write(train_code)