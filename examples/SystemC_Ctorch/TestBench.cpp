/*#include <iostream>
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
#include "tlm_utils/simple_target_socket.h"
#include <opencv2/opencv.hpp>
#include <random>
#include <fstream>
#include <ctime>
#include "json/json.hpp"
using json = nlohmann::json;
using namespace std;
using namespace sc_core;
using namespace tlm;

clock_t start;
SC_MODULE(Initiator) {
    tlm_utils::simple_initiator_socket<Initiator> init_socket;

    SC_CTOR(Initiator) : init_socket("init_socket") {
        SC_THREAD(sendDataThread);
    }

    void sendDataThread() {
        sc_time tLOCAL(SC_ZERO_TIME);
        unsigned int addr = static_cast<unsigned int>(rand() % 0x100);
        cout << "address: " << addr << "\n";

        // Create the MNIST dataset
        string mnistRoot = "MNIST/raw";

        auto dataset = torch::data::datasets::MNIST(mnistRoot, torch::data::datasets::MNIST::Mode::kTest).map(torch::data::transforms::Stack<>());

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

        // Send the payload through the init_socket
        SC_REPORT_INFO("Initiator", "Doing a WRITE transaction");
        init_socket->b_transport(payload, tLOCAL);

        cout << "\n-------------------------------------------------------------------------------------------------------------------------\n";
        // Extract the input data from the payload
        float* extracted_input_data = reinterpret_cast<float*>(payload.get_data_ptr());
        int input_size2 = payload.get_data_length() / sizeof(float);

        clock_t end2 = clock();
        double duration2 = double(end2 - start) / CLOCKS_PER_SEC;
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
};

SC_MODULE(Target) {
    tlm_utils::simple_target_socket<Target> target_socket;

    SC_CTOR(Target) : target_socket("target_socket") {
        target_socket.register_b_transport(this, &Target::b_transport);
    }
    vector<float> flattened_array;

    void b_transport(tlm_generic_payload & payload, sc_time & tLOCAL) {

        // Extract the input data from the payload
        float* input_data = reinterpret_cast<float*>(payload.get_data_ptr());
        int input_size = payload.get_data_length() / sizeof(float);

        torch::jit::Module module;
        torch::Device device = torch::cuda::is_available() ? torch::kCUDA : torch::kCPU;

        try {
            // Deserialize the ScriptModule from a file using torch::jit::load().
            //module = torch::jit::load("E:\\courses\\Graduation Project\\traced_GoogleLeNet_model.pt");
            module = torch::jit::load("trained_model.pt");
            module.to(device);
            module.eval();
        }
        catch (const c10::Error& e) {
            cerr << "error loading the model\n" << e.msg();
            return;
        }
        vector<torch::jit::IValue> ivalueVector;
        // int batch_size = 1; int num_channels = 3; int height = 224; int width = 224;
        int batch_size = 1; int num_channels = 1; int height = 28; int width = 28;
        // Reshape the input tensor 
        at::Tensor input_tensor = torch::from_blob(input_data, { batch_size,num_channels, height, width });

        ivalueVector.push_back(input_tensor);
        //cout << "Inputs: " << ivalueVector << "\n";

        start = clock();
        // Pass ivalueVector to the forward function
        at::Tensor output = module.forward(ivalueVector).toTensor();
        clock_t end = clock();

        at::Tensor soft_output = torch::softmax(output, 1);
        at::Tensor sigm_output = torch::sigmoid(output);
        at::Tensor argmax_output = torch::argmax(output, 1);
        cout << "Predictions: " << output << '\n';
        cout << "argMax Predictions: " << argmax_output << '\n';
        cout << "SoftMax Predictions: " << soft_output << '\n';
        cout << "Sigmoid Predictions: " << sigm_output << '\n';

        ////////////////////////////////////////////////////////////////////////////////
        // Access the underlying data as a C++ array 
        auto soft_output_accessor = output.accessor<float, 2>();
        std::vector<std::vector<float>> soft_output_array;
        // Iterate over the tensor elements and populate the array 
        for (int i = 0; i < soft_output_accessor.size(0); ++i) {
            std::vector<float> row;
            for (int j = 0; j < soft_output_accessor.size(1); ++j)
                row.push_back(soft_output_accessor[i][j]);
            soft_output_array.push_back(row);
        }

        // Flattening to 1D array
        // Calculate the total number of elements
        int total_elements = soft_output_array.size() * soft_output_array[0].size();

        // Create a contiguous 1D array and copy the elements
        flattened_array.resize(total_elements);
        // cout << "\n1D array: ";
        for (int j = 0; j < total_elements; j++) {
            flattened_array[j] = soft_output_array[0][j];
            //cout << flattened_array[j];
        }

        // Set the data pointer and length in the payload
        payload.set_data_ptr(reinterpret_cast<unsigned char*>(flattened_array.data()));
        payload.set_data_length(total_elements * sizeof(float));
        cout << "\nFlattened array: ";
        for (int i = 0; i < total_elements; i++)
            cout << flattened_array[i] << " ";

        // Calculate the duration
        double duration = double(end - start) / CLOCKS_PER_SEC;
        // Output the time taken
        cout << "\n\nInference Time taken: " << duration << " seconds" << endl;

        if (payload.is_read())
            SC_REPORT_INFO("Target", "Doing a READ transaction");

        else if (payload.is_write())
            SC_REPORT_INFO("Target", "Doing a WRITE transaction");

        // Set the response status
        payload.set_response_status(TLM_OK_RESPONSE);

        // Send the response back through the target_socket
        //target_socket->b_transport(payload, tLOCAL);
    }
};

void setMKLThreads() {
    int numThreads = 4; // Set the desired number of threads
    torch::set_num_threads(numThreads);
}

int sc_main(int argc, char* argv[]) {
    setMKLThreads();
    // Create instances of the initiator and target modules
    Initiator initiator("initiator");
    Target target("target");

    // Connect the sockets
    initiator.init_socket.bind(target.target_socket);

    // Start simulation
    sc_start();

    return 0;
}*/