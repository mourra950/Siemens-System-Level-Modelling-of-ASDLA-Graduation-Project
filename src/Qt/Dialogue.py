from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QCheckBox,
    QComboBox,
    QMessageBox,
)
import inspect
import typing
import torch

statics = {
    "device": [
        {"text": "In miscelleneous params", "data": "In miscelleneous params"},
    ],
    "dtype": [{"text": "float32", "data": "torch.float32"}],
    "padding_mode": [
        {"text": "zeros", "data": "'zeros'"},
        {"text": "reflect", "data": "'reflect'"},
        {"text": "replicate", "data": "'replicate'"},
        {"text": "circular", "data": "'circular'"},
    ],
    "reduction": [
        {"text": "mean", "data": "'mean'"},
        {"text": "sum", "data": "'sum'"},
    ],
    "nonlinearity": [
        {"text": "tanh", "data": "'tanh'"},
        {"text": "relu", "data": "'relu'"},
    ],
    "mode": [
        {"text": "min", "data": "'min'"},
        {"text": "max", "data": "'max'"},
    ],
    "mode_CyclicLR": [
        {"text": "triangular", "data": "'triangular'"},
        {"text": "triangular2", "data": "'triangular2'"},
        {"text": "exp_range", "data": "'exp_range'"},
    ],
    "threshold_mode": [
        {"text": "rel", "data": "'rel'"},
        {"text": "abs", "data": "'abs'"},
    ],
    "scale_mode": [
        {"text": "cycle", "data": "'cycle'"},
        {"text": "iterations", "data": "'iterations'"},
    ],
    "anneal_strategy": [
        {"text": "cos", "data": "'cos'"},
        {"text": "linear", "data": "'linear'"},
    ],
}
find = [
    "device",
    "dtype",
    "padding_mode",
    "reduction",
    "nonlinearity",
    "mode",
    "mode_CyclicLR",
    "threshold_mode",
    "scale_mode",
    "anneal_strategy",
]


class LayerDialog:

    def create_dialogue_controller(
        self,
        torch_funcs,
        func_name,
        params_names,
        params_value_widgets,
        allParamsColumn_QVBoxLayout,
    ):

        for param in torch_funcs[func_name]:
            if param["name"] in find:
                paramValue_QWidget = QComboBox()
                for i in statics[param["name"]]:
                    print(i)
                    paramValue_QWidget.addItem(i["text"], i["data"])

            else:
                try:
                    try:
                        if bool in param["type"].__args__:
                            paramValue_QWidget = QCheckBox()
                            try:
                                paramValue_QWidget.setChecked(
                                    param["defaultvalue"])
                            except:
                                pass
                        elif int in param["type"].__args__:
                            paramValue_QWidget = QSpinBox(
                                minimum=-1000, maximum=1000)
                            paramValue_QWidget.setValue(0)
                        elif float in param["type"].__args__:
                            paramValue_QWidget = QDoubleSpinBox(
                                minimum=0, maximum=1000)
                            paramValue_QWidget.setSingleStep(0.000000001)
                            paramValue_QWidget.setDecimals(8)
                            paramValue_QWidget.setValue(param["defaultvalue"])
                        else:
                            print(param["type"])
                            paramValue_QWidget = QLineEdit()
                            if (
                                param["defaultvalue"] != inspect._empty
                                and param["defaultvalue"] != None
                            ):
                                paramValue_QWidget.setText(
                                    str(param["defaultvalue"]))
                    except:
                        if (bool == param["type"]) or (
                            typing.Optional[bool] == param["type"]
                        ):
                            paramValue_QWidget = QCheckBox()
                            paramValue_QWidget.setChecked(
                                param["defaultvalue"])
                        elif int == param["type"]:
                            paramValue_QWidget = QSpinBox(
                                minimum=1, maximum=1000)
                            paramValue_QWidget.setValue(param["defaultvalue"])
                        elif float == param["type"]:
                            paramValue_QWidget = QDoubleSpinBox(
                                minimum=0, maximum=1000)
                            paramValue_QWidget.setSingleStep(0.000000001)
                            paramValue_QWidget.setDecimals(8)
                            paramValue_QWidget.setValue(param["defaultvalue"])
                        elif (torch.Tensor == param["type"]) or (
                            typing.Optional[torch.Tensor] == param["type"]
                        ):
                            break
                        else:
                            print(param["type"])
                            paramValue_QWidget = QLineEdit()
                            if (
                                param["defaultvalue"] != inspect._empty
                                and param["defaultvalue"] != None
                            ):
                                paramValue_QWidget.setText(
                                    str(param["defaultvalue"]))
                except:
                    pass
            params_names.append(param["name"])
            params_value_widgets.append(paramValue_QWidget)

            paramRow_QHBoxLayout = QHBoxLayout()
            paramRow_QHBoxLayout.addWidget(QLabel(f'{param["name"]}'))
            paramRow_QHBoxLayout.addWidget(paramValue_QWidget)
            allParamsColumn_QVBoxLayout.addLayout(paramRow_QHBoxLayout)

    def create_dialogue_error(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("error!")
        dlg.setStandardButtons(QMessageBox.Yes)
        dlg.setIcon(QMessageBox.Critical)
        return dlg
