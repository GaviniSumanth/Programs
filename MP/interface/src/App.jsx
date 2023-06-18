import { Tab } from "@headlessui/react";
import "./style.css";
import Card from "./components/Card";
function App() {
  return (
    <>
      <Landing />
      <Tab.Group>
        <Tab.List className="tabs">
          <Tab className="tab">Steam</Tab>
          <Tab className="tab">Human Resources</Tab>
          <Tab className="tab">Student Adaptability</Tab>
        </Tab.List>
        <Tab.Panels className="panels">
          <Tab.Panel className="panel"></Tab.Panel>
          <Tab.Panel className="panel"></Tab.Panel>
          <Tab.Panel className="panel">
            <Card
              src="https://images.unsplash.com/photo-1684151941972-2d456c0e2b3b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
              description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet."
              url="Form"
            />
            <Card
              src="https://images.unsplash.com/photo-1684151941972-2d456c0e2b3b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
              description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet."
              url="https://www.google.com"
            />
            <Card
              src="https://images.unsplash.com/photo-1684151941972-2d456c0e2b3b?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=2070&q=80"
              description="Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet.Lorem ipsum dolor sit amet consectetur, adipisicing elit. Consequatur dolorem optio iure voluptate dolore culpa iste, suscipit provident adipisci, tempora reprehenderit voluptas dolor in facilis quaerat illo animi deleniti eveniet."
              url="https://www.google.com"
            />
          </Tab.Panel>
        </Tab.Panels>
      </Tab.Group>
    </>
  );
}

function Landing() {
  return (
    <div id="Landing">
      <div className="ripple-background">
        <div className="circle xxlarge"></div>
        <div className="circle xlarge"></div>
        <div className="circle large"></div>
        <div className="circle medium"></div>
        <div className="circle small"></div>
        <h1 id="Title">Mini</h1>
        <h1 id="Title">Project</h1>
        <p id="Description">
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Esse aliquid
          asperiores natus? Quaerat doloribus quas odio? Tempore corrupti error
          debitis nisi, laborum illum tempora animi aliquid eos consequuntur
          dignissimos numquam? Lorem, ipsum dolor sit amet consectetur
          adipisicing elit. Quos autem odio consequuntur repellat asperiores
          praesentium magnam sit fugiat iste, qui dolorem quis blanditiis
          molestias dicta aut veniam enim totam officia!
        </p>
      </div>
    </div>
  );
}

export default App;
