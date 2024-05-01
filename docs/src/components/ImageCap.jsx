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
function ImageCap({ fignum, description, imagesrc }) {
  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      {" "}
      <Image style={{ padding: "20px 0 20px 0" }} src={imagesrc} />
      <p style={{ textAlign: "center", margin: "10px" }}>
        <b>Figure {fignum} :</b>
        {description}
      </p>
    </div>
  );
}

export { ImageCap };
