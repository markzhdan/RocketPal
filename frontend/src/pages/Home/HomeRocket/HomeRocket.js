import React from "react";
import "./HomeRocket.css";

import earth from "../../../assets/planets/earth.gif";
import jupiter from "../../../assets/planets/jupiter.png";
import saturn from "../../../assets/planets/saturn-animated.gif";

// import rocket from "../../../assets/rocket2.gif";

import { Progress } from "@nextui-org/react";

const planets = [
  { name: "Earth", image: earth, size: 200 },
  { name: "Jupiter", image: jupiter, size: 100 },
  { name: "Saturn", image: saturn, size: 200 },
];

const HomeRocket = () => {
  return (
    <main className="HomeRocket">
      <div className="Tracks">
        <section className="RocketTrack">
          {/* <img src={rocket} alt="Rocketship Animation" width={150} /> */}
        </section>
        <section className="Planets">
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
          label="Lose weight"
          value={65}
        />
      </div>
    </main>
  );
};

export default HomeRocket;
