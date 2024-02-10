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
          name: "Drink Waters",
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
          name: "Drink Water2",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Go To The Gym3",
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
          name: "Drink Water6",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Go To The Gym7",
          completed: false,
          pointsValue: 5,
        },
        {
          name: "Drink Water09",
          completed: false,
          pointsValue: 5,
        },
      ],
    },
  ]);

  const handleTaskClick = (goalName, taskName) => {
    const updatedGoals = goals.map((goal) => {
      if (goal.name === goalName) {
        const updatedTasks = goal.tasks.map((task) => {
          if (task.name === taskName) {
            return { ...task, completed: !task.completed };
          }
          return task;
        });

        // Optionally, update the goal's completed status based on tasks
        const isGoalCompleted = updatedTasks.every((task) => task.completed);

        return { ...goal, tasks: updatedTasks, completed: isGoalCompleted };
      }
      return goal;
    });

    setGoals(updatedGoals);
  };

  console.log(goals);

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
                        <Checkbox
                          color="success"
                          isSelected={task.completed}
                          onChange={() => handleTaskClick(goal.name, task.name)}
                          lineThrough={task.completed}
                        >
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
