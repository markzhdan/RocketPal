import "./App.css";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  useLocation,
} from "react-router-dom";

import Frontpage from "./pages/Frontpage/Frontpage";
import RocketNavbar from "./components/navbar/Navbar";

import Home from "./pages/Home/Home";
import Login from "./pages/Login/Login";
import Profile from "./pages/Profile/Profile";
import Journals from "./pages/Journals/Journals";
import Journal from "./pages/Journals/Journal/Journal";
import Therapist from "./pages/Therapist/Therapist";

import Missing from "./pages/Missing/Missing";
import ProtectedRoute from "./features/auth/ProtectedRoute";
import { UserProvider } from "./features/auth/UserContext";

function App() {
  const ConditionalNavbar = () => {
    const location = useLocation();
    const hideNavbarPaths = ["/login", "/anotherPath"];
    if (hideNavbarPaths.includes(location.pathname)) {
      return null;
    }
    return <RocketNavbar />;
  };

  const protect = (component) => {
    return <ProtectedRoute>{component}</ProtectedRoute>;
  };

  return (
    <UserProvider>
      <Router>
        <div className="App">
          <ConditionalNavbar />

          <Routes>
            <Route exact path="/" element={<Frontpage />} />

            <Route path="/login" element={<Login />} />

            <Route path="/home" element={protect(<Home />)} />
            <Route path="/profile" element={protect(<Profile />)} />
            <Route path="/journals" element={protect(<Journals />)} />
            <Route path="/journal/:date" element={protect(<Journal />)} />
            <Route path="/therapist" element={protect(<Therapist />)} />

            <Route path="*" element={<Missing />} />
          </Routes>
        </div>
      </Router>
    </UserProvider>
  );
}

export default App;
