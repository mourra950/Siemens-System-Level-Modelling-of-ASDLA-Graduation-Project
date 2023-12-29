#pragma once
#ifndef TARGET_H
#define TARGET_H

#include <systemc.h>
#include "tlm.h"
#include "tlm_utils/simple_target_socket.h"
#include <vector>
#include "json/json.hpp"
#include <ctime>

using namespace tlm;
using namespace std;

struct Target : sc_core::sc_module {

    tlm_utils::simple_target_socket<Target> target_socket;
    vector<float> flattened_array;

    SC_CTOR(Target) : target_socket("target_socket") {
        target_socket.register_b_transport(this, &Target::b_transport);
    }

    void b_transport(tlm_generic_payload& payload, sc_time& tLOCAL) {

        // Extract the input data from the payload
        float* input_data = reinterpret_cast<float*>(payload.get_data_ptr());
        int input_size = payload.get_data_length() / sizeof(float);

        torch::jit::Module module;
        torch::Device device =  torch::kCPU;

        try {
            // Deserialize the ScriptModule from a file using torch::jit::load().
            cout << "ana";
            module = torch::jit::load("C:/Users/mourr/Downloads/model2.pt");
            module.to(device);
            module.eval();
        }
        catch (const c10::Error& e) {
            cerr << "error loading the model\n" << e.msg();
            return;
        }
        vector<torch::jit::IValue> ivalueVector;
        int batch_size = 1; int num_channels = 1; int height = 28; int width = 28;
        // Reshape the input tensor 
        at::Tensor input_tensor = torch::from_blob(input_data, { batch_size,num_channels, height, width });

        ivalueVector.push_back(input_tensor);
        //cout << "Inputs: " << ivalueVector << "\n";

        // Pass ivalueVector to the forward function
        clock_t start1 = clock();
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
        double duration = double(end - start1) / CLOCKS_PER_SEC;
        // Output the time taken
        cout << "\n\nInference Time taken: " << duration << " seconds" << endl;

        if (payload.is_read())
            SC_REPORT_INFO("Target", "Doing a READ transaction");

        else if (payload.is_write())
            SC_REPORT_INFO("Target", "Doing a WRITE transaction");

        // Set the response status
        payload.set_response_status(TLM_OK_RESPONSE);

    }
};

#endif  // TARGET_H

