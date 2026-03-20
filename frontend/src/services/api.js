import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-service-kkl5.onrender.com", // your Render URL
});

export const analyzeText = (text) =>
  API.post("/analyze", { text });