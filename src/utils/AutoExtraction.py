from ast import List
import inspect
import torch.nn.modules as nn
import torch.optim as optim

class AutoExtraction:

    def __init__(self) -> None:
        print("Auto Extraction")
        self.unnecessary_params = ["in_channels", "num_features", "in_features"]
        self.extract_torch_layers()
        self.extract_torch_lossfunctions()
        self.extract_torch_optimizers()
        

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

        self.LAYERS=torch_layers_dict


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
                    if inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD:
                        params_list.append(
                            {
                                "name": inspector[i].name,
                                "defaultvalue": inspector[i].default,
                                "type": inspector[i].annotation,
                            }
                        )

                if len(params_list) > 0:
                    torch_layers_dict[obj.__name__] = params_list

        self.LOSSFUNC=torch_layers_dict


    def extract_torch_optimizers(self):
        torch_optimizers_names = dir(optim)
        torch_optimizers_dict = dict()

        for optimizer_name in torch_optimizers_names:
            obj = getattr(optim, optimizer_name)

            if isinstance(obj, type):
                inspector = inspect.signature(obj).parameters
                params_list = list()

                for i in inspector:
                    if inspector[i].kind == inspect._ParameterKind.POSITIONAL_OR_KEYWORD:
                        params_list.append(
                            {
                                "name": inspector[i].name,
                                "defaultvalue": inspector[i].default,
                                "type": inspector[i].annotation,
                            }
                        )

                if len(params_list) > 0:
                    torch_optimizers_dict[obj.__name__] = params_list

        self.OPTIMIZERS=torch_optimizers_dict


