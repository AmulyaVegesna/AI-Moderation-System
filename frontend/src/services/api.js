import axios from "axios";

const API = axios.create({
  baseURL: "http://127.0.0.1:5002"
});

export const analyzeText = (text) => API.post("/analyze", { text });
export const getPosts = () => API.get("/posts");
export const deletePost = (id) => API.delete(`/post/${id}`);