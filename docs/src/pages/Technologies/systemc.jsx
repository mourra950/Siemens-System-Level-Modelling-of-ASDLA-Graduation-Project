/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;
import Custom_TLM_extension from "/Images/systemc/Custom_TLM_extension.png";
import how_old_project_accessed_the_data from "/Images/systemc/how_old_project_accessed_the_data.png";
import how_the_custom_tlm_extension_enable_accessing_the_data from "/Images/systemc/how_the_custom_tlm_extension_enable_accessing_the_data.png";

export default function SystemC() {
  return (
    <>
      <h1>SystemC</h1>
      <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>
        Project Description
      </h1>
      <Paragraph className="SE" style={{ lineHeight: "36px" }}>
        The SystemC methodology stands out for its ability to enhance the
        flexibility and configurability of generated SystemC code, offering
        advanced features to streamline the development process. One notable
        aspect is the provision for custom TLM (Transaction-Level Modeling)
        extensions.
        <br />
        <Image
          style={{ padding: "20px 0 20px 0" }}
          src={Custom_TLM_extension}
        />
        <p>Custom TLM Extension in SystemC</p>
        This figure visually represents the defined custom payload TLM,
        showcasing how it enables easier transactions without the need for
        casting information during transmission or reception, as in older
        projects.
      </Paragraph>
      <Divider />
      <Paragraph className="SE">
        This customization capability significantly enhances the flexibility of
        the generated SystemC code, providing a versatile environment for
        modeling and simulation. Moreover, the emphasis on enhancing the
        flexibility and configurability of the generated code demonstrates
        SystemC's commitment to accommodating diverse requirements in complex
        system design, making it a powerful choice for hardware and software
        co-design.
        <br />
        <Image
          style={{ padding: "20px 0 20px 0" }}
          src={how_old_project_accessed_the_data}
        />
        <p>How the old project accessed the data</p>
        <Image
          style={{ padding: "20px 0 20px 0" }}
          src={how_the_custom_tlm_extension_enable_accessing_the_data}
        />
        <p>How the custom TLM extension enables accessing the data</p>
      </Paragraph>
      <Divider />
    </>
  );
}
