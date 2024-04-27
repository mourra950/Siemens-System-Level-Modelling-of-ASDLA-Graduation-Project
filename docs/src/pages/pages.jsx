/* eslint-disable no-unused-vars */
import page1 from "./page1";
import page2 from "./page2";
import features from "./features";
import team from "./team";
import project from "./project"

const pages = [
  {
    name: "Know the Team",
    content: team(),
  },
  {
    name: "Team",
    content: team(),
  },
  {
    name: "Who are We",
    content: page1(),
  },
  {
    name: "Features",
    content: features(),
  },{
    name: "Project",
    content: project(),
  },
];
export default pages;
