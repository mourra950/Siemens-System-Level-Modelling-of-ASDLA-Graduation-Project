from mainwindow import *
import sys
from paths import *

app = QApplication(sys.argv)
win = MainWindow()

win.setWindowTitle("System Level Modelling")
# with open(css_path, "r") as f:
#     _style = f.read()
#     app.setStyleSheet(_style)

win.show()
app.exec_()