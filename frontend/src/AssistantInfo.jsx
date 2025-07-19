import React from "react";
import "./styles.css";

const AssistantInfo = () => {
  return (
    <div className="assistant-info">
      <div className="assistant-avatar">
        {/* Replace with your own SVG, image, or emoji for branding */}
        <span role="img" aria-label="InnerGlow Assistant" className="avatar-emoji">🌟</span>
      </div>
      <h2 className="assistant-title">Meet InnerGlow</h2>
      <p className="assistant-description">
        <strong>InnerGlow</strong> is your personal mental health assistant, powered by Gemini AI.<br />
        Start a conversation, track your mood, and journal your thoughts – all in a safe, supportive space.<br />
        <br />
        <span className="features-title">Features:</span>
        <ul className="features-list">
          <li>🗨️ Conversational support for mental wellness</li>
          <li>🌈 Personalized mood tracking</li>
          <li>📔 Secure journaling</li>
          <li>💡 Context-aware insights & tips</li>
        </ul>
        <span className="disclaimer">
          <em>Note: InnerGlow is not a substitute for professional medical advice or crisis support.</em>
        </span>
      </p>
    </div>
  );
};

export default AssistantInfo;
