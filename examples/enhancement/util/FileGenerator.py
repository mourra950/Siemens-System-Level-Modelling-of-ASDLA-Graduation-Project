from abc import ABC
import json
import sys
import traceback
import os

stack = traceback.extract_stack()
base_dir = os.path.dirname(stack[0].filename)
absolute_path = os.path.normpath(os.path.join(base_dir, '..'))
sys.path.append(absolute_path)

from config.paths import *
from util.TemplateRenderer import convert_jinja_to_code
from util.PathManager import to_absolute


class FileGenerator(ABC):
    batch_size = None
    learning_rate = None
    csv_path = None
    num_epochs = None
    optimizer = None
    loss_fun = None
    train = True
    layers = []

    def __init__(self, json_path):
        json_path = to_absolute(json_path)
        with open(json_path, 'r') as f:
            architecture = json.load(f)
            self.layers = architecture['layers']
            self.misc_params = architecture['misc_params']

    def generate_model(self, jinja_input_path, python_output_path):
        jinja_input_path = to_absolute(jinja_input_path)
        python_output_path = to_absolute(python_output_path)
        convert_jinja_to_code(jinja_input_path, python_output_path, {
            'layers': self.layers
        })

    def generate_train(self, train_jinja_path, train_py_path):
        convert_jinja_to_code(train_jinja_path, train_py_path, self.misc_params)


if __name__ == '__main__':
    generator = FileGenerator('../json_files/arch.json')
    generator.generate_train(
        '../jinja_templates/train.py.jinja',
        '../python_files/train.py'
    )