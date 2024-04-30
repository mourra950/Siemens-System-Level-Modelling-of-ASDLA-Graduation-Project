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
const { Paragraph } = Typography;
import imgurl from "/Images/sponsor/siemens.png";
export default function page1() {
  return (
    <>
      <h1>Experience</h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        As an aspiring professional in the field of technology, I am constantly
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        <Image style={{ padding: "20px 0 20px 0" }} src={imgurl} />
        asdasdasdqwdq
      </Paragraph>

    </>
  );
}
