import axios from "axios";

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL + "/api",
});

export const fetchWithToken = async (endpoint, method = "GET", data = null) => {
  const token = localStorage.getItem("rocketpal-token");

  try {
    const response = await api({
      method: method,
      url: endpoint,
      headers: {
        Authorization: `Bearer ${token}`,
      },
      data: data,
    });

    return response.data;
  } catch (error) {
    console.error("API call error:", error.response || error);
    throw error;
  }
};

export const fetchWithoutToken = async (
  endpoint,
  method = "GET",
  data = null
) => {
  try {
    const response = await api({
      method: method,
      url: endpoint,
      data: data,
    });

    return response.data;
  } catch (error) {
    console.error("API call error:", error.response || error);
    throw error;
  }
};
