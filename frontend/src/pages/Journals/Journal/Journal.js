import React from "react";
import { useParams } from "react-router-dom";

const Journal = () => {
  const { matchId } = useParams();

  return <div>Journal: {matchId}</div>;
};

export default Journal;
