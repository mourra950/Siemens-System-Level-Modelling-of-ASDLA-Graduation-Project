from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLabel,
    QDialog
)


class Controller:
    def __init__(self) -> None:
        self.res_block_built = False

    def on_generate_files_clicked(self):
        generator = self.file_read_json()
        self.generate_model()
        self.generate_train()

    def on_res_block_clicked(self, func_name, torch_funcs, on_submit_func, qt_layout):
        if (self.res_block_built):
            self.on_torch_func_clicked(
                func_name, torch_funcs, on_submit_func, qt_layout)
        else:
            self.res_block_built = True
            self.ResCreation.show()

    def on_torch_func_clicked(self, func_name, torch_funcs, on_submit_func, *args):

        # initialize QDialog and lists
        paramsWindow_QDialog = QDialog()
        paramsWindow_QDialog.setMinimumWidth(330)
        allParamsColumn_QVBoxLayout = QVBoxLayout()
        params_value_widgets = []
        params_names = []

        self.create_dialogue_controller(
            torch_funcs, func_name, params_names, params_value_widgets, allParamsColumn_QVBoxLayout)

        ################################

        allParamsColumn_QVBoxLayout.addWidget(QLabel())
        submitLayer_QPushButton = QPushButton('Submit Layer')

        ##############################
        submitLayer_QPushButton.clicked.connect(
            lambda  submit_func=on_submit_func, i=func_name, j=params_names, k=params_value_widgets, l=paramsWindow_QDialog, q_layout=args[0], arch=args[1]: \
                submit_func(
                    i, j, k, l, q_layout, arch
                )
        )

        allParamsColumn_QVBoxLayout.addWidget(submitLayer_QPushButton)
        paramsWindow_QDialog.setLayout(allParamsColumn_QVBoxLayout)
        paramsWindow_QDialog.setWindowTitle(f"{func_name}")
        paramsWindow_QDialog.exec()

    def on_select_lossfunc_clicked(self, lossfunc_type, params_names, params_value_widgets, paramsWindow_QDialog, *args):
        self.selected_lossfunc = {
            'type': lossfunc_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])

            if param_value != '':
                self.selected_lossfunc['params'][params_names[i]] = param_value
        self.architecture['misc_params']['loss_func'] = self.selected_lossfunc

        self.qt_selectedLossFunc_QLineEdit.setText(lossfunc_type)
        paramsWindow_QDialog.close()

    def on_select_optimizer_clicked(self, optimizer_type, params_names, params_value_widgets, paramsWindow_QDialog, *args):
        self.selected_optimizer = {
            'type': optimizer_type,
            'params': dict()
        }
        for i in range(len(params_value_widgets)):
            param_value = self.get_widget_data(params_value_widgets[i])

            if param_value != '':
                self.selected_optimizer['params'][params_names[i]
                                                  ] = param_value

            self.qt_selectedOptimizer_QLineEdit.setText(optimizer_type)
        self.architecture['misc_params']['optimizer'] = self.selected_optimizer
            
        paramsWindow_QDialog.close()
