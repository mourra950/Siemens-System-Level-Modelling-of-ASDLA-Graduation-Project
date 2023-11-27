import { useState, CSSProperties } from "react";
import "./App.css";
import { Content, Header } from "antd/es/layout/layout";
import Sider from "antd/es/layout/Sider";
import { Layout } from "antd";
import React from "react";

const style1 = {
  textAlign: "center",
  color: "#fff",
  backgroundColor: "#7dbcea",
  height: "100vh",
  overflow: "auto",
};
const style2 = {
  textAlign: "center",
  color: "#fff",
  backgroundColor: "#7dbcea",
};
function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <Layout>
        <Sider 
        breakpoint="lg"
        style={style1}>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
          <p>Ahmed</p>
        </Sider>
        <Content>
          Hello
        </Content>
      </Layout>
    </>
  );
}

export default App;
