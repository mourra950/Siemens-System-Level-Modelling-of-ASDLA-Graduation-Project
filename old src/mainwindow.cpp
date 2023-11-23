#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QProcess>
#include <QStringList>
#include <QFileInfo>
#include <QMessageBox>
#include <QString>
#include <QFile>
#include <QTextStream>
#include <QFileDialog>
#include <QStandardItemModel>
#include <QStandardItem>
#include <QDir>
#include <iostream>
#include <fstream>

#include <json-develop/single_include/nlohmann/json.hpp>
#include "json.hpp"

using json = nlohmann::json;
using namespace std;
MainWindow::MainWindow(QWidget *parent)
	: QMainWindow(parent), ui(new Ui::MainWindow)
{

	ui->setupUi(this);
	ui->layer->addItem("Convolution");
	ui->layer->addItem("Max pool");
	ui->layer->addItem("Average pool");
	ui->layer->addItem("Depthwise convolution");
	ui->layer->addItem("Flatten");
	ui->layer->addItem("Fully Connected");

	ui->comboBox_optimizer->addItem("Adadelta");
	ui->comboBox_optimizer->addItem("Adagrad");
	ui->comboBox_optimizer->addItem("Adam");
	ui->comboBox_lossFunc->addItem("L1Loss");
	ui->comboBox_lossFunc->addItem("MSELoss");
	ui->comboBox_lossFunc->addItem("CrossEntropyLoss");
	ui->comboBox_lossFunc->addItem("NLLLoss");

	model = new QStandardItemModel(10, 6, this);
	model_2 = new QStandardItemModel(10, 2, this);

	horizontalHeader.append("Layer name");
	horizontalHeader.append("Kernel");
	horizontalHeader.append("Filters");
	horizontalHeader.append("Stride");
	horizontalHeader.append("Units");
	horizontalHeader.append("Padding");
	horizontalHeader_2.append("Parameter");
	horizontalHeader_2.append("Value");
	model->setHorizontalHeaderLabels(horizontalHeader);
	model->setVerticalHeaderLabels(verticalHeader);
	model_2->setHorizontalHeaderLabels(horizontalHeader_2);
	model_2->setVerticalHeaderLabels(verticalHeader_2);
	//    QModelIndex index_31 = model_2->index(0,0,QModelIndex());
	//    model_2->setData(index_31, "Data Width");
	//    QModelIndex index_32 = model_2->index(1,0,QModelIndex());
	//    model_2->setData(index_32, "Mantissa");
	//    QModelIndex index_33 = model_2->index(2,0,QModelIndex());
	//    model_2->setData(index_33, "Exponent");
	QModelIndex index_34 = model_2->index(0, 0, QModelIndex());
	model_2->setData(index_34, "Input Width");
	QModelIndex index_35 = model_2->index(1, 0, QModelIndex());
	model_2->setData(index_35, "Input Height");
	//    QModelIndex index_36 = model_2->index(5,0,QModelIndex());
	//    model_2->setData(index_36, "Output Files Path");
	QModelIndex index_37 = model_2->index(2, 0, QModelIndex());
	model_2->setData(index_37, "Input Type");
	// QModelIndex index_38 = model_2->index(7,0,QModelIndex());
	// model_2->setData(index_38, "Arithmetic Type");
	QModelIndex index_39 = model_2->index(3, 0, QModelIndex());
	model_2->setData(index_39, "Convolution Type");

	QModelIndex index_40 = model_2->index(4, 0, QModelIndex());
	model_2->setData(index_40, "Data CSV Path");
	QModelIndex index_41 = model_2->index(5, 0, QModelIndex());
	model_2->setData(index_41, "Batch Size");
	QModelIndex index_42 = model_2->index(6, 0, QModelIndex());
	model_2->setData(index_42, "Learning Rate");
	QModelIndex index_43 = model_2->index(7, 0, QModelIndex());
	model_2->setData(index_43, "Number of Epochs");

	/******** TODO: add the comboBoxes **********/

	QModelIndex index_44 = model_2->index(8, 0, QModelIndex());
	model_2->setData(index_44, "Optimizer");
	QModelIndex index_45 = model_2->index(9, 0, QModelIndex());
	model_2->setData(index_45, "Loss Function");

	ui->tableView->setModel(model);
	ui->tableView_2->setModel(model_2);
	ui->systemC->setEnabled(false);
}

MainWindow::~MainWindow()
{
	delete ui;
}

struct layers
{
	int kernel_size = -1;
	int filters;
	int units;
	int width;
	int height;
	int channels;
	int stride;
	int padding;
	QString name;
};

layers convolution;
layers arr[100];
int layer_number = 0;
int table_row = 0;
int layers = 0;
QString batch_size;
QString learning_rate;
QString num_epochs;
QString csv_path;
QString optimizer;
QString loss_fun;
bool train = 0;

void MainWindow::on_submit_clicked()
{
	batch_size = ui->batchSize->text();
	learning_rate = ui->learningRate->text();
	num_epochs = ui->numEpochs->text();
	csv_path = ui->datacsv->text();
	optimizer = ui->comboBox_optimizer->currentText();
	loss_fun = ui->comboBox_lossFunc->currentText();

	double arithmetic(0);
	double input_type(0);
	double conv(0);
	QString input_type_color;
	QString arithmetic_type;
	QString conv_type;
	/*
		if(!file.open(QFile::WriteOnly | QFile::Truncate))
		{
			QMessageBox:: warning (this, "title", "file is not open");
		}


		QTextStream out (&file); // this is an object (out) to write to the file, and it takes the reference of my file
	*/
	if (ui->RGB->isChecked())
	{
		input_type = 1;
		input_type_color = "RGB";
	}
	else if (ui->GrayScale->isChecked())
	{
		input_type = 0;
		input_type_color = "Gray Scale";
	}

	if (ui->Winograd->isChecked())
	{
		conv = 1;
		conv_type = "Winograd";
	}
	else if (ui->Standard->isChecked())
	{
		conv = 0;
		conv_type = "Standard";
	}
	/*
		out << "Data Width"<< ","<< ui->datawidth->text() <<"\n"<<"Mantissa" <<","<< ui->mantissa->text() << "\n"<<"Exponent" <<","
			<< ui->exponent->text() << "\n"<<"Input Width" <<"," << ui->inputsize->text() << "\n"<<"Input Height" <<","
			<< ui->InputHeight->text() << "\n"<<"Input Type"<<","<<input_type<<"\n"<<"Arithmetic Type"<<","<<arithmetic<<"\n"
			<<"Convolution type"<<","<<conv<<"\n"
			<<"Output files path"<<","<<ui->outputfile->text()<<"\n";


		QModelIndex index_31 = model_2->index(0,0,QModelIndex());
		model_2->setData(index_31, "Data Width");
		QModelIndex index_32 = model_2->index(1,0,QModelIndex());
		model_2->setData(index_32, "Mantissa");
		QModelIndex index_33 = model_2->index(2,0,QModelIndex());
		model_2->setData(index_33, "Exponent");
		QModelIndex index_34 = model_2->index(3,0,QModelIndex());
		model_2->setData(index_34, "Input Width");
		QModelIndex index_35 = model_2->index(4,0,QModelIndex());
		model_2->setData(index_35, "Input Height");
		QModelIndex index_36 = model_2->index(5,0,QModelIndex());
		model_2->setData(index_36, "Output Files Path");
		QModelIndex index_37 = model_2->index(6,0,QModelIndex());
		model_2->setData(index_37, "Input Type");
		QModelIndex index_38 = model_2->index(7,0,QModelIndex());
		model_2->setData(index_38, "Arithmetic Type");
		QModelIndex index_39 = model_2->index(8,0,QModelIndex());
		model_2->setData(index_39, "Convolution Type");
	*/
	// QModelIndex index_21 = model_2->index(0,1,QModelIndex());
	// model_2->setData(index_21, ui->datawidth->text());
	// QModelIndex index_22 = model_2->index(1,1,QModelIndex());
	// model_2->setData(index_22, ui->mantissa->text());
	// QModelIndex index_23 = model_2->index(2,1,QModelIndex());
	// model_2->setData(index_23, ui->exponent->text());
	QModelIndex index_24 = model_2->index(0, 1, QModelIndex());
	model_2->setData(index_24, ui->inputsize->text());
	QModelIndex index_25 = model_2->index(1, 1, QModelIndex());
	model_2->setData(index_25, ui->InputHeight->text());
	// QModelIndex index_26 = model_2->index(2,1,QModelIndex());
	// model_2->setData(index_26, ui->outputfile->text());
	QModelIndex index_27 = model_2->index(2, 1, QModelIndex());
	model_2->setData(index_27, input_type_color);
	// QModelIndex index_28 = model_2->index(4,1,QModelIndex());
	// model_2->setData(index_28, arithmetic_type);
	QModelIndex index_29 = model_2->index(3, 1, QModelIndex());
	model_2->setData(index_29, conv_type);

	QModelIndex index_30 = model_2->index(4, 1, QModelIndex());
	model_2->setData(index_30, ui->datacsv->text());
	QModelIndex index_31 = model_2->index(5, 1, QModelIndex());
	model_2->setData(index_31, ui->batchSize->text());
	QModelIndex index_32 = model_2->index(6, 1, QModelIndex());
	model_2->setData(index_32, ui->learningRate->text());
	QModelIndex index_33 = model_2->index(7, 1, QModelIndex());
	model_2->setData(index_33, ui->numEpochs->text());

	/******** TODO: add the comboBoxes **********/
	QModelIndex index_34 = model_2->index(8, 1, QModelIndex());
	model_2->setData(index_34, ui->comboBox_optimizer->currentText());
	QModelIndex index_35 = model_2->index(9, 1, QModelIndex());
	model_2->setData(index_35, ui->comboBox_lossFunc->currentText());

	ui->tableView_2->setModel(model_2);
	/*
		file.flush();
		file.close();
		*/
}

void MainWindow::on_layerbutton_clicked()
{
	QString str_layer = ui->layer->currentText(); // to store the layer name and display it in the excel sheet

	static int counter = 0;
	static int input_width = (ui->inputsize->text()).toInt();
	static int input_height = (ui->InputHeight->text()).toInt();
	static int input_channel = 0;
	static int flag = 1;
	static int fc_flag = 1;
	int flatten_flag = 0;

	/*
		QString filter_out = "N/A";
		QString stride_out = "N/A";
		QString kernal_out = "N/A";
		QString unit_out = "N/A";
	*/

	if (ui->RGB->isChecked() && flag)
	{
		input_channel = 3;
		flag = 0;
	}
	else if (ui->GrayScale->isChecked() && flag)
	{
		input_channel = 1;
		flag = 0;
	}

	static int conv_flag = 1;

	if (str_layer == "Convolution")
	{
		if (conv_flag)
		{
			convolution.name = "conva";
			conv_flag = 0;
		}
		else
		{
			convolution.name = "convb";
			conv_flag = 1;
		}
		convolution.kernel_size = (ui->kernelsize->text()).toInt();
		convolution.stride = (ui->stride->text()).toInt();
		convolution.filters = (ui->filters->text()).toInt();
		convolution.units = (ui->units->text()).toInt();
		convolution.height = input_height;
		convolution.width = input_width;
		convolution.channels = input_channel;
		convolution.padding = ui->yes->isChecked() ? 1 : 0;
	}

	if (str_layer == "Average pool")
	{
		convolution.name = "avgpool";
		convolution.kernel_size = (ui->kernelsize->text()).toInt();
		convolution.stride = (ui->stride->text()).toInt();
		convolution.filters = input_channel;
		convolution.units = (ui->units->text()).toInt();
		convolution.height = input_height;
		convolution.width = input_width;
		convolution.channels = input_channel;
		convolution.padding = ui->yes->isChecked() ? 1 : 0;
	}

	if (str_layer == "Max pool")
	{
		convolution.name = "maxpool";
		convolution.kernel_size = (ui->kernelsize->text()).toInt();
		convolution.stride = (ui->stride->text()).toInt();
		convolution.filters = input_channel;
		convolution.units = (ui->units->text()).toInt();
		convolution.height = input_height;
		convolution.width = input_width;
		convolution.channels = input_channel;
		convolution.padding = ui->yes->isChecked() ? 1 : 0;
	}

	if (str_layer == "Depthwise convolution")
	{
		convolution.name = "depthwise";
		convolution.kernel_size = (ui->kernelsize->text()).toInt();
		convolution.stride = (ui->stride->text()).toInt();
		convolution.filters = (ui->filters->text()).toInt();
		convolution.units = (ui->units->text()).toInt();
		convolution.height = input_height;
		convolution.width = input_width;
		convolution.channels = input_channel;
		convolution.padding = ui->yes->isChecked() ? 1 : 0;
	}

	if (str_layer == "Flatten")
	{
		flatten_flag = 1;
	}

	if (str_layer == "Fully Connected")
	{
		convolution.name = "FC";
		convolution.kernel_size = 1;
		convolution.stride = 1;
		convolution.filters = (ui->filters->text()).toInt();
		convolution.units = convolution.filters;
		convolution.height = 1;
		convolution.width = 1;
		if (fc_flag)
		{
			convolution.channels = input_width * input_height * input_channel;
			fc_flag = 0;
		}
		else
		{
			convolution.channels = input_channel;
		}
		convolution.padding = ui->yes->isChecked() ? 1 : 0;
	}
	QString is_padding;
	is_padding = ui->yes->isChecked() ? "yes" : "no";

	if (str_layer == "Fully Connected")
	{

		QModelIndex index_1 = model->index(table_row, 0, QModelIndex());
		model->setData(index_1, convolution.name);
		QModelIndex index_2 = model->index(table_row, 1, QModelIndex());
		model->setData(index_2, "N/A");
		QModelIndex index_3 = model->index(table_row, 2, QModelIndex());
		model->setData(index_3, convolution.filters);
		QModelIndex index_4 = model->index(table_row, 3, QModelIndex());
		model->setData(index_4, "N/A");
		QModelIndex index_5 = model->index(table_row, 4, QModelIndex());
		model->setData(index_5, "N/A");
		QModelIndex index_6 = model->index(table_row, 5, QModelIndex());
		model->setData(index_6, "N/A");
	}
	else if (str_layer == "Flatten")
	{

		QModelIndex index_1 = model->index(table_row, 0, QModelIndex());
		model->setData(index_1, "Flatten");
		QModelIndex index_2 = model->index(table_row, 1, QModelIndex());
		model->setData(index_2, "N/A");
		QModelIndex index_3 = model->index(table_row, 2, QModelIndex());
		model->setData(index_3, "N/A");
		QModelIndex index_4 = model->index(table_row, 3, QModelIndex());
		model->setData(index_4, "N/A");
		QModelIndex index_5 = model->index(table_row, 4, QModelIndex());
		model->setData(index_5, "N/A");
		QModelIndex index_6 = model->index(table_row, 5, QModelIndex());
		model->setData(index_6, "N/A");
	}
	else if (str_layer == "Max pool" || str_layer == "Average pool")
	{
		QModelIndex index_1 = model->index(table_row, 0, QModelIndex());
		model->setData(index_1, convolution.name);
		QModelIndex index_2 = model->index(table_row, 1, QModelIndex());
		model->setData(index_2, convolution.kernel_size);
		QModelIndex index_3 = model->index(table_row, 2, QModelIndex());
		model->setData(index_3, "N/A");
		QModelIndex index_4 = model->index(table_row, 3, QModelIndex());
		model->setData(index_4, convolution.stride);
		QModelIndex index_5 = model->index(table_row, 4, QModelIndex());
		model->setData(index_5, convolution.units);
		QModelIndex index_6 = model->index(table_row, 5, QModelIndex());
		model->setData(index_6, "N/A");
	}
	else
	{
		QModelIndex index_1 = model->index(table_row, 0, QModelIndex());
		model->setData(index_1, convolution.name);
		QModelIndex index_2 = model->index(table_row, 1, QModelIndex());
		model->setData(index_2, convolution.kernel_size);
		QModelIndex index_3 = model->index(table_row, 2, QModelIndex());
		model->setData(index_3, convolution.filters);
		QModelIndex index_4 = model->index(table_row, 3, QModelIndex());
		model->setData(index_4, convolution.stride);
		QModelIndex index_5 = model->index(table_row, 4, QModelIndex());
		model->setData(index_5, convolution.units);
		QModelIndex index_6 = model->index(table_row, 5, QModelIndex());
		model->setData(index_6, is_padding);
	}

	table_row += 1;
	if (flatten_flag == 1)
	{
		return;
	}
	arr[counter] = convolution;
	counter = counter + 1;
	layers = counter;
	input_height = ui->yes->isChecked() ? input_height : (input_height - convolution.kernel_size) / convolution.stride + 1;
	input_width = ui->yes->isChecked() ? input_width : (input_width - convolution.kernel_size) / convolution.stride + 1;
	input_channel = convolution.filters;
	layer_number += 1;
}

void MainWindow::on_Arch_clicked()
{

	nlohmann::json root;
	nlohmann::json params;
	for (int i = 0; i < layers; i++)
	{
		nlohmann::json layer;

		layer["kernel_size"] = arr[i].kernel_size;
		layer["filters"] = arr[i].filters;
		layer["units"] = arr[i].units;
		layer["width"] = arr[i].width;
		layer["height"] = arr[i].height;
		layer["channels"] = arr[i].channels;
		layer["stride"] = arr[i].stride;
		layer["padding"] = arr[i].padding;
		layer["name"] = arr[i].name.toStdString();
		root["layers"].push_back(layer);
	}
	params["batch_size"] = batch_size.toStdString();
	params["learning_rate"] = learning_rate.toStdString();
	params["num_epochs"] = num_epochs.toStdString();
	params["csv_path"] = csv_path.toStdString();
	params["optimizer"] = optimizer.toStdString();
	params["loss_fun"] = loss_fun.toStdString();
	params["train"] = train;
	root["params"].push_back(params);

	std::ofstream file("arch.json");
	file << root;
	file.close();
	// ui->generatedFiles->addItem("arch.json");
	/*
	Json::Value root;
		for (int i = 0; i < 100; i++) {
			Json::Value layer;
			layer["kernel_size"] = arr[i].kernel_size;
			layer["filters"] = arr[i].filters;
			layer["units"] = arr[i].units;
			layer["width"] = arr[i].width;
			layer["height"] = arr[i].height;
			layer["channels"] = arr[i].channels;
			layer["stride"] = arr[i].stride;
			layer["padding"] = arr[i].padding;
			layer["name"] = arr[i].name.toStdString();
			root["layers"].append(layer);
		}
		std::ofstream file("arr.json");
		file << root;
		file.close();

*/

	/*
		QFile file2 ("C:/Users/user/Desktop/Generator/Architecture.csv"); //to create this file in this path
		if(!file2.open(QFile::WriteOnly | QFile::Truncate))
		{
			QMessageBox:: warning (this, "title", "file is not open");
		}

		QTextStream out (&file2); // this is an object (out) to write to the file, and it takes the reference of my file

		for (int i = 0 ; i < layer_number; i++ )
		{
		  out << "layer name" << "," << arr[i].name<< i + 1 << "\n" << "kernel size" << "," << arr[i].kernel_size  << "\n" << "stride" << "," <<arr[i].stride << "\n"
			  <<"input width" << "," << arr[i].width << "\n" << "input height" << "," << arr[i].height << "\n"<<"input channels" <<","<<arr[i].channels <<"\n"
			  << "No of filters" <<"," << arr[i].filters << "\n" << "No of units" << "," << arr[i].units << "\n" << "padding" << "," << arr[i].padding << "\n";
		}

		file2.flush();
		file2.close();
		*/
}

void MainWindow::on_generate_clicked()
{
	QString scriptPath = "C:/Users/mourr/OneDrive/Desktop/gradProject-behairy/CNN.py";
	// Create a QProcess object
	QProcess *process = new QProcess(this);
	// Set the working directory to the directory containing the script
	process->setWorkingDirectory(QFileInfo(scriptPath).path());
	// Set the process to use merged output channels
	process->setProcessChannelMode(QProcess::MergedChannels);
	// Connect the readyRead signal to a slot that will handle the script's output
	connect(process, &QProcess::readyRead, this, &MainWindow::onProcessModelReady);
	// Start the process using the "python" command and the path to the script as arguments
	process->start("python", QStringList() << scriptPath);

	ui->generatedFiles->addItem("model.py");
}
void MainWindow::on_train_clicked()
{
	train = 1;
	on_Arch_clicked();
	on_generate_clicked();
	QString scriptPath = "C:/Users/mourr/OneDrive/Desktop/gradProject-behairy/train.py";
	// Create a QProcess object
	QProcess *process = new QProcess(this);
	// Set the working directory to the directory containing the script
	process->setWorkingDirectory(QFileInfo(scriptPath).path());
	// Set the process to use merged output channels
	process->setProcessChannelMode(QProcess::MergedChannels);
	// Connect the readyRead signal to a slot that will handle the script's output
	connect(process, &QProcess::readyRead, this, &MainWindow::onProcessTrainReady);
	// Start the process using the "python" command and the path to the script as arguments
	process->start("python", QStringList() << scriptPath);

	ui->systemC->setEnabled(true);
	ui->generatedFiles->addItem("train.py");
}

void MainWindow::onProcessModelReady()
{
	// Get the QProcess object that sent the signal
	QProcess *process = qobject_cast<QProcess *>(sender());
	// Read the output of the process
	QString output = process->readAll();
	// Display the output in a QTextEdit or QPlainTextEdit widget in the frame
}
void MainWindow::onProcessTrainReady()
{
	// Get the QProcess object that sent the signal
	QProcess *process = qobject_cast<QProcess *>(sender());
	// Read the output of the process
	QString output = process->readAll();
	// Display the output in a QTextEdit or QPlainTextEdit widget in the frame
}

void MainWindow::on_systemC_clicked()
{

	ui->generatedFiles->addItem("Initiator.h");
	ui->generatedFiles->addItem("Initiator.cpp");
	ui->generatedFiles->addItem("Target.h");
	ui->generatedFiles->addItem("TestBench.cpp");
	ui->generatedFiles->addItem("main.cpp");
}

void MainWindow::on_layer_currentIndexChanged(int index)
{
	// model = new QStandardItemModel (2, 6 , this);
	// model->insertRow(2);
	ui->label_8->show();
	ui->filters->show();
	ui->label_6->show();
	ui->label_9->show();
	ui->label_10->show();
	ui->kernelsize->show();
	ui->stride->show();
	ui->units->show();
	ui->padding->show();

	if (index == 1 | index == 2)
	{
		ui->label_8->hide();
		ui->filters->hide();
		ui->padding->hide();
	}
	else if (index == 5)
	{
		ui->label_6->hide();
		ui->label_9->hide();
		ui->label_10->hide();
		ui->kernelsize->hide();
		ui->stride->hide();
		ui->units->hide();
		ui->padding->hide();
	}
	else if (index == 4)
	{
		ui->label_6->hide();
		ui->label_9->hide();
		ui->label_10->hide();
		ui->kernelsize->hide();
		ui->stride->hide();
		ui->units->hide();
		ui->padding->hide();
		ui->label_8->hide();
		ui->filters->hide();
	}
}

void MainWindow::on_generatedFiles_itemSelectionChanged()
{
	QString indata = ui->generatedFiles->currentItem()->text();

	QFile file_4("C:/Users/mourr/OneDrive/Desktop/gradProject-behairy/" + indata);
	if (!file_4.open(QIODevice::ReadOnly))
		QMessageBox::information(0, "info", file_4.errorString());
	QTextStream in(&file_4);
	ui->codeSample->setText(in.readAll());
}
