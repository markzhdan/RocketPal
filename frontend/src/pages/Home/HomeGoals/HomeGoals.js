import React, { useState, useEffect } from "react";
import "./HomeGoals.css";
import { Checkbox } from "@nextui-org/react";
import { FaTrash } from "react-icons/fa";
import { Input } from "@nextui-org/react";
import { IoIosAddCircle } from "react-icons/io";

import { fetchWithToken } from "../../../features/api/api";

const HomeGoals = () => {
  const [goals, setGoals] = useState([]);

  const fetchGoals = async () => {
    try {
      const data = await fetchWithToken("/goals");
      const jsonData = JSON.parse(data);
      setGoals(jsonData.goals);
    } catch (error) {
      console.error("Failed to fetch goals:", error);
    }
  };

  useEffect(() => {
    fetchGoals();
  }, []);

  const [goalName, setGoalName] = useState("");

  const handleChange = (event) => {
    setGoalName(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    if (goalName.trim().length > 0) {
      try {
        await fetchWithToken("/add_goal", "POST", {
          name: goalName,
        });
        setGoalName("");
        fetchGoals();
      } catch (error) {
        console.error("Error submitting new goal:", error);
      }
    }
  };

  const handleDelete = async (goalId) => {
    console.log("goal id: ", goalId);
    try {
      await fetchWithToken("/remove_goal", "POST", {
        goal_id: goalId,
      });

      fetchGoals();
    } catch (error) {
      console.error("Error submitting new goal:", error);
    }
  };

  const handleTaskClick = (goalName, taskName) => {
    const updatedGoals = goals.map((goal) => {
      if (goal.name === goalName) {
        const updatedTasks = goal.tasks.map((task) => {
          if (task.name === taskName) {
            return { ...task, completed: !task.completed };
          }
          return task;
        });

        const isGoalCompleted = updatedTasks.every((task) => task.completed);

        return { ...goal, tasks: updatedTasks, completed: isGoalCompleted };
      }
      return goal;
    });

    setGoals(updatedGoals);
  };

  return (
    <main className="HomeGoals">
      <h1 className="Head"> Your Goals</h1>
      <section className="Goals">
        <div className="goal-container">
          {goals.map((goal) => (
            <div className="Goal" key={goal.goal_id}>
              <div className="Goal-Heading">
                <h2>{goal.name}</h2>
                <FaTrash
                  onClick={() => handleDelete(goal.goal_id)}
                  role="button"
                  tabIndex="0"
                />
              </div>
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

          <div
            className="Add-Container"
            style={{ visibility: goals.length >= 3 ? "hidden" : "visible" }}
          >
            <Input
              type="Goals"
              label="Add Goal"
              placeholder="Enter a Goal"
              value={goalName}
              classNames={{
                input: ["placeholder:text-black"],
              }}
              onChange={handleChange}
            />
            <IoIosAddCircle
              style={{ fontSize: "40px" }}
              onClick={handleSubmit}
            />
          </div>
        </div>
      </section>
    </main>
  );
};

export default HomeGoals;
