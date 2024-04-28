/* eslint-disable no-unused-vars */
import {
  Button,
  Layout,
  Typography,
  Row,
  Col,
  Card,
  Divider,
  Image,
} from "antd";
const { Content } = Layout;
import { Grid } from "antd";
const { Paragraph } = Typography;
import imgomar from "/faces/omar2.png";
import CV from "/CV.pdf";
function Teamprofile({ name, linkat, ima }) {
  return (
    <div>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        <Row>
          <Col flex="auto" className="centerme" md={24} lg={12}>
            <Image style={{ padding: "20px 0 20px 0" }} src={ima} />
          </Col>
          <Col className="centerme" flex="auto" md={24} lg={12}>
            <p>{name}</p>
            <ul>
              {linkat.map((link, index) => (
                <li key={index} style={{ listStyleType: "none" }}>
                  {link.name}: <a href={link.href}>{link.text}</a>
                </li>
              ))}
              {name == "Omar Yousef" ? (
                <li>
                  CV:{" "}
                  <a
                    href={CV}
                    download="Example-PDF-document"
                    target="_blank"
                    rel="noreferrer"
                  >
                    Download
                  </a>
                </li>
              ) : (
                <></>
              )}
            </ul>
          </Col>
        </Row>
      </Paragraph>
    </div>
  );
}

export { Teamprofile };
