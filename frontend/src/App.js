import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Frontpage from "./pages/Frontpage/Frontpage";
import RocketNavbar from "./components/navbar/Navbar";

import Home from "./pages/Home/Home";
import Profile from "./pages/Profile/Profile";
import Journals from "./pages/Journals/Journals";
import Journal from "./pages/Journals/Journal/Journal";
import Therapist from "./pages/Therapist/Therapist";

import Missing from "./pages/Missing/Missing";

function App() {
  return (
    <Router>
      <div className="App">
        <RocketNavbar />
        <Routes>
          <Route exact path="/" element={<Frontpage />} />

          <Route path="/home" element={<Home />} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/journals" element={<Journals />} />
          <Route path="/journal/:date" element={<Journal />} />
          <Route path="/therapist" element={<Therapist />} />

          <Route path="*" element={<Missing />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
