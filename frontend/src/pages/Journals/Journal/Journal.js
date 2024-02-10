import React, { useState } from "react";
import { useParams } from "react-router-dom";
import { Textarea } from "@nextui-org/react";
import "./Journal.css";
import { Button } from "@nextui-org/react";

const Journal = ({ content }) => {
  const { date } = useParams();
  const [journal, setJournal] = useState({
    journal_id: 1,
    date: "2024-02-10",
    content:
      "Today was a productive day. I woke up early and went for a run in the park. The weather was chilly, but refreshing. Afterwards, I spent the morning working on my project, making significant progress. In the afternoon, I met up with a friend for coffee and had a great conversation. Overall, feeling accomplished and content.",
  });

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
            defaultValue={content}
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
