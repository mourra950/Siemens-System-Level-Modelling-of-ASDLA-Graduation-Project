/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;
import imgurl from "/Images/sponsor/siemens.png";
export default function Pytorch() {
  return (
    <>
      <h1>
        Project Title System Level Modelling of Application Specific Deep
        Learning Accelerators{" "}
      </h1>
      <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>
        Project Description
      </h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        During the academic year 2022-2023, a CSE senior project group managed
        to build a prototype of an automated flow to generate SystemC models of
        DNN and test this in a testbench environment that use images saved
        locally and used one case study (LeNet5) as demonstrator. This year we
        are implementing more complex DNN/CNN architectures while enhancing the
        old project structure, UI, and change testing methods by using the Carla
        simulator for real-time environment testing and visual representation.
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        <Row>
          <Col className="centerme" md={24} lg={12}>
            <Image style={{ padding: "20px 0 20px 0" }} src={imgurl} />
          </Col>
          <Col className="centerme" md={24} lg={12}>
            <p>
              The project is sponsored by Siemens EDA under the supervision of
              Prof. Dr. Watheq Elkharashi, Dr. Mohamed AbdelElSalam and Teacher
              Assistant Eng. Tasneem Adel.
            </p>
          </Col>
        </Row>
      </Paragraph>
    </>
  );
}
