/* eslint-disable no-unused-vars */
import page1 from "./page1";
import features from "./features";
import team from "./team";
import project from "./project";
import technologies from "./Technologies/Technologies.jsx";
import Pytorch from "./Technologies/pytorch.jsx";
import Jinja from "./Technologies/jinja.jsx";
import CMake from "./Technologies/cmake.jsx";
import SystemC from "./Technologies/systemc.jsx";
import TensorBoard from "./Technologies/tensorboard.jsx";
import GitHub from "./Technologies/github.jsx";

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
