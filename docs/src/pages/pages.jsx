/* eslint-disable no-unused-vars */
import page1 from "./page1";
import page2 from "./page2";
import features from "./features";
import team from "./team";



const pages = [
  {
    name: "Who are We",
    content: page1()
  },{
    name: "Features",
    content: features() 
  },{
    name: "Team",
    content: team() 
  },{
    name: "page2",
    content: page2() 
  },{
    name: "page2",
    content: page2() 
  }
];
export default pages;