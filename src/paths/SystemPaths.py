import os


class SystemPaths:
    def __init__(self) -> None:
        print("Sys ENV Class")
        self.basedir = os.path.dirname(__file__)
        self.publicdir = os.path.normpath(
            os.path.join(self.basedir, '../../public/'))
        self.srcdir = os.path.normpath(os.path.join(self.basedir, './../'))

        self.delete_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/delete.png"))
        self.up_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/up.png"))
        self.down_icon_path = os.path.normpath(
            os.path.join(self.publicdir, "./icons/down.png"))

        self.main_ui_path = os.path.normpath(
            os.path.join(self.publicdir, "./GUI/mainwindow.ui"))

        # to work on later
        self.css_path = 'ui/skin.qss'
        self.arch_json_path = 'json_files/arch.json'
        self.model_py_path = 'python_files/model.py'
        self.train_py_path = 'python_files/train.py'
        self.model_jinja_path = 'jinja_templates/model.py.jinja'
        self.train_jinja_path = 'jinja_templates/train.py.jinja'
