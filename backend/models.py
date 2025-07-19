from typing import Optional, Dict, Any, List
from datetime import datetime
from pydantic import BaseModel, Field

# User model
class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = True
    profile: Optional[Dict[str, Any]] = None

# Session model (for chat sessions)
class Session(BaseModel):
    id: int
    user_id: int
    started_at: datetime = Field(default_factory=datetime.utcnow)
    ended_at: Optional[datetime] = None
    context: Optional[Dict[str, Any]] = None

# Message model (individual messages)
class Message(BaseModel):
    id: int
    session_id: int
    sender: str  # 'user' or 'assistant'
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    meta: Optional[Dict[str, Any]] = None

# MoodEntry model
class MoodEntry(BaseModel):
    id: int
    user_id: int
    mood: str  # e.g., 'happy', 'sad', 'anxious'
    note: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# JournalEntry model
class JournalEntry(BaseModel):
    id: int
    user_id: int
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    tags: Optional[List[str]] = None
