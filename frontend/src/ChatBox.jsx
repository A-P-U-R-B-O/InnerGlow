import React, { useState, useRef, useEffect } from "react";
import { sendAssistantMessage } from "./api";
import "./styles.css";

const userAvatar = "🧑";
const assistantAvatar = "🌟";

const ChatBox = () => {
  const [messages, setMessages] = useState([
    {
      sender: "assistant",
      content:
        "Hi there! 🌟 I’m InnerGlow, your mental health assistant. How are you feeling today?",
      timestamp: new Date().toLocaleTimeString(),
    },
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = async (e) => {
    e.preventDefault();
    const trimmed = input.trim();
    if (!trimmed || loading) return;

    // Add user message
    const userMsg = {
      sender: "user",
      content: trimmed,
      timestamp: new Date().toLocaleTimeString(),
    };
    setMessages((prev) => [...prev, userMsg]);
    setInput("");
    setLoading(true);
    setError("");

    try {
      // You can pass user context if needed
      const response = await sendAssistantMessage(trimmed);
      setMessages((prev) => [
        ...prev,
        {
          sender: "assistant",
          content: response.reply,
          timestamp: new Date().toLocaleTimeString(),
        },
      ]);
    } catch (err) {
      setError("Sorry, something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chatbox-container">
      <div className="chatbox-header">
        <span className="chatbox-title">InnerGlow Chat</span>
      </div>
      <div className="chatbox-messages">
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={`chatbox-message ${
              msg.sender === "assistant"
                ? "assistant-message"
                : "user-message"
            }`}
          >
            <span className="chatbox-avatar">
              {msg.sender === "assistant" ? assistantAvatar : userAvatar}
            </span>
            <div className="chatbox-bubble">
              <div className="chatbox-content">{msg.content}</div>
              <div className="chatbox-timestamp">{msg.timestamp}</div>
            </div>
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>
      <form className="chatbox-form" onSubmit={handleSend}>
        <input
          type="text"
          className="chatbox-input"
          value={input}
          placeholder="Type your message…"
          onChange={(e) => setInput(e.target.value)}
          disabled={loading}
          autoFocus
        />
        <button
          type="submit"
          className="chatbox-send"
          disabled={loading || !input.trim()}
        >
          {loading ? "..." : "Send"}
        </button>
      </form>
      {error && <div className="chatbox-error">{error}</div>}
    </div>
  );
};

export default ChatBox;
