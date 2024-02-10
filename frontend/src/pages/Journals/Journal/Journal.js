import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { Textarea } from "@nextui-org/react";
import "./Journal.css";
import { Button } from "@nextui-org/react";
import { fetchWithToken } from "../../../features/api/api";

const Journal = ({ content }) => {
  const { date } = useParams();
  const [journal, setJournal] = useState({});

  function findJournalById(journals, journalId) {
    return journals.find((journal) => journal.journal_id === journalId);
  }

  const fetchEntries = async () => {
    try {
      const data = await fetchWithToken("/get_journals");
      const jsonData = JSON.parse(data);
      const journal = findJournalById(jsonData.journals, date);

      setJournal(journal);
      console.log("journal: ", journal);
    } catch (error) {
      console.error("Failed to fetch goals:", error);
    }
  };

  useEffect(() => {
    fetchEntries();
  }, []);

  return (
    <section className="Journal-Container">
      <div className="Journal">
        <h1 style={{ textAlign: "center" }}>Journal Page</h1>
        <div className="ContentBox">
          <Textarea
            key="faded"
            variant="faded"
            labelPlacement="outside"
            placeholder="Enter your description"
            className="col-span-12 md:col-span-6 mb-6 md:mb-0"
            size="lg"
            radius="md"
            defaultValue={journal.content}
            value={journal.content}
          />
        </div>

        <div className="Save-Container">
          <Button color="default">Save</Button>
          <Button color="default">Discard</Button>
        </div>
      </div>
    </section>
  );
};

export default Journal;
