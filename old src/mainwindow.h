#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QStandardItemModel>
#include <QListWidget>
#include <QListWidgetItem>
#include <QTextBrowser>

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();
    //QStandardItemModel *model;
   // QStringList horizontalHeader;
    //QStringList verticalHeader;
private slots:
   // void on_pushButton_clicked();

    void on_submit_clicked();

    void on_layerbutton_clicked();

    void on_Arch_clicked();

    //void displayCppCode(const QString& filePath,QTextBrowser* textBrowser);
    void on_generate_clicked();
    //void onProcessSystemcReady();
    //void onProcessPythonReady();
    void on_train_clicked();
    void onProcessModelReady();
    void onProcessTrainReady();

   // void on_layer_activated(int index);

    //void on_layer_currentTextChanged(const QString &arg1);

    void on_layer_currentIndexChanged(int index);

    void on_systemC_clicked();

    //void on_listWidget_currentItemChanged(QListWidgetItem *current, QListWidgetItem *previous);

    //void on_listWidget_currentRowChanged(int currentRow);

   // void on_listWidget_currentTextChanged(const QString &currentText);

    //void on_listWidget_currentRowChanged(int currentRow);

    void on_generatedFiles_itemSelectionChanged();

private:
    Ui::MainWindow *ui;
    QStandardItemModel *model;
    QStandardItemModel *model_2;

    QStringList horizontalHeader;
    QStringList verticalHeader;
    QStringList horizontalHeader_2;
    QStringList verticalHeader_2;
};
#endif // MAINWINDOW_H
