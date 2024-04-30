/* eslint-disable no-unused-vars */
import page1 from "./page1";
import features from "./features";
import team from "./team";
import project from "./project";
import technologies from "./Technologies";
import Pytorch from "./pytorch.jsx";

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
];
export default pages;
