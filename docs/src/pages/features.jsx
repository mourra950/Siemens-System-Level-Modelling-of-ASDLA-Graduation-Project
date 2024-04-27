export default function features() {
    return(
    <div>
        <h1>Features</h1>
        <ul>
            <li>Enables users to generate Deep Learning Models, particularly CNNs, in PyTorch.</li>
            <li>Ensures the validity and correctness of models, even in the presence of user errors.</li>
            <li>Automatically computes the input shape of each layer based on the output of the preceding layer.</li>
            <li>Facilitates model training for users.</li>
            <li>Wraps the model with SystemC for enhanced functionality.</li>
            <li>Enables the monitoring and visualization of the learning process through TensorBoard.</li>
            <li>Allows users to compare between various training runs using TensorBoard.</li>
            <li>The tool remains updated with the latest PyTorch Layers through auto extraction.</li>
            <li>Allows users to conduct transfer learning with existing pretrained models.</li>
            <li>Streamlines the building process and ensures compatibility with diverse platforms.</li>
            <li>Modularized code, open for extension, and better readability.</li>
        </ul>
    </div>
    );
  }