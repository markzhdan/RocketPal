import React from "react";
import "./Loading.css";
import { ColorRing } from "react-loader-spinner";

const Loading = () => {
  return (
    <div className="Loading">
      <ColorRing
        visible={true}
        height="80"
        width="80"
        ariaLabel="color-ring-loading"
        wrapperStyle={{}}
        wrapperClass="color-ring-wrapper"
        colors={["#d30011", "#d30011", "#d30011", "#d30011", "#d30011"]}
      />
      <h3>Data is loading... wait a moment please!</h3>
    </div>
  );
};

export default Loading;
