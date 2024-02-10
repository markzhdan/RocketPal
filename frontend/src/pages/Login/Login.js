import React, { useEffect, useState } from "react";
import { Input, Button, Link } from "@nextui-org/react";
import "./Login.css";
import Logo from "../../components/Logo/Logo";
import { useUser } from "../../features/auth/UserContext";
import { useNavigate } from "react-router-dom";
import { fetchWithoutToken } from "../../features/api/api";
import { EyeFilledIcon } from "./EyeFilledIcon";
import { EyeSlashFilledIcon } from "./EyeSlashedFilledIcon";

export default function Login() {
  const { user, setUser } = useUser();
  const navigate = useNavigate();
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const [isVisible, setIsVisible] = useState(false);

  const toggleVisibility = () => setIsVisible(!isVisible);
  const handleEmailChange = (event) => setUsername(event.target.value);
  const handlePasswordChange = (event) => setPassword(event.target.value);

  const fetchJWT = async (event) => {
    try {
      const response = await fetchWithoutToken("/login", "POST", {
        email: username,
        password,
      });

      if (!response) throw new Error("Failed to authenticate");

      localStorage.setItem("rocketpal-token", response.access_token);
      setUser(response.user);
      navigate("/home", { replace: true });
    } catch (err) {
      console.error("Authentication error:", err);
      navigate("/login", { replace: true });
    }
  };

  useEffect(() => {
    if (user) {
      navigate("/home", { replace: true });
      return;
    }

    fetchJWT();
  }, []);

  return (
    <main className="Login">
      <section className="LoginContainer">
        <div className="Title">
          <div className="LogoContainer">
            <Logo />
            <h1>RocketPal Log In</h1>
          </div>
          <p className="text-zinc-500">
            Log into your account to reach your goals!
          </p>
        </div>

        <div className="FormContainer">
          <Input
            type="email"
            label="Email"
            classNames={{
              label: ["text-black"],
            }}
            onChange={handleEmailChange}
          />

          <Input
            label="Password"
            endContent={
              <button type="button" onClick={toggleVisibility}>
                {isVisible ? (
                  <EyeSlashFilledIcon className="text-2xl text-default-400 pointer-events-none" />
                ) : (
                  <EyeFilledIcon className="text-2xl text-default-400 pointer-events-none" />
                )}
              </button>
            }
            type={isVisible ? "text" : "password"}
            classNames={{
              label: ["text-black"],
            }}
            onChange={handlePasswordChange}
          />

          <Link color="foreground" href="/register">
            Not signed up? Sign up now.
          </Link>

          <Button color="primary" onClick={fetchJWT}>
            Login
          </Button>
        </div>
      </section>
    </main>
  );
}
