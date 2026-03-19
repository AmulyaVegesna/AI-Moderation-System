import React from "react";
import TextInput from "./components/TextInput";
import AdminDashboard from "./components/AdminDashboard";

function App() {
  return (
    <div className="container">
      <h1>AI Social Media Moderation System</h1>

      <TextInput />
      <AdminDashboard />
    </div>
  );
}

export default App;