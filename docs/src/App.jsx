import { useState } from "react";
import "./App.css";
import { Content } from "antd/es/layout/layout";
import Sider from "antd/es/layout/Sider";
import { Layout } from "antd";
import pages from "./pages/pages";
import { Drawer, Button } from "antd";
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
  const [brokenpage, setbrokenpage] = useState(true);
  const showDrawer = () => {
    setOpen(true);
  };
  const onClose = () => {
    setOpen(false);
  };
  return (
    <>
      <Layout>
        {brokenpage ? (
          <>
            <Sider
              className="Drawer"
              style={{
                backgroundColor: "white",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
              }}
              breakpoint="lg"
              width={70}
              onBreakpoint={(b) => {
                setbrokenpage(b);
                console.log(b);
              }}
            >
              <Button onClick={showDrawer} style={{ border: "none" }}>
                <MenuOutlined />
              </Button>
            </Sider>
          </>
        ) : (
          <Sider
            breakpoint="lg"
            style={style1}
            onBreakpoint={(b) => {
              setbrokenpage(b);
              console.log(b);
            }}
          >
            {pages.map((page, index) => (
              <button key={index} onClick={() => setPageContent(page.content)}>
                {page.name}
              </button>
            ))}
          </Sider>
        )}
        <Drawer
          title="Documentation"
          onClose={onClose}
          open={open}
          placement="left"
        >
          {pages.map((page, index) => (
            <button key={index} onClick={() => setPageContent(page.content)}>
              {page.name}
            </button>
          ))}
        </Drawer>
        <Content style={{ backgroundColor: "white" }} className="Content">
          {pageContent}
        </Content>
      </Layout>
    </>
  );
}

export default App;
