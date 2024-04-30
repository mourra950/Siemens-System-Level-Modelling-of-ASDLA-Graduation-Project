/* eslint-disable no-unused-vars */
import page1 from "./page1";
import features from "./features";
import team from "./team";
import project from "./project";
import technologies from "./Technologies";
import Pytorch from "./pytorch.jsx";
import Jinja from "./jinja.jsx";
import CMake from "./CMake.jsx";
import SystemC from "./systemc.jsx";
import TensorBoard from "./tensorboard.jsx";
import GitHub from "./github.jsx";

const pages = [
  {
    name: "Project",
    content: project(),
  },
  {
    name: "Features",
    content: features(),
  },
  {
    name: "Technologies",
    content: technologies(),
  },
  {
    name: "Know the Team",
    content: team(),
  },
  {
    name: "Pytorch",
    content: Pytorch(),
  },
  {
    name: "Jinja",
    content: Jinja(),
  },
  {
    name: "CMake",
    content: CMake(),
  },
  {
    name: "SystemC",
    content: SystemC(),
  },
  {
    name: "TensorBoard",
    content: TensorBoard(),
  },
  {
    name: "GitHub",
    content: GitHub(),
  },

];
export default pages;
