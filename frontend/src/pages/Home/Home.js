import React from "react";
import "./Home.css";

import HomeGoals from "./HomeGoals/HomeGoals";
import HomeRocket from "./HomeRocket/HomeRocket";
import HomeTalks from "./HomeTalks/HomeTalks";

const Home = () => {
  return (
    <main className="Home">
      <HomeGoals />
      <HomeRocket />
      <HomeTalks />
    </main>
  );
};

export default Home;
