#include "Target.h"
#include "extension.cpp"
#include <iostream>
using namespace cv;

void showImage(Mat image)
{
    namedWindow("Display window", cv::WindowFlags::WINDOW_NORMAL); // Create a window for display.
    imshow("Display window", image);
    waitKey(0);
}


Target::Target(sc_core::sc_module_name name) : sc_core::sc_module(name), target_socket("target_socket")
{
    target_socket.register_b_transport(this, &Target::b_transport);
}


void Target::b_transport(tlm::tlm_generic_payload &trans, sc_core::sc_time &t)
{
   
    // Read image from the path using imread
    auto image = imread("E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/examples/SystemC_Ctorch/build2/image_samples/img_1.jpg");
    // Use show image to show the read image
    // showImage(image);
    torch::Device device = torch::cuda::is_available() ? torch::kCUDA : torch::kCPU;
    cout << torch::cuda::is_available()<<device << " device"<<endl;
    //torch::Device device(torch::kCUDA);
    // Torch Test
    cout << "Ahmed MOhamed" << endl;
    // 
    // Load and deserialize Pt file created by saving the model after training in python
    auto module = torch::jit::load("E:/Github/Siemens-System-Level-Modelling-of-ASDLA-Graduation-Project/examples/SystemC_Ctorch/build2/Pt/model2.pt");
    module.to(device);
    cout << "Ahmed" << endl;

    // size of the image
    auto sizes = {1, 1, image.rows, image.cols};
    // transform to tensor
    auto tensor_image = torch::from_blob(image.data, {1, 3, 28, 28});
    tensor_image = tensor_image.to(device);//Type(at::kFloat);
    // make image go through the model
    cout << "Ahmed"<<endl;

    auto result = module.forward({tensor_image}).toTensor();
    auto max_result = result.max(1, true);
    auto max_index = std::get<1>(max_result).item<float>();
    // Print predication
    std::cout << "\nprinting the image prediction " << max_index << endl;

    // Reading the payload and check the transaction command
    tlm::tlm_command cmd = trans.get_command();
    my_extension *test_extension_transaction;
    trans.get_extension(test_extension_transaction);
    cout << test_extension_transaction->id
         << endl;

    if (cmd != tlm::TLM_IGNORE_COMMAND)
    {
        trans.set_response_status(tlm::TLM_GENERIC_ERROR_RESPONSE);
        return;
    }

    trans.set_response_status(tlm::TLM_OK_RESPONSE);
}