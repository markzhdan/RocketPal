import React, { useEffect, useState } from "react";
import { Input, Button, Link } from "@nextui-org/react";
import "./Register.css";
import Logo from "../../components/Logo/Logo";
import { useUser } from "../../features/auth/UserContext";
import { useNavigate } from "react-router-dom";
import { fetchWithoutToken } from "../../features/api/api";

export default function Register() {
  const { user, setUser } = useUser();
  const navigate = useNavigate();
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [passwordRepeat, setPasswordRepeat] = useState("");

  const [invalidForm, setInvalidForm] = useState(false);

  const handleFirstNameChange = (event) => setFirstName(event.target.value);
  const handleLastNameChange = (event) => setLastName(event.target.value);
  const handleEmailChange = (event) => setEmail(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);
  const handlePasswordRepeatChange = (event) =>
    setPasswordRepeat(event.target.value);

  const registerUser = async (event) => {
    event.preventDefault();
    if (password !== passwordRepeat && password === "") {
      setInvalidForm(true);
      return;
    }

    try {
      const response = await fetchWithoutToken("/register", "POST", {
        name: firstName,
        email,
        password,
      });

      if (!response) throw new Error("Failed to authenticate");

      localStorage.setItem("rocketpal-token", response.access_token);
      setUser(response.user);
      navigate("/home", { replace: true });
    } catch (err) {
      console.error("Authentication error:", err);
      navigate("/", { replace: true });
    }
  };

  useEffect(() => {
    if (user) {
      navigate("/home", { replace: true });
      return;
    }
  }, []);

  return (
    <main className="Register">
      <section className="RegisterContainer">
        <div className="Title">
          <div className="LogoContainer">
            <Logo />
            <h1>RocketPal Register!</h1>
          </div>
          <p className="text-zinc-500">Sign up to start reaching your goals!</p>
        </div>

        <div className="FormContainer">
          <div className="FullNameSection" style={{ display: "flex", gap: 10 }}>
            <Input
              isRequired
              type="text"
              label="First Name"
              classNames={{
                label: ["text-black"],
              }}
              onChange={handleFirstNameChange}
            />
            <Input
              type="text"
              label="Last Name"
              classNames={{
                label: ["text-black"],
              }}
              onChange={handleLastNameChange}
            />
          </div>

          <Input
            isRequired
            type="email"
            label="Email"
            classNames={{
              label: ["text-black"],
            }}
            onChange={handleEmailChange}
          />

          <Input
            isRequired
            label="Password"
            type={"password"}
            classNames={{
              label: ["text-black"],
            }}
            onChange={handlePasswordChange}
          />
          <Input
            isRequired
            label="Repeat Password"
            type={"password"}
            classNames={{
              label: ["text-black"],
            }}
            onChange={handlePasswordRepeatChange}
          />

          <div className="InvalidWarning">
            <p
              style={{
                visibility: invalidForm ? "visible" : "hidden",
                color: "red",
              }}
            >
              Form is invalid!
            </p>
          </div>

          <Button color="primary" onClick={registerUser}>
            Login
          </Button>
        </div>
      </section>
    </main>
  );
}
