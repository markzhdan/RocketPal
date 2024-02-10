import React, { createContext, useState, useContext, useEffect } from "react";
import { fetchWithToken } from "../api/api";

const UserContext = createContext({});

export const UserProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [isAuthenticating, setIsAuthenticating] = useState(true);
  // has token ?!? this can be used to immeditelity direct to dashboard so you dont see the site

  const fetchUserData = async () => {
    const token = localStorage.getItem("rocketpal-token");

    if (!token) {
      setUser(null);
      return;
    }
    setIsAuthenticating(true);

    // TODO: CHECK setuser in callback
    try {
      const response = await fetchWithToken("/me");
      setUser(response.user);
    } catch (error) {
      console.log("Error fetching user data:", error);
      setUser(null);
    } finally {
      setIsAuthenticating(false);
    }
  };

  useEffect(() => {
    fetchUserData();
  }, []);

  const logout = () => {
    localStorage.removeItem("rocketpal-token");
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, isAuthenticating, setUser, logout }}>
      {children}
    </UserContext.Provider>
  );
};

export const useUser = () => useContext(UserContext);
