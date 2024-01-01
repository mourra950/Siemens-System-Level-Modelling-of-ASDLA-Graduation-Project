#include "Target.h"
#include "extension.cpp"
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
    // OpenCV test

    // Read image from the path using imread
    auto image = imread("./image_samples/img_1.jpg", cv::ImreadModes::IMREAD_GRAYSCALE);
    // Use show image to show the read image
    showImage(image);

    // Torch Test
    // Load and deserialize Pt file created by saving the model after training in python
    auto module = torch::jit::load("./Pt/model2.pt");
    // size of the image
    auto sizes = {1, 1, image.rows, image.cols};
    // transform to tensor
    auto tensor_image = torch::from_blob(image.data, {1, 1, 28, 28});
    tensor_image = tensor_image.toType(at::kFloat);
    // make image go through the model
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