#include <iostream>
#include <fstream>
#include <string>
#include <memory>
#include <vector>
#include <torch/script.h>
#include <torch/torch.h>
#include <torch/nn.h>
#include <torch/optim.h>
#include <torch/data/example.h>
#include <torch/csrc/jit/serialization/import.h>
#include <opencv2/opencv.hpp>
#include <random>
#include <fstream>
#include <ctime>
#include "systemc.h"
#include "tlm.h"
#include "tlm_utils/simple_initiator_socket.h"
#include "Initiator.h"
#include "json/json.hpp"
using json = nlohmann::json;
using namespace std;
using namespace sc_core;
using namespace tlm;
using namespace torch;


void Initiator::sendDataThread() {
    sc_time tLOCAL(SC_ZERO_TIME);
    unsigned int addr = static_cast<unsigned int>(rand() % 0x100);
    cout << "address: " << addr << "\n";
    std::string mnistpath = "E:/FinalBehairy/examples-main/cpp/mnist/build/data";
    //torch::data::datasets::MNIST cMnist = torch::data::datasets::MNIST(mnistpath);
   // auto dataset = torch::data::make_data_loader(cMnist.map(torch::data::transforms::Stack<>()));
    


    auto dataset1 = torch::data::datasets::MNIST(mnistpath, torch::data::datasets::MNIST::Mode::kTest);
    auto dataset = dataset1.map(torch::data::transforms::Stack<>());
    
    // Access a specific image from the dataset
    size_t index = 15;  // Index of the image to extract
    auto example = dataset.get_batch({ index });

    // Extract the image and label
    torch::Tensor image2 = example.data[0];
    torch::Tensor label = example.target[0];
    //Add an extra dimension to the image2 tensor.
    image2 = image2.unsqueeze(1);

    // Print the shape of the image tensor and count the total number of elements in a tensor.
    cout << "Image shape: " << image2.sizes() << endl << "Image Label: " << label << " " << "\n\n";
    int64_t num_elements = image2.numel();

    // Create a vector to store the tensor elements from the Mnist dataset Image
   // cout << "Image vector extraced from Mnist: ";
    vector<float> image_vector(num_elements);
    auto data_ptr = image2.data_ptr<float>();
    for (int64_t i = 0; i < num_elements; ++i) {
        image_vector[i] = data_ptr[i];
        //cout << image_vector[i] << " ";
    }
    int image_size = image_vector.size() * sizeof(float);
    cout << "\n";

    // Create a payload for the transaction
    tlm_generic_payload payload;
    payload.set_data_ptr(reinterpret_cast<unsigned char*>(image_vector.data()));
    payload.set_data_length(image_size);
    payload.set_write();

    clock_t start2 = clock();
    // Send the payload through the init_socket
    SC_REPORT_INFO("Initiator", "Doing a WRITE transaction");
    init_socket->b_transport(payload, tLOCAL);

    cout << "\n-------------------------------------------------------------------------------------------------------------------------\n";
    // Extract the input data from the payload
    float* extracted_input_data = reinterpret_cast<float*>(payload.get_data_ptr());
    int input_size2 = payload.get_data_length() / sizeof(float);

    clock_t end2 = clock();
    double duration2 = double(end2 - start2) / CLOCKS_PER_SEC;
    // Output the time taken

    cout << "Inputs received in initiator module: ";
    for (int i = 0; i < input_size2; ++i)
        cout << extracted_input_data[i] << " ";

    cout << endl;
    // Handle response or check for errors
    if (payload.is_response_error())
        SC_REPORT_ERROR("Initiator", "Received error reply.");
    else
        SC_REPORT_INFO("Initiator", "Received correct reply.");

    cout << "\n\nTransaction Time taken: " << duration2 << " seconds" << endl;
}