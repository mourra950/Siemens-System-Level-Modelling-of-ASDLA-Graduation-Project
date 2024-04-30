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
import imgomar from "/Images/faces/omar2.png";
import imgbanna from "/Images/faces/banna.jpg";
import imgadham from "/Images/faces/adham.jpg";
import imgnada from "/Images/faces/nada.png";
import { Teamprofile } from "../components/teamprofile.jsx";
const omar = [
  {
    href: "https://github.com/mourra950",
    name: "Github",
    text: "mourra950",
  },
  {
    href: "https://www.linkedin.com/in/mourra950/",
    name: "Linkdin",
    text: "in/mourra950",
  },
  {
    href: "https://mourra950.github.io/Portofolio/",
    name: "Portfolio",
    text: "Awsome Portfolio",
  },
];
const banna = [
  {
    href: "https://github.com/OmarElbanna",
    name: "Github",
    text: "OmarElbanna",
  },
  {
    href: "https://www.linkedin.com/in/omar-el-banna/",
    name: "Linkdin",
    text: "in/omar-el-banna",
  },
];

const nada = [
  {
    href: "https://github.com/Nada119",
    name: "Github",
    text: "Nada119",
  },
  {
    href: "https://www.linkedin.com/in/nada-amr/",
    name: "Linkdin",
    text: "in/nada-amr",
  },
];
const adham = [
  {
    href: "https://github.com/Adham-Abdelmaksoud",
    name: "Github",
    text: "Adham-Abdelmaksoud",
  },
  {
    href: "https://www.linkedin.com/in/adham-abdelmaksoud/",
    name: "Linkdin",
    text: "in/adham-abdelmaksoud",
  },
];

export default function team() {
  return (
    <>
      <h1>Know the team</h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        We are 4 Engineers from Ain Shams University with a diverse set of
        skills.
      </Paragraph>
      <Teamprofile name={"Omar Yousef"} linkat={omar} ima={imgomar} />
      <Teamprofile name={"Omar Elbanna"} linkat={banna} ima={imgbanna} />
      <Teamprofile name={"Nada Amr"} linkat={nada} ima={imgnada} />
      <Teamprofile name={"Adham Abdelmaksoud"} linkat={adham} ima={imgadham} />
    </>
  );
}
