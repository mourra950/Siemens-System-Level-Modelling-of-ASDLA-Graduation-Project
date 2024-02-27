import os
import sys
from PySide6 import QtWidgets,QtCore

from PySide6.QtWidgets import QTreeWidget,QTreeWidgetItem
from PySide6.QtUiTools import QUiLoader

basedir = os.path.dirname(__file__)
loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)

example = loader.findChild(QTreeWidget, "treeWidget")

window = loader.load(os.path.join(basedir, "mainwindow.ui"), None)
window.setWindowTitle("System Level Modelling")
example.
ex=QTreeWidget()
item1= QTreeWidgetItem(ex,)

ex.addTopLevelItems()


with open(os.path.join(basedir, "skin.qss"), "r") as f:
    _style = f.read()
    app.setStyleSheet(_style)

window.show()
app.exec()


class testView(QtCore.QAbstractItemModel):
    
