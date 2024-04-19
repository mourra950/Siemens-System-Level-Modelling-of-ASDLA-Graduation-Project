from ast import List
import inspect
import torch.nn.modules as nn
import torchvision.models as models


import torch.optim as optim
import types
import copy

statics = [{
    "name": "device", "options": ["cpu", "cuda"],
    "name": "dtype", "options": ["torch.float32"],
    "name": "padding_mode", "options": ['zeros', 'reflect', 'replicate', 'circular'],
}]


class AutoExtraction:

    def __init__(self) -> None:
        print("Auto Extraction")
        self.unnecessary_params = [
            "in_channels", "num_features", "in_features"]
        self.unnecessary_optimizer_params = [
            'params'
        ]

        self.extract_torch_layers()
        self.extract_res_block()
        self.extract_torch_lossfunctions()
        self.extract_torch_optimizers()
        self.extract_pretrained_models()

    def extract_res_block(self):
        res_params = [{
            'name': "in_channels",
            'defaultvalue': 0,
            'type': int
        },
            {
            'name': "out_channels",
            'defaultvalue': 0,
            'type': int
        }
        ]
        res_block_dict = {"Residual Block": res_params}
        self.LAYERS.update(res_block_dict)
        self.LAYERS_WITHOUT_RES = copy.deepcopy(self.LAYERS)
        self.LAYERS_WITHOUT_RES.pop("Residual Block")

    def extract_torch_layers(self) -> dict:
        torch_layers_names = dir(nn)
        torch_layers_dict = dict()

        for layer_name in torch_layers_names:
            obj = getattr(nn, layer_name)

            if (
                isinstance(obj, type)
                and obj is not nn.Module
                and issubclass(obj, nn.Module)
                and "Loss" not in layer_name
                and "1d" not in layer_name
                and "3d" not in layer_name
            ):
                inspector = inspect.signature(obj).parameters
                params_list = list()

                for i in inspector:
                    if (
                        inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD
                        and inspector[i].name not in self.unnecessary_params
                    ):
                        
                        params_list.append(
                            {
                                "name": inspector[i].name,
                                "defaultvalue": inspector[i].default,
                                "type": inspector[i].annotation,
                            }
                        )

                if len(params_list) > 0:
                    torch_layers_dict[obj.__name__] = params_list

        self.LAYERS = torch_layers_dict
        # for Residual blocks

    def extract_torch_lossfunctions(self):
        torch_layers_names = dir(nn)
        torch_layers_dict = dict()

        for layer_name in torch_layers_names:
            obj = getattr(nn, layer_name)

            if (
                isinstance(obj, type)
                and obj is not nn.Module
                and issubclass(obj, nn.Module)
                and "Loss" in layer_name
            ):
                inspector = inspect.signature(obj).parameters
                params_list = list()

                for i in inspector:
                    if (
                        inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD
                        and not
                        isinstance(inspector[i].default, types.FunctionType)
                    ):
                        params_list.append(
                            {
                                "name": inspector[i].name,
                                "defaultvalue": inspector[i].default,
                                "type": inspector[i].annotation,
                            }
                        )

                if len(params_list) > 0:
                    torch_layers_dict[obj.__name__] = params_list

        self.LOSSFUNC = torch_layers_dict

    def extract_torch_optimizers(self):
        torch_optimizers_names = dir(optim)
        torch_optimizers_dict = dict()
        # print(torch_optimizers_names)
        for optimizer_name in torch_optimizers_names:
            obj = getattr(optim, optimizer_name)

            if isinstance(obj, type):
                inspector = inspect.signature(obj).parameters
                params_list = list()

                for i in inspector:

                    if (
                        inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD
                        and
                        inspector[i].name not in self.unnecessary_optimizer_params
                        and not
                        isinstance(inspector[i].default, types.FunctionType)
                    ):
                        # print(inspector[i].annotation,
                        #       type(inspector[i].default))
                        params = None
                        if (inspector[i].annotation == inspect._empty):
                            params = type(inspector[i].default)
                        else:
                            params = inspector[i].annotation

                        params_list.append(
                            {
                                "name": inspector[i].name,
                                "defaultvalue": inspector[i].default,
                                "type": params,
                            }
                        )

                if len(params_list) > 0:
                    torch_optimizers_dict[obj.__name__] = params_list

        self.OPTIMIZERS = torch_optimizers_dict

    def extract_pretrained_models(self):

        # Get a list of all available pre-trained models
        pretrained_models = dir(models)

        # Filter out the models that start with "__" (internal attributes) and those that end with "_"
        self.PRETRAINED_MODELS = [model for model in pretrained_models if not model.startswith(
            "__") and not model.endswith("_") and model[0].islower()]
