import React, { useState } from "react";
import { analyzeText } from "../services/api";

const TextInput = () => {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = async () => {
  if (!text) return alert("Enter some text");

  setLoading(true);       // START loading
  setResult(null);        // clear old result

  try {
    const res = await analyzeText(text);
    setResult(res.data);
  } catch (err) {
    console.error(err);
    alert("Backend not running");
  }

  setLoading(false);      // STOP loading
};

  

  return (
    <div>
      <h2>Enter Text</h2>

      <textarea
        rows="4"
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br /><br />

      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
      {loading && <div className="loader"></div>}

      {result && (
        <div className="fade-in">
          <p>Score: {result.score}%</p>
          <div className="progress">
            <div 
              className="progress-fill"
              style={{ width: `${result.score}%` }}
            ></div>
          </div>
          {result && (
            <div
              className="fade-in"
              style={{
                background:
                  result.score > 70
                    ? "rgba(239, 68, 68, 0.6)"   // 🔴 toxic
                    : result.score > 40
                    ? "rgba(234, 179, 8, 0.6)"   // 🟡 medium
                    : "rgba(34, 197, 94, 0.6)",  // 🟢 safe
                padding: "15px",
                borderRadius: "12px",
                marginTop: "15px",
                backdropFilter: "blur(10px)"
              }}
            >
              {/* Score */}
              <p>Score: {result.score}%</p>

              {/* Progress bar */}
              <div className="progress">
                <div
                  className="progress-fill"
                  style={{ width: `${result.score}%` }}
                ></div>
              </div>

              {/* Category */}
              <p>
                Category:
                <span className={`badge ${result.category === "Safe" ? "green" : "red"}`}>
                  {result.category}
                </span>
              </p>

              {/* Action */}
              <p>
                Action:
                <span
                  className={`badge ${
                    result.action === "Allow"
                      ? "green"
                      : result.action === "Warn"
                      ? "yellow"
                      : "red"
                  }`}
                >
                  {result.action}
                </span>
              </p>
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default TextInput;