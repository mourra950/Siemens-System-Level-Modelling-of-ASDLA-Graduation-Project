#include <iostream>
#include <string>
#include <memory>
#include <vector>
#include <torch/script.h>
#include <torch/torch.h>
#include <torch/nn.h>
#include <torch/optim.h>
#include <torch/data/example.h>
#include <torch/csrc/jit/serialization/import.h>
#include "systemc.h"
#include "tlm.h"
#include "tlm_utils/simple_initiator_socket.h"
#include <opencv2/opencv.hpp>
#include <random>
#include <fstream>
#include <ctime>
#include "json/json.hpp"
#include "Initiator.h"

using json = nlohmann::json;
using namespace std;
using namespace sc_core;
using namespace tlm;

using namespace tlm;

void Initiator::sendDataThread() {
    tlm_generic_payload payload;
    sc_time tLOCAL(SC_ZERO_TIME);

    unsigned int addr = static_cast<unsigned int>(rand() % 0x100);
    cout << "address: " << addr << "\n";
    ////////////////////////////////////////////////////////////////////////////////

    // Preprocess the input image
    cv::Mat image = cv::imread("E:\\courses\\Graduation Project\\Final_SystemC\\Final_SystemC\\ILSVRC2017_test_00000014.JPEG");
    cv::resize(image, image, cv::Size(224, 224));
    cv::cvtColor(image, image, cv::COLOR_BGR2RGB);
    image.convertTo(image, CV_32FC3, 1.0 / 255.0);
    cv::Mat normalized_image = (image - cv::Scalar(0.485, 0.456, 0.406)) / cv::Scalar(0.229, 0.224, 0.225);
    torch::Tensor tensor_image = torch::from_blob(normalized_image.data, { 1, image.rows, image.cols,3 }).permute({ 0, 3, 1, 2 });
    // cout<<"\n"<< tensor_image.sizes();

         // cout << "\ntensor: " << tensor_image;
    int64_t num_elements = tensor_image.numel();
    vector<float> image_vector(num_elements);
    auto data_ptr = tensor_image.data_ptr<float>();
    for (int64_t i = 0; i < num_elements; ++i) {
        image_vector[i] = data_ptr[i];
    }

    //cout << "Inputs: " << myVector << "\n";
    ////////////////////////////////////////////////////////////////////////////////
    // Create a payload for the transaction
    int image_size = image_vector.size() * sizeof(float);
    payload.set_data_ptr(reinterpret_cast<unsigned char*>(image_vector.data()));
    payload.set_data_length(image_size);
    payload.set_write();

    // Send the payload through the init_socket
    SC_REPORT_INFO("Initiator", "Doing a WRITE transaction");
    init_socket->b_transport(payload, tLOCAL);

    cout << "\n---------------------------------------------------------------------------------------------\n";
    // Extract the input data from the payload
    float* extracted_input_data = reinterpret_cast<float*>(payload.get_data_ptr());
    int input_size2 = payload.get_data_length() / sizeof(float);
    cout << "Inputs received in initiator module: ";
    for (int i = 0; i < input_size2; ++i)
        cout << extracted_input_data[i] << " ";

    cout << endl;
    // Handle response or check for errors
    if (payload.is_response_error())
        SC_REPORT_ERROR("Initiator", "Received error reply.");
    else
        SC_REPORT_INFO("Initiator", "Received correct reply.");
}