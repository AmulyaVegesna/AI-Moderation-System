import React, { useEffect, useState } from "react";
import { getPosts, deletePost } from "../services/api";

const AdminDashboard = () => {
  const [posts, setPosts] = useState([]);

  const fetchPosts = async () => {
    try {
      const res = await getPosts();
      setPosts(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  const handleDelete = async (id) => {
    await deletePost(id);
    fetchPosts();
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div>
      <h2>Admin Dashboard</h2>

      {posts.length === 0 && <p>No posts yet</p>}

      {posts.map((post) => (
        <div
          key={post._id}
          style={{
            border: "1px solid gray",
            padding: "10px",
            margin: "10px"
          }}
        >
          <p><b>Text:</b> {post.text}</p>
          <p><b>Score:</b> {post.score}</p>
          <p><b>Category:</b> {post.category}</p>
          <p><b>Action:</b> {post.action}</p>

          <button onClick={() => handleDelete(post._id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
};

export default AdminDashboard;