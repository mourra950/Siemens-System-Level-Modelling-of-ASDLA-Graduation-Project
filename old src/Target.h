#pragma once
#ifndef TARGET_H
#define TARGET_H

#include <systemc.h>
#include "tlm.h"
#include "tlm_utils/simple_target_socket.h"
#include <vector>
#include "json/json.hpp"

using json = nlohmann::json;

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

        //Check the output is received correctly in the target
     /* cout << "Input received in Target module: ";
        for (int i = 0; i < 50; ++i) {
            cout << input_data[i] << " ";
        }
        cout << endl;*/

        torch::jit::Module module;
        torch::Device device = torch::cuda::is_available() ? torch::kCUDA : torch::kCPU;

        try {
            // Deserialize the ScriptModule from a file using torch::jit::load().
            //module = torch::jit::load("E:\\courses\\Graduation Project\\traced_GoogleLeNet_model.pt");
            module = torch::jit::load("E:\\courses\\Graduation Project\\Final_SystemC\\Final_SystemC\\vgg16.pt");
            module.to(device);
            module.eval();
        }
        catch (const c10::Error& e) {
            cerr << "error loading the model\n" << e.msg();
            return;
        }
        vector<torch::jit::IValue> ivalueVector;

        int batch_size = 1; int num_channels = 3; int height = 224; int width = 224;
        // int batch_size = 1; int num_channels = 1; int height = 28; int width = 28;
         // Reshape the input tensor 
        at::Tensor input_tensor = torch::from_blob(input_data, { batch_size, height, width, num_channels }).permute({ 0, 3, 1, 2 });

        ivalueVector.push_back(input_tensor);
        //cout << "Inputs: " << ivalueVector << "\n";

        // Pass ivalueVector to the forward function
        clock_t start = clock();
        at::Tensor output = module.forward(ivalueVector).toTensor();
        clock_t end = clock();

        // Post-process the output
        at::Tensor probabilities = torch::softmax(output, 1);

        ///////////////////////////////////////////////////
        /*auto data2_ptr = probabilities.data_ptr<float>();
        int64_t num_of_elements = probabilities.numel();
        vector<float> prob_vector(num_of_elements);
        for (int64_t i = 0; i < num_of_elements; ++i) {
            prob_vector[i] = data2_ptr[i];
        }
        sort(prob_vector.begin(), prob_vector.end());*/
        /////////////////////////////////////////////////
        auto results = probabilities.sort(1, true);
        // Calculate the duration
        double duration = double(end - start) / CLOCKS_PER_SEC;
        // Output the time taken
        cout << "\nInference Time taken: " << duration << " seconds" << endl;

        //cout << probabilities;
        // Print the top 5 predicted classes
        const int kTopK = 5;
        at::Tensor topk_values = get<0>(results).narrow(1, 0, kTopK);
        at::Tensor topk_indices = get<1>(results).narrow(1, 0, kTopK);

        // Access the underlying data as a C++ array 
        auto topk_values_a = topk_values.accessor<float, 2>();
        auto topk_indices_a = topk_indices.accessor<int64_t, 2>();
        ////////////////////////////////////////////////////////////////
        //Added part to convert tensor to 2D array and then flatten it
        std::vector<std::vector<float>> soft_output_array;
        // Iterate over the tensor elements and populate the array 
        for (int i = 0; i < topk_values_a.size(0); ++i) {
            std::vector<float> row;
            for (int j = 0; j < topk_values_a.size(1); ++j)
                row.push_back(topk_values_a[i][j]);
            soft_output_array.push_back(row);
        }

        // Flattening to 1D array
        // Calculate the total number of elements
        int total_elements = soft_output_array.size() * soft_output_array[0].size();
        // Create a contiguous 1D array and copy the elements
        flattened_array.resize(total_elements);
        //cout << "\n1D array: ";
        for (int j = 0; j < total_elements; j++) {
            flattened_array[j] = soft_output_array[0][j];
            //cout << flattened_array[j];
        }
        ////////////////////////////////////////////////////////////////////////////////
        cout << "\n\nTop " << kTopK << " predictions:" << endl;
        for (int i = 0; i < kTopK; i++) {
            cout << "Class: " << topk_indices_a[0][i] << ", Probability: " << topk_values_a[0][i] << endl;
        }

        ifstream file("E:\\courses\\Graduation Project\\Final_SystemC\\Final_SystemC\\imagenet_class_index.json");

        if (!file.is_open()) {
            cerr << "Failed to open the JSON file." << endl;
            return;
        }

        json jsonData;
        file >> jsonData;
        file.close();

        // Access the JSON data
        // Example: printing the value of a key 
        string key = to_string(topk_indices_a[0][0]);
        cout << "Predicted Class: " << jsonData[key][1] << endl;

        ////////////////////////////////////////////////////////////////////////////////
        // Access the underlying data as a C++ array 
    /*    auto soft_output_accessor = probabilities.accessor<float, 2>();
        vector<vector<float>> soft_output_array;
        // Iterate over the tensor elements and populate the array
        for (int i = 0; i < soft_output_accessor.size(0); ++i) {
            vector<float> row;
            for (int j = 0; j < soft_output_accessor.size(1); ++j)
                row.push_back(soft_output_accessor[i][j]);
            soft_output_array.push_back(row);
        }

         // Flattening to 1D array
         // Calculate the total number of elements
        int total_elements = soft_output_array.size() * soft_output_array[0].size();

        // Create a contiguous 1D array and copy the elements
        int index = 0;
        flattened_array.resize(total_elements);
        // cout << "\n1D array: ";
        for (int j = 0; j < total_elements; j++) {
            flattened_array[j] = soft_output_array[0][j];
            //cout << flattened_array[j];
        }*/

        // Set the data pointer and length in the payload
        payload.set_data_ptr(reinterpret_cast<unsigned char*>(flattened_array.data()));
        payload.set_data_length(total_elements * sizeof(float));

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

#endif  // TARGET_H

