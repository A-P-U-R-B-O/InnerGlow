from fastapi import APIRouter, Depends, HTTPException, Body
from pydantic import BaseModel
from typing import Optional, Dict, Any

from backend.gemini_api import GeminiAPIClient, get_gemini_client

router = APIRouter(
    prefix="/assistant",
    tags=["assistant"]
)

# Request/response schemas
class AssistantQuery(BaseModel):
    message: str
    user_context: Optional[Dict[str, Any]] = None

class AssistantResponse(BaseModel):
    reply: str
    meta: Optional[Dict[str, Any]] = None

@router.post("/chat", response_model=AssistantResponse)
async def chat_with_assistant(
    query: AssistantQuery = Body(...),
    gemini: GeminiAPIClient = Depends(get_gemini_client)
):
    """
    Send a message to the mental health assistant powered by Gemini API.
    Optionally include user context for personalization (mood, history, etc).
    """
    try:
        gemini_result = await gemini.send_message(query.message, query.user_context)
        # Expecting Gemini API to return {'reply': ..., 'meta': ... }
        return AssistantResponse(
            reply=gemini_result.get("reply", ""),
            meta=gemini_result.get("meta", {})
        )
    except HTTPException as exc:
        raise exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

# Optionally, add health check or assistant info endpoints
@router.get("/info")
def get_assistant_info():
    """
    Returns basic info about the InnerGlow mental health assistant.
    """
    return {
        "name": "InnerGlow",
        "powered_by": "Gemini API",
        "description": "A virtual mental health assistant for support and wellbeing.",
        "features": [
            "Conversational support",
            "Personalized mental wellness tips",
            "Context-aware responses"
        ]
    }
