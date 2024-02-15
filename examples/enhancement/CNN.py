from abc import ABC

from DNN import DNN
import json
from util.TemplateRenderer import convert_jinja_to_code
from paths import *

class Cnn(DNN, ABC):
    batch_size = None
    learning_rate = None
    csv_path = None
    num_epochs = None
    optimizer = None
    loss_fun = None
    train = True
    layers = []

    def parse_json(self):
        with open('json_files/arch.json', 'r') as f:
            architecture = json.load(f)
            self.layers = architecture['layers']
            
            convert_jinja_to_code(model_jinja_path, model_py_path, {
                'layers': self.layers
            })

            self.misc_params = architecture['misc_params']
            print(self.misc_params)

    def train_build(self):
        convert_jinja_to_code(train_jinja_path, train_py_path, {
            'learning_rate': self.learning_rate,
            'batch_size': self.batch_size,
            'num_epochs': self.num_epochs,
            'optimizer': self.optimizer,
            'loss_func': self.loss_fun
        })

    def BuildModel(self):
        self.parse_json()
        # if self.train == True:
        #     self.train_build()


if __name__ == '__main__':
    model = Cnn()
    model.BuildModel()