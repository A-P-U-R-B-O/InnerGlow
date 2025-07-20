import React, { useEffect, useState } from "react";
import AssistantInfo from "./AssistantInfo";
import ChatBox from "./ChatBox";
import "./styles.css";

const API_URL = process.env.REACT_APP_API_URL;

// Example: Fetching backend status/root endpoint and showing it at the top.
// You can expand this to fetch other endpoints as needed.

function App() {
  // State for backend status
  const [status, setStatus] = useState(null);
  const [statusError, setStatusError] = useState(null);

  useEffect(() => {
    // Fetch backend root status on mount
    fetch(`${API_URL}/health`)
      .then((res) => {
        if (!res.ok) throw new Error("Failed to fetch backend status");
        return res.json();
      })
      .then(setStatus)
      .catch((err) => setStatusError(err.message));
  }, []);

  return (
    <div className="app-background">
      <header className="app-header">
        <h1 className="app-title">InnerGlow</h1>
        <p className="app-subtitle">
          Your virtual mental health assistant, powered by Gemini AI
        </p>
        <div style={{ marginTop: "1rem" }}>
          {statusError && (
            <span className="error">
              Could not connect to backend: {statusError}
            </span>
          )}
          {status && (
            <span>
              <strong>Backend status:</strong> {status.status} | Version: {status.version}
            </span>
          )}
        </div>
      </header>
      <main className="app-main">
        <AssistantInfo />
        <ChatBox />
      </main>
      <footer className="app-footer">
        <span>
          &copy; {new Date().getFullYear()} InnerGlow &mdash; For wellbeing and self-care.
        </span>
      </footer>
    </div>
  );
}

export default App;
