#include "Initiator.h"
#include "extension.cpp"
using json = nlohmann::json;
using namespace std;
using namespace sc_core;
using namespace tlm;
using namespace torch;

void Initiator::sendDataThread()
{
    cout << "\nahmed\n";
    tlm::tlm_generic_payload trans;
    my_extension *incr_cmd_extension = new my_extension;
    incr_cmd_extension->id = 5;
    trans.set_extension(incr_cmd_extension);
    trans.set_command(tlm::TLM_WRITE_COMMAND);
    sc_time delay;

    init_socket->b_transport(trans, delay);
    incr_cmd_extension->id = 12;
    init_socket->b_transport(trans, delay);

    return;

    // sc_time tLOCAL(SC_ZERO_TIME);
    // unsigned int addr = static_cast<unsigned int>(rand() % 0x100);
    // cout << "address: " << addr << "\n";
    // std::string mnistpath = "E:/FinalBehairy/examples-main/cpp/mnist/build/data"; // currently working on a code to make it dynamic
    // auto dataset1 = torch::data::datasets::MNIST(mnistpath, torch::data::datasets::MNIST::Mode::kTest);
    // auto dataset = dataset1.map(torch::data::transforms::Stack<>());
    // // Access a specific image from the dataset
    // size_t index = 15; // Index of the image to extract
    // auto example = dataset.get_batch({index});
    // // Extract the image and label
    // torch::Tensor image2 = example.data[0];
    // torch::Tensor label = example.target[0];
    // // cout << "image 20 " << image2 << "\n label" << label;
    // // // Add an extra dimension to the image2 tensor.
    // // image2 = image2.unsqueeze(1);
    // // cout << "image 21 " << image2 << "\n label" << label;
    // // Print the shape of the image tensor and count the total number of elements in a tensor.
    // cout << "Image shape: " << image2.sizes() << endl
    //      << "Image Label: " << label << " "
    //      << "\n\n";
    // int64_t num_elements = image2.numel();
    // // Create a vector to store the tensor elements from the Mnist dataset Image
    // // cout << "Image vector extraced from Mnist: ";
    // vector<float> image_vector(num_elements);
    // auto data_ptr = image2.data_ptr<float>();
    // for (int64_t i = 0; i < num_elements; ++i)
    // {
    //     image_vector[i] = data_ptr[i];
    //     // cout << image_vector[i] << " ";
    // }
    // int image_size = image_vector.size() * sizeof(float);
    // cout << "\n";
    // // Create a payload for the transaction
    // tlm_generic_payload payload;
    // payload.set_data_ptr(reinterpret_cast<unsigned char *>(image_vector.data()));
    // payload.set_data_length(image_size);
    // payload.set_write();
    // clock_t start2 = clock();
    // // Send the payload through the init_socket
    // SC_REPORT_INFO("Initiator", "Doing a WRITE transaction");
    // init_socket->b_transport(payload, tLOCAL);
    // cout << "\n-------------------------------------------------------------------------------------------------------------------------\n";
    // // Extract the input data from the payload
    // float *extracted_input_data = reinterpret_cast<float *>(payload.get_data_ptr());
    // int input_size2 = payload.get_data_length() / sizeof(float);
    // // Output the time taken
    // cout << "Inputs received in initiator module: ";
    // for (int i = 0; i < input_size2; ++i)
    //     cout << extracted_input_data[i] << " ";
    // cout << endl;
    // // Handle response or check for errors
    // if (payload.is_response_error())
    //     SC_REPORT_ERROR("Initiator", "Received error reply.");
    // else
    //     SC_REPORT_INFO("Initiator", "Received correct reply.");
}
