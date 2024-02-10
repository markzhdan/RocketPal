import React, { useEffect } from "react";
import { Navigate } from "react-router-dom";
import { useUser } from "../auth/UserContext";

import LoginLoading from "../../components/Loading/LoginLoading";

const ProtectedRoute = ({ children }) => {
  const { user, isAuthenticating } = useUser();

  if (isAuthenticating) {
    return <LoginLoading />;
  }

  if (!user) {
    // Redirect to the login page if the user is not authenticated
    return <Navigate to="/login" replace />;
  }

  return children;
};

export default ProtectedRoute;
