from PySide6.QtWidgets import QLineEdit, QSpinBox, QComboBox, QPushButton
from utils.AutoExtraction import AutoExtraction
from Classes.Children import Children
from Qt.WidgetData import WidgetData
from Qt.Dialogue import LayerDialog


class LossFunction:

    def __init__(self) -> None:
        self.Children = Children()
        self.LayerDialog = LayerDialog()
        self.LOSSFUNC = AutoExtraction().LOSSFUNC
        self.WidgetUtility = WidgetData()
        self.loss_function = dict()
        self.fill_lossfunctions()

    def load_from_config(self, json_data: dict):
        if len(json_data["loss_func"]) != 0:
            self.loss_function = json_data['loss_func']
            self.Children.qt_selectedLossFunc_QLineEdit.setText(
                json_data['loss_func']["type"])

    def fill_lossfunctions(self):
        for lossfunc in self.LOSSFUNC:
            selectLossFunc_QPushButton = QPushButton(lossfunc)
            selectLossFunc_QPushButton.clicked.connect(
                lambda i=lossfunc,
                j=self.LOSSFUNC,
                k=self.on_select_lossfunc_clicked:
                self.LayerDialog.on_torch_func_clicked(
                    i, j, k,
                    None, None
                )
            )
            self.Children.qt_lossFuncsList_QVBoxLayout.addWidget(
                selectLossFunc_QPushButton)

    def on_select_lossfunc_clicked(
        self,
        lossfunc_type,
        params_names,
        params_value_widgets,
        paramsWindow_QDialog,
        *args,
    ):
        self.selected_lossfunc = {"type": lossfunc_type, "params": dict()}
        for i in range(len(params_value_widgets)):
            param_value = self.WidgetUtility.get_widget_data(
                params_value_widgets[i])

            if param_value != "":
                self.selected_lossfunc["params"][params_names[i]] = param_value

        self.Children.qt_selectedLossFunc_QLineEdit.setText(lossfunc_type)
        self.loss_function = self.selected_lossfunc
        paramsWindow_QDialog.close()
