// API utility for communicating with InnerGlow backend

const BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

// --- Gemini/Assistant Chat ---
export async function sendAssistantMessage(message, userContext = {}) {
  const res = await fetch(`${BASE_URL}/assistant/chat`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message,
      user_context: userContext
    })
  });
  if (!res.ok) {
    throw new Error(`Assistant API error: ${res.status}`);
  }
  return res.json();
}

// --- Assistant Info ---
export async function fetchAssistantInfo() {
  const res = await fetch(`${BASE_URL}/assistant/info`);
  if (!res.ok) {
    throw new Error("Failed to fetch assistant info");
  }
  return res.json();
}

// --- Model Schemas (for client validation, optional) ---
export async function fetchModelSchemas() {
  const res = await fetch(`${BASE_URL}/schemas`);
  if (!res.ok) {
    throw new Error("Failed to fetch model schemas");
  }
  return res.json();
}

// --- Mood Entry ---
export async function addMoodEntry(userId, mood, note = "") {
  const res = await fetch(`${BASE_URL}/mood`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user_id: userId,
      mood,
      note
    })
  });
  if (!res.ok) {
    throw new Error("Failed to add mood entry");
  }
  return res.json();
}

// --- Journal Entry ---
export async function addJournalEntry(userId, content, tags = []) {
  const res = await fetch(`${BASE_URL}/journal`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      user_id: userId,
      content,
      tags
    })
  });
  if (!res.ok) {
    throw new Error("Failed to add journal entry");
  }
  return res.json();
}

// --- You can add more feature APIs below as needed ---
