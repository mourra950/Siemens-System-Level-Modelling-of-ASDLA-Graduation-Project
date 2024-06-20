import json
import os
from PySide6.QtWidgets import QMessageBox, QSpinBox, QFileDialog, QLineEdit, QComboBox
from Classes.Parameters_folder.Miscellaneous import Miscellaneous
from Classes.Parameters_folder.Optimizer import Optimizer
from Classes.Parameters_folder.LossFunction import LossFunction
from Classes.Parameters_folder.Scheduler import Scheduler
from Classes.Parameters_folder.Pretrained import Pretrained

from Classes.Parameters_folder.Layers_System.Layers_System import Layers_System

from Classes.Children import Children
from paths.SystemPaths import SystemPaths


class Parameters:
    def __init__(self) -> None:
        self.Children = Children()
        self.SysPath = SystemPaths()
        # optimizer
        self.Misc_params = Miscellaneous()

        self.Optim_params = Optimizer()
        # loss_func
        self.LossFunc_params = LossFunction()
        # scheduler
        self.Scheduler_params = Scheduler()
        # layers
        self.Layers_System = Layers_System()
        # pretrained
        self.Pretrained = Pretrained()
        self.layers = []
        self.connections()

    def connections(self):
        self.Children.qt_actionLoad.triggered.connect(self.load_configs)

    def create_architecture(self):
        self.architecture = {
            'layers': self.Layers_System.layers,
            'misc_params': self.Misc_params.miscellaneous,
            'optimizer': self.Optim_params.optimizer,
            'loss_func': self.LossFunc_params.loss_function,
            'scheduler': self.Scheduler_params.scheduler,
            'pretrained': self.Pretrained.pretrained
        }
        return self.architecture

    def load_configs(self):
        path_arch_json, _ = QFileDialog.getOpenFileName(
            None, "Load configuration file",  self.SysPath.jsondir, "JSON Files (*.json)"
        )
        if path_arch_json:
            with open(path_arch_json, "r") as json_file:
                temp = json.load(json_file)
                # misc
                self.Misc_params.load_from_config(temp)
                # optimizer
                self.Optim_params.load_from_config(temp)
                # loss_func
                self.LossFunc_params.load_from_config(temp)
                # scheduler
                self.Scheduler_params.load_from_config(temp)
                # layers
                self.Layers_System.load_from_config(temp)
