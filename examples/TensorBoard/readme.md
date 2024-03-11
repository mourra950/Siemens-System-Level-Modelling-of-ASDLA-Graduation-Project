# TensorBoard Setup:

- **writer:** Initializes a SummaryWriter for logging data to TensorBoard.

## Training Loop:

- Loops over the specified number of epochs (`EPOCHS`).
- Trains the model on the training dataset and logs training accuracy and loss to TensorBoard.
- Visualizes the final layers' weights using histograms on TensorBoard at the last epoch.

## Test Evaluation:

- Evaluates the model on the test dataset and logs test accuracy to TensorBoard.
- Adds an example grid of input images to TensorBoard.

## Learning Rate and Model Weights Visualization:

- Logs the learning rate and histograms of convolutional layer weights to TensorBoard.

## Confusion Matrix Visualization:

- Computes and visualizes a confusion matrix on the test set, logging it as a figure on TensorBoard.

## ONNX Export:

- Exports the model to the ONNX format for TensorBoard visualization.
