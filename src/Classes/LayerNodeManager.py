from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QHBoxLayout, QLabel, QCheckBox, QDialog,
    QFrame
)
from PySide6.QtUiTools import QUiLoader
from PySide6 import QtCore
from PySide6.QtGui import QIcon


class LayerNodeManager:
    def __init__(self) -> None:
        self.architecture = {
            'layers': [],
            'misc_params': {
                'width': 1,
                'height': 1,
                'channels': 1,
            }
        }
    def create_layer_node(self, layer, index):
        addedLayerRow_QHBoxLayout = QHBoxLayout()
        border_QFrame = QFrame()
        border_QFrame.setMaximumHeight(70)
        border_QFrame.setLayout(addedLayerRow_QHBoxLayout)
        border_QFrame.setStyleSheet('''
            QFrame{
                border: 1px solid black;
            }
            QLabel{
                border: none;
                font-weight: bold;
                font-size: 15px;
            }
        ''')

        delete_QPushButton = QPushButton()
        delete_QPushButton.setMaximumWidth(30)
        delete_QPushButton.setIcon(QIcon(self.delete_icon_path))
        delete_QPushButton.clicked.connect(
            lambda func=self.on_delete_layer_clicked, i=border_QFrame:
            func(i)
        )
        up_QPushButton = QPushButton()
        up_QPushButton.setMaximumWidth(28)
        up_QPushButton.setIcon(QIcon(self.up_icon_path))
        up_QPushButton.clicked.connect(
            lambda func=self.on_move_buttons_clicked, i=border_QFrame:
            func(i, 'up')
        )
        down_QPushButton = QPushButton()
        down_QPushButton.setMaximumWidth(28)
        down_QPushButton.setIcon(QIcon(self.down_icon_path))
        down_QPushButton.clicked.connect(
            lambda  func=self.on_move_buttons_clicked,  i=border_QFrame:
            func(i, 'down')
        )

        moveableArrows_QVBoxLayout = QVBoxLayout()
        moveableArrows_QVBoxLayout.addWidget(up_QPushButton)
        moveableArrows_QVBoxLayout.addWidget(down_QPushButton)

        addedLayerRow_QHBoxLayout.addWidget(QLabel(layer['type']))
        addedLayerRow_QHBoxLayout.addLayout(moveableArrows_QVBoxLayout)
        addedLayerRow_QHBoxLayout.addWidget(delete_QPushButton)

        if index == -1:
            self.qt_addedLayers_QVBoxLayout.addWidget(border_QFrame)
            self.architecture['layers'].append(layer)
        else:
            self.qt_addedLayers_QVBoxLayout.insertWidget(index, border_QFrame)
            self.architecture['layers'].insert(index, layer)

    def on_delete_layer_clicked(self, border_QFrame):
        for i in range(len(self.architecture['layers'])):
            if border_QFrame == self.qt_addedLayers_QVBoxLayout.itemAt(i).widget():
                layer_widget = self.qt_addedLayers_QVBoxLayout.itemAt(i).widget()

                self.architecture['layers'].pop(i)
                layer_widget.deleteLater()
                self.qt_addedLayers_QVBoxLayout.removeWidget(layer_widget)
                break

    def on_move_buttons_clicked(self, border_QFrame, direction):
        size = len(self.architecture['layers'])
        for i in range(size):
            if border_QFrame == self.qt_addedLayers_QVBoxLayout.itemAt(i).widget():
                if (
                    (i == 0 and direction == 'up')
                    or
                    (i == size and direction == 'down')
                ):
                    break

                layer_widget = self.qt_addedLayers_QVBoxLayout.itemAt(i).widget()
                if direction == 'up':
                    new_idx = i-1
                elif direction == 'down':
                    new_idx = i+1

                layer = self.architecture['layers'].pop(i)
                self.architecture['layers'].insert(new_idx, layer)

                self.qt_addedLayers_QVBoxLayout.removeWidget(layer_widget)
                self.qt_addedLayers_QVBoxLayout.insertWidget(
                    new_idx, layer_widget)
                break
