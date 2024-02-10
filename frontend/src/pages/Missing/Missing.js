import React from "react";
import "./Missing.css"; // Import CSS file for styling

const Missing = () => {
  return (
    <main className="Missing">
      <div className="container">
        <h1>404 - Page Not Found</h1>
        <div className="container">
          <p className="typed">We're sorry, the page you are looking for might have been removed, had
          its name changed, or is temporarily unavailable.</p>
        </div>
      </div>
    </main>
  );
};

export default Missing;
