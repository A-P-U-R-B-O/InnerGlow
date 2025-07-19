import os
import httpx
from fastapi import HTTPException
from typing import Dict, Any, Optional

# Load your Gemini API key from environment variables for security
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL", "https://api.gemini.example.com/v1/chat")

class GeminiAPIClient:
    def __init__(self, api_key: Optional[str] = None, api_url: Optional[str] = None):
        self.api_key = api_key or GEMINI_API_KEY
        self.api_url = api_url or GEMINI_API_URL
        if not self.api_key:
            raise ValueError("Gemini API key not set. Please set GEMINI_API_KEY in environment.")

    async def send_message(self, message: str, user_context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Send a message to the Gemini API and return the response.
        Optionally include user context for personalization.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "message": message,
            "context": user_context or {}
        }

        async with httpx.AsyncClient(timeout=20.0) as client:
            try:
                response = await client.post(self.api_url, json=payload, headers=headers)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as exc:
                raise HTTPException(
                    status_code=exc.response.status_code,
                    detail=f"Gemini API error: {exc.response.text}"
                )
            except Exception as exc:
                raise HTTPException(
                    status_code=500,
                    detail=f"Internal error communicating with Gemini API: {str(exc)}"
                )

# For convenience, you can create a singleton Gemini client for the app
gemini_client = GeminiAPIClient()

# Example FastAPI dependency for route handlers
def get_gemini_client() -> GeminiAPIClient:
    return gemini_client

# Example usage in a route:
# from fastapi import APIRouter, Depends
# router = APIRouter()
#
# @router.post("/assistant/gemini")
# async def chat_with_gemini(
#     message: str,
#     user_context: Optional[Dict[str, Any]] = None,
#     gemini: GeminiAPIClient = Depends(get_gemini_client)
# ):
#     response = await gemini.send_message(message, user_context)
#     return response
