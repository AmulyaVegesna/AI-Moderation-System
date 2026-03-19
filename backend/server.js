//Imports
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");
const axios = require("axios");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

//MongoDB connection
mongoose.connect("mongodb://127.0.0.1:27017/moderationDB")
  .then(() => console.log("MongoDB Connected"))
  .catch(err => console.log(err));


//Schema
const PostSchema = new mongoose.Schema({
  text: String,
  score: Number,
  category: String,
  action: String,
  createdAt: { type: Date, default: Date.now }
});

//Model
const Post = mongoose.model("Post", PostSchema);


//Actions
function getAction(score) {
  if (score <= 30) return "Allow";
  if (score <= 70) return "Warn";
  return "Block";
}


//Post
app.post("/analyze", async (req, res) => {
  try {
    const { text } = req.body;
        const aiResponse = await axios.post("http://127.0.0.1:5001/analyze",
      { text }
    );
    const { score, category } = aiResponse.data;
    const action = getAction(score);
    const post = new Post({
      text,
      score,
      category,
      action
    });

    await post.save();

    res.json({ score, category, action });
    } catch (error) {
    console.error(error);
    res.status(500).json({ error: "Server error" });
  }
});

//Get post
app.get("/posts", async (req, res) => {
  const posts = await Post.find().sort({ createdAt: -1 });
  res.json(posts);
});

//delete
app.delete("/post/:id", async (req, res) => {
  await Post.findByIdAndDelete(req.params.id);
  res.json({ message: "Deleted" });
});

//app.listen
app.listen(5002, () => {
  console.log("Server running on port 5002");
});