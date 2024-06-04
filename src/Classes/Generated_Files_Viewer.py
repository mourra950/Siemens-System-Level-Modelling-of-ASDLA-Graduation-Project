from utils.Singleton import Singleton
from PySide6.QtWidgets import QTreeView, QTreeWidgetItem
from PySide6.QtCore import Qt

import os


class GeneratedFilesViewer():
    def __init__(self) -> None:
        self.qt_output_tree_viewer.itemClicked.connect(self.on_file_clicked)

    def show_files(self, project_path):
        root = QTreeWidgetItem([os.path.basename(project_path)])
        root.setData(0, Qt.ItemDataRole.UserRole, project_path)
        self.qt_output_tree_viewer.addTopLevelItem(root)
        self.create_children(root, project_path)

    def create_children(self, root, project_path):
        for item in os.listdir(project_path):
            item_path = os.path.join(project_path, item)
            child_item = QTreeWidgetItem([item])
            child_item.setData(0, Qt.ItemDataRole.UserRole, item_path)
            root.addChild(child_item)
            if os.path.isdir(item_path):
                self.create_children(child_item, item_path)

    def on_file_clicked(self, file, column):
        file_path = file.data(0, Qt.ItemDataRole.UserRole)
        if os.path.isfile(file_path):
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    self.qt_output_file_viewer.setPlainText(content)
            except:
                pass
