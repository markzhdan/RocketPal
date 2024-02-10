import React from "react";
import "./HomeTalks.css";
import { useState } from "react";
import { Checkbox } from "@nextui-org/react";
import { FaBlackTie, FaTrashCan } from "react-icons/fa6";
import { FaTrash } from "react-icons/fa";
import { Input } from "@nextui-org/react";
import { IoIosAddCircle } from "react-icons/io";
import { useHistory } from "react-router-dom";
import { Link } from "react-router-dom";
import { FaPencilAlt } from "react-icons/fa";
import { Button } from "@nextui-org/react";

const HomeTalks = () => {
  const [entry, setEntries] = useState([
    {
      journal_id: "1",
      date: "2024-02-10",
      content:
        "Today was a productive day. I like monkeys. The weather was chilly, but refreshing. Afterwards, I spent the morning working on my project, making significant progress. In the afternoon, I met up with a friend for coffee and had a great conversation. Overall, feeling accomplished and content.",
    },
  ]);

  return (
    <main className="HomeTalks">
      <div className="Main-Container">
        <h1>Most Recent Journal</h1>
        <section className="Journal-Contain">
          <div className="Recent-Journal">
            {entry.map((entry) => (
              <div
                className="Journal-Entry"
                key={entry.journal_id}
                // onClick={() => redirectToJournalPage(entry.entry_id)}
              >
                <div className="Journal-Headers">
                  <h2>{entry.date}</h2>
                  <div className="icons">
                    <Link
                      to={`/journal/${entry.journal_id}`}
                      key={entry.journal_id}
                      className="Edit-Journal"
                    >
                      <FaPencilAlt />
                    </Link>
                  </div>
                </div>
                <div className="Content">
                  <p>{entry.content.substring(0, 350) + "..."}</p>
                </div>
              </div>
            ))}
          </div>
        </section>
        <div className="x`button">
          <Button color="default" size="lg" width="100px;">
            Button
          </Button>
        </div>
      </div>
    </main>
  );
};

export default HomeTalks;
