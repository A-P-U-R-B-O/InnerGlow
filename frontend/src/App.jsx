import React from "react";
import AssistantInfo from "./AssistantInfo";
import ChatBox from "./ChatBox";
import "./styles.css";

function App() {
  return (
    <div className="app-background">
      <header className="app-header">
        <h1 className="app-title">InnerGlow</h1>
        <p className="app-subtitle">
          Your virtual mental health assistant, powered by Gemini AI
        </p>
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
