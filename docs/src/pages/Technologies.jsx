/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Paragraph } = Typography;
import github from "/tech/Github.png";
import jinja from "/tech/Jinja.png";
import python from "/tech/python.png";
import pytorch from "/tech/pytorch.png";
import react from "/tech/react.png";
import systemc from "/tech/systemc.png";
import cpp from "/tech/cpp.png";
import qt from "/tech/Qt.png";

export default function project() {
  return (
    <>
      <h1>Technologies used in this project</h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        During this project different technologies were used to obtain optimal
        peformance and usability
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        <Row>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={github} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={jinja} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={python} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={pytorch} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={react} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={systemc} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={cpp} />
          </Col>
          <Col flex="auto" className="centerme" md={6}>
            <Image style={{ padding: "20px 0 20px 0" }} src={qt} />
          </Col>
        </Row>
      </Paragraph>
    </>
  );
}
