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
import imgurl from "/celeste.jpg";
export default function page1() {
  return (
    <>
      <h1>Experience</h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        As an aspiring professional in the field of technology, I am constantly
        seeking new opportunities to broaden my knowledge and expertise. I
        believe that it is important to continuously challenge myself by taking
        various courses and participating in competitions in different fields.
        Through platforms such as Udemy, Coursera, and CS50, I have been able to
        explore various technologies and expand my skill set. Additionally, I am
        always eager to learn and embrace new technologies, and I am open to
        taking on any opportunity that allows me to further develop my knowledge
        and expertise. This mindset has enabled me to constantly evolve and
        adapt to the rapidly changing technology landscape, and I am excited to
        continue on this path of growth and learning.{" "}
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        <Image style={{ padding: "20px 0 20px 0" }} src={imgurl} />
        asdasdasdqwdq
      </Paragraph>
      
    </>
  );
}
