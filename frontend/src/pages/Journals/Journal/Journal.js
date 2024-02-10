import React from "react";
import { useParams } from "react-router-dom";

const Journal = () => {
  const { date } = useParams();

  return <main className="Journal">Journal: {date}</main>;
};

export default Journal;
