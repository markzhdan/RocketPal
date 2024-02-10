import React, { useState } from "react";
import "./Journals.css";

const Journals = () => {
  return (
    <main className="Journals">
      <div className="journal-container">
        <JournalContainer
          title="Container 1"
          includeHeading={true}
          maxEntries={3}
        />
        <JournalContainer
          title="Container 2"
          includeHeading={false}
          maxEntries={3}
        />
        <JournalContainer
          title="Container 3"
          includeHeading={false}
          maxEntries={3}
        />
      </div>
    </main>
  );
};

function JournalContainer({ title, includeHeading }) {
  const [entries, setEntries] = useState([]);
  const [currentContainer, setCurrentContainer] = useState(0);

  const addEntry = (entry) => {
    setEntries([...entries, entry]);
    setCurrentContainer(currentContainer + 1);
  };

  return (
    <div className="journal">
      {includeHeading && <h1>Journals</h1>}
      <div className="journal-content">
        <div className="sub-entries">
          {currentContainer === 0 && <SubContainer addEntry={addEntry} />}
          {currentContainer > 0 && <SubContainer addEntry={addEntry} />}
        </div>
        <div className="entries">
          {entries.map((entry, index) => (
            <JournalEntry
              key={index}
              date={entry.date}
              content={entry.content}
            />
          ))}
        </div>
      </div>
    </div>
  );
}

function SubContainer({ addEntry }) {
  const [date, setDate] = useState("");
  const [content, setContent] = useState("");
  const [isInputOpen, setIsInputOpen] = useState(false); // State to track whether input section is open

  const toggleInput = () => {
    setIsInputOpen(!isInputOpen);
  };

  const addJournalEntry = () => {
    if (date && content) {
      addEntry({ date, content });
      setDate("");
      setContent("");
      setIsInputOpen(false); // Close input section after adding entry
    }
  };

  return (
    <div className="sub-container">
      {isInputOpen ? (
        <div className="journal-input">
          <input
            type="text"
            placeholder="Date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
          <textarea
            placeholder="Write your journal entry here..."
            value={content}
            onChange={(e) => setContent(e.target.value)}
          ></textarea>
          <button onClick={addJournalEntry}>Add Entry</button>
        </div>
      ) : (
        <div className="plus-sign" onClick={toggleInput}>
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 24 24"
            width="24"
            height="24"
          >
            <path fill="none" d="M0 0h24v24H0z" />
            <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zM11 7h2v6h6v2h-6v6h-2v-6H5v-2h6z" />
          </svg>
        </div>
      )}
    </div>
  );
}

function JournalEntry({ date, content }) {
  return (
    <div className="entry">
      <div className="entry-header">Date: {date}</div>
      <div className="entry-content">Content: {content}</div>
    </div>
  );
}

export default Journals;
