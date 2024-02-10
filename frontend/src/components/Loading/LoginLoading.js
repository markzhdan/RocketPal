import React from "react";
import "./LoginLoading.css";
import { ColorRing } from "react-loader-spinner";

import Logo from "../Logo/Logo";

const LoginLoading = () => {
  return (
    <div className="LoginLoading">
      <div className="LogingLoadingContainer">
        <Logo />
        <ColorRing
          visible={true}
          height="80"
          width="80"
          ariaLabel="color-ring-loading"
          wrapperStyle={{}}
          wrapperClass="color-ring-wrapper"
          colors={["#d30011", "#d30011", "#d30011", "#d30011", "#d30011"]}
        />
        <h3>Logging you in... hold tight</h3>
      </div>
    </div>
  );
};

export default LoginLoading;
