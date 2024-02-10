import React from "react";
import "./HomeTalks.css";
import { useState } from "react";
import { Link } from "react-router-dom";
import { FaPencilAlt } from "react-icons/fa";
import { Button } from "@nextui-org/react";

const HomeTalks = () => {
  const [entry, setEntries] = useState([
    {
      journal_id: "2",
      date: "2024-02-10",
      content:
        "Today I felt a little down. I did nothing but play videogames all day and not a single bit of work. I didn't anything else besides junk food and soda today.  I have so many assignments due but I can't seem to get the motivation to do them. I feel like I am falling behind and losing myself. I want to start getting back into shape by working out and fixing my diet. I also need to lock in and get all my school work sorted out, I want to turn my life around.",
    },
  ]);

  return (
    <main className="HomeTalks">
      <div className="Main-Container">
        <h1>Recent Journals</h1>
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
          <Link
            to={`/journals`}
            key={entry.journal_id}
            className="Edit-Journal"
          >
            <Button color="default" size="lg" width="100px;">
              See all journals
            </Button>
          </Link>
        </div>
      </div>
    </main>
  );
};

export default HomeTalks;
