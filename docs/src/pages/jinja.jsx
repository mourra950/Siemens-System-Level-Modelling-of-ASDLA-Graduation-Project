// /* eslint-disable no-unused-vars */
// import { Layout, Typography, Row, Col, Divider, Image } from "antd";
// const { Content } = Layout;
// const { Paragraph } = Typography;
// import imgurl from "/Images/sponsor/siemens.png";
// export default function Jinja() {
//     return (
//         <>
//             <h1>
//                 Jinja{" "}
//             </h1>
//             <h1 style={{ marginBottom: "32px", fontSize: "1.5vmax" }}>
//                 Project Description
//             </h1>
//             <Paragraph className="SE" style={{ lineHeight: "36px" }}>

//             </Paragraph>
//             <Divider />
//             <Paragraph className="SE">
//                 <Row>
//                     <Col className="centerme" md={24} lg={12}>
//                         <Image style={{ padding: "20px 0 20px 0" }} src={imgurl} />
//                     </Col>
//                     <Col className="centerme" md={24} lg={12}>
//                         <p>

//                         </p>
//                     </Col>
//                 </Row>
//             </Paragraph>
//         </>
//     );
// }



/* eslint-disable no-unused-vars */
import { Layout, Typography, Row, Col, Divider, Image } from "antd";
const { Content } = Layout;
const { Paragraph } = Typography;

import jinja_template_code_sample from "/Images/jinja/jinja_template_code_sample.png";
import jinja_render_code_sample from "/Images/jinja/jinja_render_code_sample.png";

export default function Jinja() {
    return (
        <>
            <h1>Jinja</h1>

            <Paragraph className="SE" style={{ lineHeight: "36px" }}>
                In our tool, Jinja is implemented and used through two main steps:
                <ol>
                    <li>
                        Jinja template code is written in a file with the extension ".py.jinja," containing the structure of the Python file to be generated. Parts of the code structure that frequently change depending on given variables are defined using Jinja variables, for loops, and if conditions. This is useful in defining the code structure of the model to be generated by the tool, and the Jinja template adjusts the generated code depending on the layers and the number of parameters to be used.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={jinja_template_code_sample} />
                        <p>Jinja Template Sample</p>
                    </li>
                    <li>
                        A Python code is written to render the Jinja template into actual Python code according to the given parameters. This is done by defining the environment that includes the template directory path and the name of the template file to be rendered. Then, the parameters of the model are passed to a function as a dictionary that renders the template into the desired code. Finally, the rendered code is written into a Python file.
                        <br />
                        <Image style={{ padding: "20px 0 20px 0" }} src={jinja_render_code_sample} />
                        <p>Jinja Render Example</p>
                    </li>
                </ol>
            </Paragraph>
            <Divider />
            <Paragraph className="SE">
                Jinja is used to replace code generation of the model and the training code, previously done by string builder, with a Jinja template rendered by a template renderer function. Three Jinja templates were created: one for the model architecture, one for the training code, and one for the residual block.
                <br />
                A generic function for Jinja template rendering converts relative paths into absolute paths during the process of rendering the template, allowing the use of relative paths in defining the paths of the Jinja templates and the directories for the output rendered Python files.
                <br />
                This function is extensively used in the CNN.py file instead of all the string builders, modularizing code generation, model code, and training code. This maintains both the single responsibility and the Open-Closed principle while decreasing lines of code in the CNN.py file from 242 lines to 143 lines, making it more readable and easier to modify.
            </Paragraph>
            <Divider />

        </>
    );
}
