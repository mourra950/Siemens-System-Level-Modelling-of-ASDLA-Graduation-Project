from utils.Singleton import Singleton
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


class WidgetData(metaclass=Singleton):
    def get_widget_data(self, widget):
        if isinstance(widget, QCheckBox):
            param_value = widget.isChecked()
        elif isinstance(widget, QSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QDoubleSpinBox):
            param_value = widget.value()
        elif isinstance(widget, QComboBox):
            param_value = widget.currentData()
        else:
            param_value = widget.text().strip()
            try:
                param_value = eval(param_value)
            except:
                pass
        return param_value
