import React, { useState, useEffect } from "react";
import "./HomeGoals.css";
import { Checkbox } from "@nextui-org/react";

const HomeGoals = () => {
  const [goals, setGoals] = useState([
    {
      name: "Stay Healthy",
      completed: false,
      pointsValue: 20,
      icon: "healthIcon",
      tasks: [
        {
          name: "Drink Water",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Go To The Gym",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Drink Water",
          completed: false,
          pointsValue: 5,
        },
      ],
    },
    {
      name: "Be good at running",
      completed: false,
      pointsValue: 20,
      icon: "healthIcon",
      tasks: [
        {
          name: "Drink Water",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Go To The Gym",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Drink Watssssssss ssssssssssssser",
          completed: false,
          pointsValue: 5,
        },
      ],
    },
    {
      name: "Be good at Fortnite",
      completed: false,
      pointsValue: 20,
      icon: "healthIcon",
      tasks: [
        {
          name: "Drink Water",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Go To The Gym",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Drink Water",
          completed: false,
          pointsValue: 5,
        },
      ],
    },
  ]);

  return (
    <>
      {goals.length == 0 ? (
        <main className="HomeGoals">
          <h1>You completed all your goals, add button</h1>
        </main>
      ) : (
        <main className="HomeGoals">
          <h1 className="Head">Goals</h1>
          <section className="Goals">
            <div className="goal-container">
              {goals.map((goal) => (
                <div className="Goal" key={goal.name}>
                  <h2>{goal.name}</h2>

                  <div className="Tasks">
                    {goal.tasks.map((task) => (
                      <div className="Task" key={task.name}>
                        <Checkbox defaultSelected color="success">
                          {task.name}
                        </Checkbox>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>
        </main>
      )}
    </>
  );
};

export default HomeGoals;
