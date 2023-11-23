/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.5.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QListWidget>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableView>
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QHBoxLayout *horizontalLayout;
    QTabWidget *tabWidget;
    QWidget *Dashboard;
    QLabel *label;
    QLabel *label_2;
    QWidget *Params;
    QLineEdit *InputHeight;
    QLabel *label_4;
    QLineEdit *inputsize;
    QLabel *label_5;
    QTableView *tableView_2;
    QPushButton *submit;
    QWidget *layoutWidget;
    QGridLayout *gridLayout;
    QGroupBox *inputtype;
    QVBoxLayout *verticalLayout;
    QRadioButton *RGB;
    QRadioButton *GrayScale;
    QGroupBox *groupBox;
    QRadioButton *Standard;
    QRadioButton *Winograd;
    QLabel *label_13;
    QLabel *label_14;
    QLabel *label_15;
    QLabel *label_16;
    QLabel *label_17;
    QLabel *label_18;
    QLineEdit *datacsv;
    QLineEdit *numEpochs;
    QLineEdit *learningRate;
    QLineEdit *batchSize;
    QComboBox *comboBox_optimizer;
    QComboBox *comboBox_lossFunc;
    QFrame *line_2;
    QWidget *Architecture;
    QVBoxLayout *verticalLayout_7;
    QVBoxLayout *verticalLayout_6;
    QVBoxLayout *verticalLayout_3;
    QGroupBox *groupBox_3;
    QComboBox *layer;
    QGroupBox *groupBox_2;
    QWidget *layoutWidget1;
    QHBoxLayout *horizontalLayout_2;
    QVBoxLayout *verticalLayout_4;
    QLabel *label_10;
    QLabel *label_6;
    QLabel *label_8;
    QLabel *label_9;
    QVBoxLayout *verticalLayout_5;
    QLineEdit *units;
    QLineEdit *kernelsize;
    QLineEdit *filters;
    QLineEdit *stride;
    QGroupBox *padding;
    QWidget *layoutWidget2;
    QHBoxLayout *horizontalLayout_3;
    QRadioButton *yes;
    QRadioButton *no;
    QWidget *layoutWidget3;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *layerbutton;
    QPushButton *Arch;
    QTableView *tableView;
    QWidget *OutputFiles;
    QLabel *Lcode;
    QTextBrowser *codeSample;
    QPushButton *generate;
    QPushButton *train;
    QLabel *Lgenerated;
    QPushButton *systemC;
    QListWidget *generatedFiles;
    QWidget *GeneratedFiles;
    QStatusBar *statusbar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(888, 625);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        horizontalLayout = new QHBoxLayout(centralwidget);
        horizontalLayout->setObjectName("horizontalLayout");
        tabWidget = new QTabWidget(centralwidget);
        tabWidget->setObjectName("tabWidget");
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(tabWidget->sizePolicy().hasHeightForWidth());
        tabWidget->setSizePolicy(sizePolicy);
        QFont font;
        font.setFamilies({QString::fromUtf8("Siemens Sans")});
        font.setBold(true);
        tabWidget->setFont(font);
        tabWidget->setAutoFillBackground(false);
        tabWidget->setStyleSheet(QString::fromUtf8("background-color: rgb(222, 222, 222);"));
        Dashboard = new QWidget();
        Dashboard->setObjectName("Dashboard");
        label = new QLabel(Dashboard);
        label->setObjectName("label");
        label->setGeometry(QRect(220, 260, 441, 41));
        QFont font1;
        font1.setFamilies({QString::fromUtf8("Siemens Sans")});
        font1.setPointSize(14);
        font1.setBold(true);
        label->setFont(font1);
        label->setStyleSheet(QString::fromUtf8(""));
        label_2 = new QLabel(Dashboard);
        label_2->setObjectName("label_2");
        label_2->setGeometry(QRect(110, 120, 681, 131));
        label_2->setPixmap(QPixmap(QString::fromUtf8("../../../../Desktop/Siemens-invert-logo-700x167.png")));
        tabWidget->addTab(Dashboard, QString());
        Params = new QWidget();
        Params->setObjectName("Params");
        InputHeight = new QLineEdit(Params);
        InputHeight->setObjectName("InputHeight");
        InputHeight->setGeometry(QRect(190, 60, 154, 26));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(InputHeight->sizePolicy().hasHeightForWidth());
        InputHeight->setSizePolicy(sizePolicy1);
        QFont font2;
        font2.setFamilies({QString::fromUtf8("Siemens Sans")});
        InputHeight->setFont(font2);
        InputHeight->setStyleSheet(QString::fromUtf8("background-color: white;"));
        label_4 = new QLabel(Params);
        label_4->setObjectName("label_4");
        label_4->setGeometry(QRect(10, 20, 78, 20));
        label_4->setFont(font2);
        inputsize = new QLineEdit(Params);
        inputsize->setObjectName("inputsize");
        inputsize->setGeometry(QRect(190, 20, 154, 26));
        sizePolicy1.setHeightForWidth(inputsize->sizePolicy().hasHeightForWidth());
        inputsize->setSizePolicy(sizePolicy1);
        inputsize->setFont(font2);
        inputsize->setStyleSheet(QString::fromUtf8("background-color: white;"));
        label_5 = new QLabel(Params);
        label_5->setObjectName("label_5");
        label_5->setGeometry(QRect(10, 60, 83, 20));
        sizePolicy1.setHeightForWidth(label_5->sizePolicy().hasHeightForWidth());
        label_5->setSizePolicy(sizePolicy1);
        label_5->setFont(font2);
        tableView_2 = new QTableView(Params);
        tableView_2->setObjectName("tableView_2");
        tableView_2->setGeometry(QRect(500, 10, 251, 401));
        tableView_2->setFont(font2);
        tableView_2->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
""));
        tableView_2->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);
        submit = new QPushButton(Params);
        submit->setObjectName("submit");
        submit->setGeometry(QRect(200, 500, 133, 29));
        submit->setFont(font2);
        submit->setStyleSheet(QString::fromUtf8(""));
        layoutWidget = new QWidget(Params);
        layoutWidget->setObjectName("layoutWidget");
        layoutWidget->setGeometry(QRect(420, 420, 421, 112));
        layoutWidget->setFont(font2);
        gridLayout = new QGridLayout(layoutWidget);
        gridLayout->setObjectName("gridLayout");
        gridLayout->setContentsMargins(0, 0, 0, 0);
        inputtype = new QGroupBox(layoutWidget);
        inputtype->setObjectName("inputtype");
        sizePolicy1.setHeightForWidth(inputtype->sizePolicy().hasHeightForWidth());
        inputtype->setSizePolicy(sizePolicy1);
        inputtype->setFont(font2);
        inputtype->setStyleSheet(QString::fromUtf8("background-color: rgb(222, 222, 222);"));
        verticalLayout = new QVBoxLayout(inputtype);
        verticalLayout->setObjectName("verticalLayout");
        RGB = new QRadioButton(inputtype);
        RGB->setObjectName("RGB");
        RGB->setFont(font2);

        verticalLayout->addWidget(RGB);

        GrayScale = new QRadioButton(inputtype);
        GrayScale->setObjectName("GrayScale");
        GrayScale->setFont(font2);

        verticalLayout->addWidget(GrayScale);


        gridLayout->addWidget(inputtype, 0, 0, 1, 1);

        groupBox = new QGroupBox(layoutWidget);
        groupBox->setObjectName("groupBox");
        QSizePolicy sizePolicy2(QSizePolicy::Fixed, QSizePolicy::Minimum);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(groupBox->sizePolicy().hasHeightForWidth());
        groupBox->setSizePolicy(sizePolicy2);
        groupBox->setFont(font2);
        groupBox->setStyleSheet(QString::fromUtf8("background-color: rgb(222, 222, 222);"));
        Standard = new QRadioButton(groupBox);
        Standard->setObjectName("Standard");
        Standard->setGeometry(QRect(10, 50, 91, 24));
        Standard->setFont(font2);
        Winograd = new QRadioButton(groupBox);
        Winograd->setObjectName("Winograd");
        Winograd->setGeometry(QRect(10, 20, 93, 24));
        Winograd->setFont(font2);

        gridLayout->addWidget(groupBox, 0, 1, 1, 1);

        label_13 = new QLabel(Params);
        label_13->setObjectName("label_13");
        label_13->setGeometry(QRect(10, 100, 91, 20));
        label_13->setFont(font2);
        label_14 = new QLabel(Params);
        label_14->setObjectName("label_14");
        label_14->setGeometry(QRect(10, 220, 111, 20));
        label_14->setFont(font2);
        label_15 = new QLabel(Params);
        label_15->setObjectName("label_15");
        label_15->setGeometry(QRect(10, 180, 91, 20));
        label_15->setFont(font2);
        label_16 = new QLabel(Params);
        label_16->setObjectName("label_16");
        label_16->setGeometry(QRect(10, 140, 71, 20));
        label_16->setFont(font2);
        label_17 = new QLabel(Params);
        label_17->setObjectName("label_17");
        label_17->setGeometry(QRect(10, 300, 91, 20));
        label_17->setFont(font2);
        label_18 = new QLabel(Params);
        label_18->setObjectName("label_18");
        label_18->setGeometry(QRect(10, 260, 71, 20));
        label_18->setFont(font2);
        datacsv = new QLineEdit(Params);
        datacsv->setObjectName("datacsv");
        datacsv->setGeometry(QRect(190, 100, 154, 26));
        sizePolicy1.setHeightForWidth(datacsv->sizePolicy().hasHeightForWidth());
        datacsv->setSizePolicy(sizePolicy1);
        datacsv->setFont(font2);
        datacsv->setStyleSheet(QString::fromUtf8("background-color: white;"));
        numEpochs = new QLineEdit(Params);
        numEpochs->setObjectName("numEpochs");
        numEpochs->setGeometry(QRect(190, 220, 154, 26));
        sizePolicy1.setHeightForWidth(numEpochs->sizePolicy().hasHeightForWidth());
        numEpochs->setSizePolicy(sizePolicy1);
        numEpochs->setFont(font2);
        numEpochs->setStyleSheet(QString::fromUtf8("background-color: white;"));
        learningRate = new QLineEdit(Params);
        learningRate->setObjectName("learningRate");
        learningRate->setGeometry(QRect(190, 180, 154, 26));
        sizePolicy1.setHeightForWidth(learningRate->sizePolicy().hasHeightForWidth());
        learningRate->setSizePolicy(sizePolicy1);
        learningRate->setFont(font2);
        learningRate->setStyleSheet(QString::fromUtf8("background-color: white;"));
        batchSize = new QLineEdit(Params);
        batchSize->setObjectName("batchSize");
        batchSize->setGeometry(QRect(190, 140, 154, 26));
        sizePolicy1.setHeightForWidth(batchSize->sizePolicy().hasHeightForWidth());
        batchSize->setSizePolicy(sizePolicy1);
        batchSize->setFont(font2);
        batchSize->setStyleSheet(QString::fromUtf8("background-color: white;"));
        comboBox_optimizer = new QComboBox(Params);
        comboBox_optimizer->setObjectName("comboBox_optimizer");
        comboBox_optimizer->setGeometry(QRect(190, 260, 151, 21));
        comboBox_optimizer->setFont(font2);
        comboBox_lossFunc = new QComboBox(Params);
        comboBox_lossFunc->setObjectName("comboBox_lossFunc");
        comboBox_lossFunc->setGeometry(QRect(190, 300, 151, 21));
        comboBox_lossFunc->setFont(font2);
        line_2 = new QFrame(Params);
        line_2->setObjectName("line_2");
        line_2->setGeometry(QRect(10, 340, 162, 16));
        line_2->setFont(font2);
        line_2->setFrameShape(QFrame::HLine);
        line_2->setFrameShadow(QFrame::Sunken);
        tabWidget->addTab(Params, QString());
        Architecture = new QWidget();
        Architecture->setObjectName("Architecture");
        verticalLayout_7 = new QVBoxLayout(Architecture);
        verticalLayout_7->setObjectName("verticalLayout_7");
        verticalLayout_6 = new QVBoxLayout();
        verticalLayout_6->setObjectName("verticalLayout_6");
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        groupBox_3 = new QGroupBox(Architecture);
        groupBox_3->setObjectName("groupBox_3");
        groupBox_3->setFont(font);
        layer = new QComboBox(groupBox_3);
        layer->setObjectName("layer");
        layer->setGeometry(QRect(10, 40, 171, 26));
        layer->setFont(font2);
        layer->setStyleSheet(QString::fromUtf8("background-color: white;"));
        groupBox_2 = new QGroupBox(groupBox_3);
        groupBox_2->setObjectName("groupBox_2");
        groupBox_2->setGeometry(QRect(0, 190, 750, 331));
        groupBox_2->setFont(font);
        layoutWidget1 = new QWidget(groupBox_2);
        layoutWidget1->setObjectName("layoutWidget1");
        layoutWidget1->setGeometry(QRect(10, 20, 191, 137));
        layoutWidget1->setFont(font2);
        horizontalLayout_2 = new QHBoxLayout(layoutWidget1);
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        verticalLayout_4 = new QVBoxLayout();
        verticalLayout_4->setObjectName("verticalLayout_4");
        label_10 = new QLabel(layoutWidget1);
        label_10->setObjectName("label_10");
        label_10->setFont(font2);

        verticalLayout_4->addWidget(label_10);

        label_6 = new QLabel(layoutWidget1);
        label_6->setObjectName("label_6");
        label_6->setFont(font2);

        verticalLayout_4->addWidget(label_6);

        label_8 = new QLabel(layoutWidget1);
        label_8->setObjectName("label_8");
        label_8->setFont(font2);

        verticalLayout_4->addWidget(label_8);

        label_9 = new QLabel(layoutWidget1);
        label_9->setObjectName("label_9");
        label_9->setFont(font2);

        verticalLayout_4->addWidget(label_9);


        horizontalLayout_2->addLayout(verticalLayout_4);

        verticalLayout_5 = new QVBoxLayout();
        verticalLayout_5->setObjectName("verticalLayout_5");
        units = new QLineEdit(layoutWidget1);
        units->setObjectName("units");
        units->setFont(font2);
        units->setStyleSheet(QString::fromUtf8("background-color: white;"));

        verticalLayout_5->addWidget(units);

        kernelsize = new QLineEdit(layoutWidget1);
        kernelsize->setObjectName("kernelsize");
        kernelsize->setFont(font2);
        kernelsize->setStyleSheet(QString::fromUtf8("background-color: white;"));

        verticalLayout_5->addWidget(kernelsize);

        filters = new QLineEdit(layoutWidget1);
        filters->setObjectName("filters");
        filters->setFont(font2);
        filters->setStyleSheet(QString::fromUtf8("background-color: white;"));

        verticalLayout_5->addWidget(filters);

        stride = new QLineEdit(layoutWidget1);
        stride->setObjectName("stride");
        stride->setFont(font2);
        stride->setStyleSheet(QString::fromUtf8("background-color: white;"));

        verticalLayout_5->addWidget(stride);


        horizontalLayout_2->addLayout(verticalLayout_5);

        padding = new QGroupBox(groupBox_2);
        padding->setObjectName("padding");
        padding->setGeometry(QRect(30, 180, 151, 91));
        padding->setFont(font2);
        padding->setStyleSheet(QString::fromUtf8("background-color: rgb(222, 222, 222);"));
        layoutWidget2 = new QWidget(padding);
        layoutWidget2->setObjectName("layoutWidget2");
        layoutWidget2->setGeometry(QRect(20, 30, 108, 28));
        layoutWidget2->setFont(font2);
        horizontalLayout_3 = new QHBoxLayout(layoutWidget2);
        horizontalLayout_3->setObjectName("horizontalLayout_3");
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        yes = new QRadioButton(layoutWidget2);
        yes->setObjectName("yes");
        yes->setFont(font2);

        horizontalLayout_3->addWidget(yes);

        no = new QRadioButton(layoutWidget2);
        no->setObjectName("no");
        no->setFont(font2);

        horizontalLayout_3->addWidget(no);

        layoutWidget3 = new QWidget(groupBox_2);
        layoutWidget3->setObjectName("layoutWidget3");
        layoutWidget3->setGeometry(QRect(240, 260, 244, 31));
        layoutWidget3->setFont(font2);
        horizontalLayout_4 = new QHBoxLayout(layoutWidget3);
        horizontalLayout_4->setObjectName("horizontalLayout_4");
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        layerbutton = new QPushButton(layoutWidget3);
        layerbutton->setObjectName("layerbutton");
        layerbutton->setFont(font2);

        horizontalLayout_4->addWidget(layerbutton);

        Arch = new QPushButton(layoutWidget3);
        Arch->setObjectName("Arch");
        Arch->setFont(font2);

        horizontalLayout_4->addWidget(Arch);

        tableView = new QTableView(groupBox_3);
        tableView->setObjectName("tableView");
        tableView->setGeometry(QRect(275, 31, 461, 351));
        tableView->setFont(font2);
        tableView->setStyleSheet(QString::fromUtf8("background-color: white;"));
        tableView->setSizeAdjustPolicy(QAbstractScrollArea::AdjustToContents);

        verticalLayout_3->addWidget(groupBox_3);


        verticalLayout_6->addLayout(verticalLayout_3);


        verticalLayout_7->addLayout(verticalLayout_6);

        tabWidget->addTab(Architecture, QString());
        OutputFiles = new QWidget();
        OutputFiles->setObjectName("OutputFiles");
        Lcode = new QLabel(OutputFiles);
        Lcode->setObjectName("Lcode");
        Lcode->setGeometry(QRect(390, 20, 301, 20));
        Lcode->setFont(font);
        Lcode->setAlignment(Qt::AlignCenter);
        codeSample = new QTextBrowser(OutputFiles);
        codeSample->setObjectName("codeSample");
        codeSample->setGeometry(QRect(390, 60, 301, 301));
        codeSample->setStyleSheet(QString::fromUtf8("background-color: white;"));
        generate = new QPushButton(OutputFiles);
        generate->setObjectName("generate");
        generate->setGeometry(QRect(70, 380, 161, 23));
        generate->setFont(font2);
        train = new QPushButton(OutputFiles);
        train->setObjectName("train");
        train->setGeometry(QRect(310, 380, 161, 21));
        train->setFont(font2);
        Lgenerated = new QLabel(OutputFiles);
        Lgenerated->setObjectName("Lgenerated");
        Lgenerated->setGeometry(QRect(50, 20, 261, 20));
        Lgenerated->setFont(font);
        Lgenerated->setAlignment(Qt::AlignCenter);
        systemC = new QPushButton(OutputFiles);
        systemC->setObjectName("systemC");
        systemC->setGeometry(QRect(540, 380, 161, 21));
        systemC->setFont(font2);
        generatedFiles = new QListWidget(OutputFiles);
        generatedFiles->setObjectName("generatedFiles");
        generatedFiles->setGeometry(QRect(40, 60, 271, 301));
        generatedFiles->setAutoFillBackground(true);
        generatedFiles->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);"));
        tabWidget->addTab(OutputFiles, QString());
        GeneratedFiles = new QWidget();
        GeneratedFiles->setObjectName("GeneratedFiles");
        tabWidget->addTab(GeneratedFiles, QString());

        horizontalLayout->addWidget(tabWidget);

        MainWindow->setCentralWidget(centralwidget);
        statusbar = new QStatusBar(MainWindow);
        statusbar->setObjectName("statusbar");
        MainWindow->setStatusBar(statusbar);

        retranslateUi(MainWindow);

        tabWidget->setCurrentIndex(1);


        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        label->setText(QCoreApplication::translate("MainWindow", "Application Specific Deep Learning Accelerator", nullptr));
        label_2->setText(QString());
        tabWidget->setTabText(tabWidget->indexOf(Dashboard), QCoreApplication::translate("MainWindow", "Welcome Screen", nullptr));
        label_4->setText(QCoreApplication::translate("MainWindow", "Input Width", nullptr));
        label_5->setText(QCoreApplication::translate("MainWindow", "Input Height", nullptr));
        submit->setText(QCoreApplication::translate("MainWindow", "Submit Parameters", nullptr));
        inputtype->setTitle(QCoreApplication::translate("MainWindow", "Input Type", nullptr));
        RGB->setText(QCoreApplication::translate("MainWindow", "RGB", nullptr));
        GrayScale->setText(QCoreApplication::translate("MainWindow", "Gray Scale", nullptr));
        groupBox->setTitle(QCoreApplication::translate("MainWindow", "Convolution Type", nullptr));
        Standard->setText(QCoreApplication::translate("MainWindow", "Standard ", nullptr));
        Winograd->setText(QCoreApplication::translate("MainWindow", "Winograd", nullptr));
        label_13->setText(QCoreApplication::translate("MainWindow", "Data CSV Path", nullptr));
        label_14->setText(QCoreApplication::translate("MainWindow", "Number of Epochs", nullptr));
        label_15->setText(QCoreApplication::translate("MainWindow", "Learning Rate", nullptr));
        label_16->setText(QCoreApplication::translate("MainWindow", "Batch Size", nullptr));
        label_17->setText(QCoreApplication::translate("MainWindow", "Loss Function", nullptr));
        label_18->setText(QCoreApplication::translate("MainWindow", "Optimizer", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Params), QCoreApplication::translate("MainWindow", "Miscellaneous Parameters", nullptr));
        groupBox_3->setTitle(QCoreApplication::translate("MainWindow", "Layer", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("MainWindow", "Parameters", nullptr));
        label_10->setText(QCoreApplication::translate("MainWindow", "No of Units", nullptr));
        label_6->setText(QCoreApplication::translate("MainWindow", "Kernel Size", nullptr));
        label_8->setText(QCoreApplication::translate("MainWindow", "No of Filters", nullptr));
        label_9->setText(QCoreApplication::translate("MainWindow", "Stride", nullptr));
        padding->setTitle(QCoreApplication::translate("MainWindow", "Padding", nullptr));
        yes->setText(QCoreApplication::translate("MainWindow", "Yes", nullptr));
        no->setText(QCoreApplication::translate("MainWindow", "No", nullptr));
        layerbutton->setText(QCoreApplication::translate("MainWindow", "Submit Layer", nullptr));
        Arch->setText(QCoreApplication::translate("MainWindow", "Submit Architecture", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(Architecture), QCoreApplication::translate("MainWindow", "Architecture", nullptr));
        Lcode->setText(QCoreApplication::translate("MainWindow", "Code Sample", nullptr));
        generate->setText(QCoreApplication::translate("MainWindow", "Generate Pytorch Model", nullptr));
        train->setText(QCoreApplication::translate("MainWindow", "Train Pytorch Model", nullptr));
        Lgenerated->setText(QCoreApplication::translate("MainWindow", "Generated Files", nullptr));
        systemC->setText(QCoreApplication::translate("MainWindow", "SystemC wrapper", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(OutputFiles), QCoreApplication::translate("MainWindow", "Output Files", nullptr));
        tabWidget->setTabText(tabWidget->indexOf(GeneratedFiles), QCoreApplication::translate("MainWindow", "Generated Files", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
