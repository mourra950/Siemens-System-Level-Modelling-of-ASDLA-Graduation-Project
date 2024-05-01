/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;

import static_path_after1 from "/Images/cmake/static_path_after1.png";
import static_path_after2 from "/Images/cmake/static_path_after2.png";
import Declaring_Dependencies from "/Images/cmake/Declaring_Dependencies.png";
import { ImageCap } from "../../components/ImageCap";

export default function CMake() {
  return (
    <>
      <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>CMake</h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        CMake's ability to resolve static paths is a pivotal feature in project
        development. This capability streamlines the integration of external
        files and folders, ensuring a seamless process. The COPY command in
        CMake allows developers to efficiently copy and insert necessary
        components into the project structure, enhancing accessibility relative
        to the project path. This dynamic approach simplifies file management
        and contributes to a more organized and portable codebase.
        <br />
        <ImageCap
          fignum={1}
          description={"Result of using the COPY command"}
          imagesrc={static_path_after1}
        />
        <ImageCap
          fignum={2}
          description={"Result of using the COPY command"}
          imagesrc={static_path_after2}
        />
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        In parallel, CMake's dependency declaration mechanism is a robust method
        for managing project dependencies. The "find_package" method in CMake is
        a powerful tool for specifying and locating required packages or
        libraries, adding a layer of automation to the process. The use of the
        "REQUIRED" property further strengthens this declaration, signaling the
        critical nature of these dependencies to the build process. This
        systematic approach to dependency management enhances the reliability
        and stability of the build process.
        <br />
        <ImageCap
          fignum={3}
          description={"Declaring Dependencies"}
          imagesrc={Declaring_Dependencies}
        />
      </Paragraph>
      <Divider />
    </>
  );
}
