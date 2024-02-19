from abc import ABC
import json

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

    # def generate_train(self):
    #     convert_jinja_to_code(train_jinja_path, train_py_path, {
    #         'learning_rate': self.learning_rate,
    #         'batch_size': self.batch_size,
    #         'num_epochs': self.num_epochs,
    #         'optimizer': self.optimizer,
    #         'loss_func': self.loss_fun
    #     })

    def BuildModel(self):
        self.generate_model()
        # if self.train == True:
        #     self.generate_train()