from PySide6.QtWidgets import (
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
    QSpinBox,
    QTreeWidget,
    QTextBrowser,
    QTextEdit
)


class Children:
    def __init__(self) -> None:
        self.ResCreation = self.loader.load(
            self.SysPath.res_build_ui_path, None)
        self.ui = self.loader.load(self.SysPath.GUI_path, None)
        self.find_children()

    def find_children(self) -> None:
        """Locate all qt elements"""
        self.qt_layers_scroll_box = self.ui.findChild(QVBoxLayout, "Scrollbox")
        self.qt_layersList_QVBoxLayout = self.ui.findChild(
            QVBoxLayout, "layersList_QVBoxLayout"
        )
        self.qt_inputWidth_QSpinBox = self.ui.findChild(
            QSpinBox, "inputWidth_QSpinBox")
        self.qt_inputHeight_QSpinBox = self.ui.findChild(
            QSpinBox, "inputHeight_QSpinBox"
        )
        self.qt_batchSize_QSpinBox = self.ui.findChild(
            QSpinBox, "batchSize_QSpinBox")
        self.qt_numEpochs_QSpinBox = self.ui.findChild(
            QSpinBox, "numberEpochs_QSpinBox"
        )
        self.qt_selectedOptimizer_QLineEdit = self.ui.findChild(
            QLineEdit, "selectedOptimizer_QLineEdit"
        )
        self.qt_selectedLossFunc_QLineEdit = self.ui.findChild(
            QLineEdit, "selectedLossFunc_QLineEdit"
        )
        self.qt_selectedScheduler_QLineEdit = self.ui.findChild(
            QLineEdit, "selectedScheduler_QLineEdit"
        )
        self.qt_selectedDevice_QComboBox = self.ui.findChild(
            QComboBox, "deviceComboBox"
        )
        self.qt_selectedDataset_QComboBox = self.ui.findChild(
            QComboBox, "datasetComboBox"
        )

        # replacment

        self.qt_inputType_QSpinBox = self.ui.findChild(
            QSpinBox, "inputChannelsSpinBox")
        self.qt_addedLayers_QVBoxLayout = self.ui.findChild(
            QVBoxLayout, "addedLayers_QVBoxLayout"
        )
        self.qt_optimizersList_QVBoxLayout = self.ui.findChild(
            QVBoxLayout, "optimizersList_QVBoxLayout"
        )
        self.qt_lossFuncsList_QVBoxLayout = self.ui.findChild(
            QVBoxLayout, "lossFuncsList_QVBoxLayout"
        )
        self.qt_schedulersList_QVBoxLayout = self.ui.findChild(
            QVBoxLayout, "schedulersList_QVBoxLayout"
        )

        self.qt_submitParams_QPushButton = self.ui.findChild(
            QPushButton, "submitParams_QPushButton"
        )
        self.qt_submitArch_QPushButton = self.ui.findChild(
            QPushButton, "submitArch_QPushButton"
        )
        self.qt_generateFiles_QPushButton = self.ui.findChild(
            QPushButton, "generateFiles_QPushButton"
        )
        self.qt_trainModel_QPushButton = self.ui.findChild(
            QPushButton, "trainPyModel_btn"
        )
        # self.omar_generate_btn = self.ui.findChild(
        #     QPushButton, 'omar_generate_btn'
        # )

        ####################################################
        self.res_layersList_QVBoxLayout = self.ResCreation.findChild(
            QVBoxLayout, "res_layersList_QVBoxLayout"
        )
        self.res_addedLayers_QVBoxLayout = self.ResCreation.findChild(
            QVBoxLayout, "res_addedLayers_QVBoxLayout"
        )
        self.submitRes_QPushButton = self.ResCreation.findChild(
            QPushButton, "submitRes_QPushButton"
        )
        ##########################################################
        # self.Create_transfer_learning_model_QPushButton = self.ui.findChild(
        #     QPushButton, "Create_transfer_Model_QPushButton"
        # )

        # self.Create_transfer_learning_model_QPushButton = self.ui.findChild(
        #     QPushButton, 'Train_transfer_Model_QPushButton')
        # self.Create_transfer_learning_model_QPushButton = self.ui.findChild(
        #     QPushButton, 'Run_transfer_Model_QPushButton')
        # self.Pretrained_model_ComboBox = self.ui.findChild(
        #     QComboBox, 'Pretrained_model_ComboBox')
        self.pretrained_model_combobox = self.ui.findChild(
            QComboBox, "Pretrained_model_ComboBox"
        )
        self.Create_transfer_learning_model_QPushButton = self.ui.findChild(
            QPushButton, "Train_transfer_Model_QPushButton"
        )
        self.Create_transfer_Model_QPushButton = self.ui.findChild(
            QPushButton, "Create_transfer_Model_QPushButton"
        )
        self.Run_transfer_Model_QPushButton = self.ui.findChild(
            QPushButton, "Run_transfer_Model_QPushButton"
        )
        # testing generating manual
        self.qt_manual_generate = self.ui.findChild(
            QPushButton, "Generate_manual_QPushButton"
        )

        self.qt_output_tree_viewer = self.ui.findChild(
            QTreeWidget, "files_tree")

        self.qt_output_file_viewer = self.ui.findChild(
            QTextBrowser, "codeSample")

        # Violation Layer List
        self.qt_violations_text_edit = self.ui.findChild(
            QTextEdit, "Violation_QTextEdit")
