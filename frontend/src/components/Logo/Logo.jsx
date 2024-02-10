import React from "react";

import RocketPalLogo from "../../assets/logos/RocketPalLogoV2.png";

const Logo = () => {
  return (
    <div className="RocketPalLogo">
      <img
        src={RocketPalLogo}
        alt="Rocket Pal Logo"
        width={50}
        height={50}
        style={{ borderRadius: "50%", border: "3px solid #09002a" }}
      />
    </div>
  );
};

export default Logo;
