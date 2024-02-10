import React, { useState } from "react";
import "./Home.css";

import HomeGoals from "./HomeGoals/HomeGoals";
import HomeRocket from "./HomeRocket/HomeRocket";
import HomeTalks from "./HomeTalks/HomeTalks";

const Home = () => {
  const [points, setPoints] = useState(0);
  const [totalPoints, setTotalPoints] = useState(0);

  return (
    <main className="Home">
      <HomeGoals
        points={points}
        setPoints={setPoints}
        setTotalPoints={setTotalPoints}
      />
      <HomeRocket points={points} totalPoints={totalPoints} />
      <HomeTalks />
    </main>
  );
};

export default Home;
