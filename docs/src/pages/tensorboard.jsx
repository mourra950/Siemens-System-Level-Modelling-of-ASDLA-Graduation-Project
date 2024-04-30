/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;

import scalar_dashoard from "/Images/tensorboard/scalar_dashoard.png";
import model from "/Images/tensorboard/model.png";
import histogram from "/Images/tensorboard/histogram.png";
import comparison from "/Images/tensorboard/comparison.png";


export default function TensorBoard() {
    return (
        <>
            <h1>TensorBoard</h1>
            <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>Introduction</h1>
            <Paragraph className="SE" style={{ lineHeight: "36px" }}>
                TensorBoard stands as an effective solution to the challenge of visualizing and comprehending the intricacies inherent in machine learning model development. By providing a rich set of features, TensorBoard addresses the problem of visualizing complex training processes, enabling researchers and practitioners to gain valuable insights into model performance, architecture, and parameter dynamics. Its diverse functionalities, ranging from scalar metric dashboards to real-time monitoring and remote access, collectively contribute to a holistic solution for analyzing and managing machine learning models. TensorBoard, through its intuitive interface and powerful visualization capabilities, plays a pivotal role in overcoming the visualization challenges associated with deep learning projects, ultimately enhancing the efficiency and interpretability of the model development lifecycle.
            </Paragraph>
            <Divider />
            <h2>Importance of TensorBoard Usage</h2>
            <Paragraph className="SE">
                <ul>
                    <li>
                        <strong>Scalar Dashboards:</strong>
                        <br />
                        Visualize scalar metrics over time, including training and validation loss, as well as accuracy during training and testing. This is graphically represented to track the progression of metrics throughout the training process.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={scalar_dashoard} />
                        <p>Scalar Dashboards in TensorBoard</p>
                    </li>
                    <li>
                        <strong>Graph Visualization:</strong>
                        <br />
                        Users can visualize the computational graph of their TensorFlow model, providing a clear depiction of the model's architecture and data flow through different layers.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={model} />
                        <p>Graph Visualization in TensorBoard</p>
                    </li>
                    <li>
                        <strong>Histograms:</strong>
                        <br />
                        TensorBoard provides histograms to inspect the distribution of weights and biases in the model. This is crucial for understanding how parameters evolve during training and offers insights into the dynamics of model parameters.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={histogram} />
                        <p>Histograms in TensorBoard</p>
                    </li>
                    <li>
                        <strong>Project Management:</strong>
                        <br />
                        TensorBoard can manage and organize multiple experiments or runs within a project. This is particularly useful when comparing different model architectures, hyperparameters, or training strategies. It provides a unified dashboard view for streamlined project management.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={comparison} />
                        <p>Project Management in TensorBoard</p>
                    </li>
                    <li>
                        <strong>Profile and Performance:</strong>
                        <br />
                        TensorBoard includes profiling tools to identify bottlenecks in models, enabling optimization for better performance.
                    </li>
                    <li>
                        <strong>Cross-Validation Visualization:</strong>
                        <br />
                        Utilized during model training to visualize metrics across different folds in cross-validation, enhancing the understanding of model performance in various validation scenarios.
                    </li>
                    <li>
                        <strong>Hyperparameter Tuning:</strong>
                        <br />
                        Allows tracking of performance for different hyperparameter settings over time, facilitating the hyperparameter tuning process for optimal model performance.
                    </li>
                    <li>
                        <strong>Interactive Navigation:</strong>
                        <br />
                        TensorBoard offers an interactive and user-friendly interface for navigation. Users can zoom in and out, pan across graphs, and click on data points to get detailed information. This enhances exploration and analysis of complex training dynamics.
                    </li>
                    <li>
                        <strong>Real-Time Monitoring and Remote Access:</strong>
                        <br />
                        TensorBoard allows for real-time monitoring of training progress and can be accessed remotely, enhancing flexibility for researchers and practitioners. This is particularly advantageous due to its web-based interface.
                    </li>
                    <li>
                        <strong>Exporting Visualizations:</strong>
                        <br />
                        Users can export visualizations from TensorBoard for use in presentations, reports, or papers. This supports effective communication of research outcomes through visual aids.
                    </li>
                </ul>
            </Paragraph>
            <Divider />
        </>
    );
}
