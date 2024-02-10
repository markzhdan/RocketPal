import React, { useState, useEffect } from "react";
import "./HomeGoals.css";
import { Checkbox } from "@nextui-org/react";
import { FaTrash } from "react-icons/fa";
import { Input } from "@nextui-org/react";
import { IoIosAddCircle } from "react-icons/io";

import { fetchWithToken } from "../../../features/api/api";

const HomeGoals = ({ points, setPoints, setTotalPoints }) => {
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

  useEffect(() => {
    const totalPointsValue = goals.reduce((total, goal) => {
      const goalPoints = goal.tasks.reduce(
        (sum, task) => sum + task.pointsValue,
        0
      );
      return total + goalPoints;
    }, 1);

    const totalPointsValueCompleted = goals.reduce((total, goal) => {
      const goalPoints = goal.tasks.reduce((sum, task) => {
        if (task.completed) {
          return sum + task.pointsValue;
        }
        return sum;
      }, 0);
      return total + goalPoints;
    }, 0);

    setPoints(totalPointsValueCompleted);

    setTotalPoints(totalPointsValue);
  });

  console.log("goals: ", goals);

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

  const handleDelete = async (goal) => {
    console.log("goal id: ", goal);

    try {
      await fetchWithToken("/remove_goal", "POST", {
        goal_id: goal.goal_id,
      });

      const totalPointsValueCompleted = goals.reduce((total, goal) => {
        const goalPoints = goal.tasks.reduce((sum, task) => {
          if (task.completed) {
            return sum + task.pointsValue;
          }
          return sum;
        }, 0);
        return total + goalPoints;
      }, 0);

      setPoints(points - totalPointsValueCompleted);

      fetchGoals();
    } catch (error) {
      console.error("Error submitting new goal:", error);
    }
  };

  function toggleTaskCompletion(goal, taskNameToToggle) {
    const updatedTasks = goal.tasks.map((task) => {
      if (task.name === taskNameToToggle) {
        return { ...task, completed: !task.completed };
      }
      return task;
    });

    return {
      ...goal,
      tasks: updatedTasks,
    };
  }

  const handleTaskClick = async (goal, task) => {
    const updatedGoal = toggleTaskCompletion(goal, task.name);
    delete updatedGoal["_id"];

    try {
      await fetchWithToken("/modify_goal", "POST", updatedGoal);
      fetchGoals();
    } catch (error) {
      console.error("Error modifying new goal:", error);
    }

    if (task.completed) {
      setPoints(points - task.pointsValue);
    } else {
      setPoints(points + task.pointsValue);
    }
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
                  onClick={() => handleDelete(goal)}
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
                      onChange={() => handleTaskClick(goal, task)}
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
