import { useState } from "react";
import "./App.css";
import { Layout } from "antd";
const { Header, Sider, Content } = Layout;
import pages from "./pages/pages";
import { Drawer, Button, Image } from "antd";
import imgurl3 from "/Images/lego/tip.png";


const style1 = {
  textAlign: "center",
  color: "#fff",
  backgroundColor: "#e9e9e9",
  height: "100vh",
  overflow: "auto",
};
import { MenuOutlined } from "@ant-design/icons";
// const style2 = {
//   textAlign: "center",
//   color: "#fff",
//   backgroundColor: "#7dbcea",
// };

function App() {
  const [open, setOpen] = useState(false);
  const [pageContent, setPageContent] = useState(pages[0].content);
  const showDrawer = () => {
    setOpen(true);
  };
  const onClose = () => {
    setOpen(false);
  };
  return (
    <>
      <Layout>
        <Header
          className="Drawer"
          style={{
            backgroundColor: "white",
            display: "flex",
            alignItems: "flex-end",
          }}
          width={10}
        >
          <Button onClick={showDrawer} style={{ border: "none" }}>
            <MenuOutlined />
          </Button>
        </Header>

        <Drawer
          title="Documentation"
          onClose={onClose}
          open={open}
          placement="left"
        >
          {pages.map((page, index) => (
            <button
              key={index}
              onClick={() => {
                setPageContent(page.content);
                setOpen(false);
              }}
            >
              {page.name}
            </button>
          ))}
        </Drawer>
        <Content style={{ backgroundColor: "white" }} className="Content">
          {pageContent}
          <Image preview={false} src={imgurl3} />
        </Content>
      </Layout>
    </>
  );
}

export default App;
