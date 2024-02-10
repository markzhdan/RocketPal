import React from "react";
import "./HomeRocket.css";

import earth from "../../../assets/planets/earth.gif";
import sun from "../../../assets/planets/sun.gif";
import venus from "../../../assets/planets/venus.gif";
import saturn from "../../../assets/planets/saturn-animated.gif";

import rocket from "../../../assets/rocket4.gif";

import { Progress } from "@nextui-org/react";

const planets = [
  { name: "Sun", image: sun, size: 200 },
  { name: "Earth", image: earth, size: 200 },
  { name: "Venus", image: venus, size: 200 },
  { name: "Saturn", image: saturn, size: 200 },
];

const HomeRocket = ({ points, totalPoints }) => {
  console.log(
    "points: ",
    (points / (totalPoints == 0 ? 1 : totalPoints)) * 100
  );
  console.log(points);
  console.log(totalPoints);
  return (
    <main className="HomeRocket">
      <div className="Tracks">
        <section className="RocketTrack">
          <img src={rocket} alt="Rocketship Animation" width={500} />
        </section>
        <section className="Planets">
          <div className="DottedPath"></div>
          {planets.map((planet) => (
            <img
              src={planet.image}
              alt={`${planet.name} Planet`}
              key={planet.name}
              width={planet.size}
            />
          ))}
        </section>
      </div>
      <div className="ProgressBar">
        <Progress
          size="sm"
          radius="sm"
          classNames={{
            base: "max-w-md",
            track: "drop-shadow-md border border-default h-5",
            indicator: "bg-gradient-to-r from-pink-500 to-yellow-500 ",
            label: "tracking-wider font-medium text-white-500",
            value: "text-foreground/60 ",
          }}
          label="Reach Home Base"
          value={(points / (totalPoints == 0 ? 1 : totalPoints)) * 100}
        />
      </div>
    </main>
  );
};

export default HomeRocket;
