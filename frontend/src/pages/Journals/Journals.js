import React, { useState, useEffect } from "react";
import "./Journals.css";
import { Checkbox } from "@nextui-org/react";
import { FaBlackTie, FaTrashCan } from "react-icons/fa6";
import { FaTrash } from "react-icons/fa";
import { Input } from "@nextui-org/react";
import { IoIosAddCircle } from "react-icons/io";
import { useHistory } from "react-router-dom";
import { Link } from "react-router-dom";
import { FaPencilAlt } from "react-icons/fa";

const Journals = () => {
  const [selectedEntryContent, setSelectedEntryContent] = useState("");
  const [entry, setEntries] = useState([
    {
      journal_id: "1",
      date: "2024-02-10",
      content:
        "Today was a productive day. I woke up early and went for a run in the park. The weather was chilly, but refreshing. Afterwards, I spent the morning working on my project, making significant progress. In the afternoon, I met up with a friend for coffee and had a great conversation. Overall, feeling accomplished and content.",
    },
    {
      journal_id: "2",
      date: "2024-02-09",
      content:
        "Spent the day indoors due to heavy rain. Despite the gloomy weather, I managed to catch up on some reading and watched a few episodes of my favorite TV show. Feeling relaxed and rejuvenated.",
    },
    {
      journal_id: "3",
      date: "2024-02-08",
      content:
        "Attended a workshop on mindfulness and meditation today. It was enlightening to learn new techniques for managing stress and improving focus. I'm determined to incorporate these practices into my daily routine.",
    },
    {
      journal_id: "4",
      date: "2024-02-10",
      content:
        "Today was a productive day. I woke up early and went for a run in the park. The weather was chilly, but refreshing. Afterwards, I spent the morning working on my project, making significant progress. In the afternoon, I met up with a friend for coffee and had a great conversation. Overall, feeling accomplished and content.",
    },
    {
      journal_id: "5",
      date: "2024-02-09",
      content:
        "Spent the day indoors due to heavy rain. Despite the gloomy weather, I managed to catch up on some reading and watched a few episodes of my favorite TV show. Feeling relaxed and rejuvenated.",
    },
    {
      journal_id: "6",
      date: "2024-02-08",
      content:
        "Attended a workshop on mindfulness and meditation today. It was enlightening to learn new techniques for managing stress and improving focus. I'm determined to incorporate these practices into my daily routine.",
    },
  ]);

  const handleEdit = (content) => {
    setSelectedEntryContent(content);
  };

  const handleAddEntry = () => {
    const newEntry = {
      journal_id: parseInt(entry.length + 1),
      date: new Date().toISOString().slice(0, 10),
      content: "Click to pen to edit...", // You can customize this
    };
    setEntries([...entry, newEntry]);
  };

  const handleDelete = (entryId) => {
    setEntries((prevEntries) =>
      prevEntries.filter((entry) => entry.journal_id !== entryId)
    );
  };

  return (
    <div className="Container">
      <main className="Journals">
        <div className="Journal-Header">
          <h1>Self-Reflection Journals</h1>
        </div>

        <section className="Entries-Container">
          <div className="Add-Container">
            <h2>Add a Journal!</h2>
            <IoIosAddCircle
              style={{ fontSize: "80px" }}
              onClick={handleAddEntry}
            />
          </div>
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
                  <FaTrash
                    onClick={() => handleDelete(entry.journal_id)}
                    role="button"
                    tabIndex="0"
                  />
                </div>
              </div>
              <div className="Content">
                <p>{entry.content.substring(0, 250) + "..."}</p>
              </div>
            </div>
          ))}
        </section>
      </main>
    </div>
  );
};

export default Journals;
