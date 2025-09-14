import axios from "axios";

const API_URL = "http://localhost:8000";

export const signup = (email: string, password: string) =>
  axios.post(`${API_URL}/auth/signup`, { email, password });

export const login = (email: string, password: string) =>
  axios.post(`${API_URL}/auth/login`, { email, password });
