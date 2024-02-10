import React from "react";
import "./Frontpage.css";
import { Button, ButtonGroup } from "@nextui-org/react";
import rocket from "../../assets/rocket4.gif";
import { Link } from "react-router-dom";

const Frontpage = () => {
  return (
    <main className="Frontpage">
      <img src={rocket} alt="Rocketship Animation" width={800} />
      <div className="container">
        <p className="typed">Where Your Goals Will Reach the Stars...</p>
      </div>
      <div className="button-container">
        <Link to={`/Login`} className="Sign-Up">
          <Button color="primary" size="lg">
            Get Started!
          </Button>
        </Link>
      </div>
    </main>
  );
};

export default Frontpage;
