import axios from "axios";

const API = axios.create({
  baseURL: "https://ai-service-kkl5.onrender.com",
});

export const analyzeText = (text) =>
  API.post("/analyze", { text });

export const getPosts = () =>
  API.get("/posts");

export const deletePost = (text) =>
  API.delete(`/delete/${text}`);