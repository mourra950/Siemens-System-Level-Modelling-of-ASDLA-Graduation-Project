from PySide6.QtWidgets import (
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QSpinBox,
    QDoubleSpinBox,
    QCheckBox,
    QComboBox,
)
import inspect
import typing

statics = {
    "device": [
        {"text": "cpu", "data": "'cpu'"},
        {"text": "cuda", "data": "'cuda'"},
    ],
    "dtype": [{"text": "float32", "data": "torch.float32"}],
    "padding_mode": [
        {"text": "zeros", "data": "'zeros'"},
        {"text": "reflect", "data": "'reflect'"},
        {"text": "replicate", "data": "'replicate'"},
        {"text": "circular", "data": "'circular'"},
    ],
    "reduction":[
        {"text": "none", "data": "'none'"},
        {"text": "mean", "data": "'mean'"},
        {"text": "sum", "data": "'sum'"},
    ]
}
find = ["device", "dtype", "padding_mode","reduction"]


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
                    if bool in param["type"].__args__:
                        paramValue_QWidget = QCheckBox()
                        try:
                            paramValue_QWidget.setChecked(param["defaultvalue"])
                        except:
                            pass
                    elif int in param["type"].__args__:
                        paramValue_QWidget = QSpinBox(minimum=-1000, maximum=1000)
                        paramValue_QWidget.setValue(0)
                    else:
                        paramValue_QWidget = QLineEdit()
                        if (
                            param["defaultvalue"] != inspect._empty
                            and param["defaultvalue"] != None
                        ):
                            paramValue_QWidget.setText(str(param["defaultvalue"]))
                except:
                    if (bool == param["type"]) or (
                        typing.Optional[bool] == param["type"]
                    ):
                        paramValue_QWidget = QCheckBox()
                        paramValue_QWidget.setChecked(param["defaultvalue"])
                    elif int == param["type"]:
                        paramValue_QWidget = QSpinBox(minimum=1, maximum=1000)
                        paramValue_QWidget.setValue(0)
                    elif float == param["type"]:
                        paramValue_QWidget = QDoubleSpinBox(minimum=0, maximum=1000)
                        paramValue_QWidget.setSingleStep(0.00000001)
                        paramValue_QWidget.setDecimals(8)
                        paramValue_QWidget.setValue(0.00)

                    else:
                        paramValue_QWidget = QLineEdit()
                        if (
                            param["defaultvalue"] != inspect._empty
                            and param["defaultvalue"] != None
                        ):
                            paramValue_QWidget.setText(str(param["defaultvalue"]))

            params_names.append(param["name"])
            params_value_widgets.append(paramValue_QWidget)

            paramRow_QHBoxLayout = QHBoxLayout()
            paramRow_QHBoxLayout.addWidget(QLabel(f'{param["name"]}'))
            paramRow_QHBoxLayout.addWidget(paramValue_QWidget)
            allParamsColumn_QVBoxLayout.addLayout(paramRow_QHBoxLayout)
