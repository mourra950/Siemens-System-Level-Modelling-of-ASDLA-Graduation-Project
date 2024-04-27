import { useState } from "react";
import "./App.css";
import { Content } from "antd/es/layout/layout";
import Sider from "antd/es/layout/Sider";
import { Layout } from "antd";
import pages from "./pages/pages";
const style1 = {
  textAlign: "center",
  color: "#fff",
  backgroundColor: "#7dbcea",
  height: "100vh",
  overflow: "auto",
};
// const style2 = {
//   textAlign: "center",
//   color: "#fff",
//   backgroundColor: "#7dbcea",
// };

function App() {
  const [pageContent, setPageContent] = useState("");
  return (
    <>
      <Layout>
        <Sider breakpoint="lg" style={style1}>
          {pages.map((page, index) => (
            <button key={index} onClick={()=>setPageContent(page.content)}>
              {page.name}
            </button>
          ))}
        </Sider>
        <Content className="Content">{pageContent}</Content>
      </Layout>
    </>
  );
}

export default App;
