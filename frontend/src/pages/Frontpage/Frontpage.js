import React from "react";
import "./Frontpage.css";

import rocket from "../../assets/rocket4.gif";

const Frontpage = () => {
  return (
    <main className="Frontpage">
      <img src={rocket} alt="Rocketship Animation" width={800} />
    </main>
  );
};

export default Frontpage;
