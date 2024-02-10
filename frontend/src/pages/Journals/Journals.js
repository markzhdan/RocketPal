import React, { useState, useEffect } from "react";
import "./Journals.css";
import { FaTrash } from "react-icons/fa";
import { Input } from "@nextui-org/react";
import { IoIosAddCircle } from "react-icons/io";
import { useHistory } from "react-router-dom";
import { Link } from "react-router-dom";
import { FaPencilAlt } from "react-icons/fa";
import { fetchWithToken } from "../../features/api/api";
import { useNavigate } from "react-router-dom";

const Journals = () => {
  const [selectedEntryContent, setSelectedEntryContent] = useState("");
  const [entry, setEntries] = useState([]);
  const navigate = useNavigate();

  const fetchEntries = async () => {
    try {
      const data = await fetchWithToken("/get_journals");
      const jsonData = JSON.parse(data);
      setEntries(jsonData.journals);
    } catch (error) {
      console.error("Failed to fetch goals:", error);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  const handleEdit = (content) => {
    setSelectedEntryContent(content);
  };

  const handleAddEntry = async () => {
    const newEntry = {
      journal_id: "" + parseInt(entry.length + 1),
      date: new Date().toISOString().slice(0, 10),
      content: "Click to pen to edit...",
    };

    try {
      await fetchWithToken("/add_journal", "POST", newEntry);
    } catch (error) {
      console.error("Error modifying new goal:", error);
    }

    navigate(`/journal/${newEntry.journal_id}`);
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
          {entry && entry.length !== 0
            ? entry.map((entry) => (
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
              ))
            : null}
        </section>
      </main>
    </div>
  );
};

export default Journals;
