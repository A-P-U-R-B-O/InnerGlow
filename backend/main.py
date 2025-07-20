from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

from backend.assistant import router as assistant_router
# If you plan to use database or background tasks in future, import here.

app = FastAPI(
    title="InnerGlow Mental Health Assistant",
    description="A virtual mental health assistant powered by Gemini API, with journaling and mood tracking features.",
    version="1.0.0"
)

# Advanced CORS configuration
origins = os.getenv("CORS_ORIGINS", "*")
if isinstance(origins, str):
    # Accept comma-separated env list or "*"
    if origins != "*":
        origins = [o.strip() for o in origins.split(",") if o.strip()]
    else:
        origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Health/Status endpoint for frontend ---
@app.get("/health", tags=["root"])
def read_health():
    """Health/status endpoint for frontend."""
    return {
        "service": "InnerGlow",
        "status": "OK",
        "version": "1.0.0",
        "docs_url": "/docs"
    }

# --- Include assistant router BEFORE mounting static files ---
app.include_router(assistant_router)

# --- Optionally expose model schemas for frontend/clients ---
from backend.models import User, Session, Message, MoodEntry, JournalEntry

@app.get("/schemas", tags=["meta"])
def get_model_schemas():
    """Returns Pydantic model schemas for API clients."""
    return {
        "User": User.schema(),
        "Session": Session.schema(),
        "Message": Message.schema(),
        "MoodEntry": MoodEntry.schema(),
        "JournalEntry": JournalEntry.schema()
    }

# --- Advanced health checks, startup, and shutdown events ---
@app.on_event("startup")
async def startup_event():
    # You could initialize DB connections, background workers, etc.
    print("🚀 InnerGlow backend started")

@app.on_event("shutdown")
async def shutdown_event():
    # Clean up resources, close DB connections, etc.
    print("💤 InnerGlow backend shutting down")

# --- Advanced global error handler example ---
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exception_handlers import RequestValidationError
from fastapi.exceptions import HTTPException

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail, "type": "HTTPException"}
    )

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors(), "body": exc.body, "type": "ValidationError"}
    )

# --- Mount React build as static files at root ---
static_folder = os.path.join(os.path.dirname(__file__), '../frontend/build')
app.mount("/", StaticFiles(directory=static_folder, html=True), name="static")

# --- Advanced: ready for adding more routers ---
# For future: from backend.journal import router as journal_router
# For future: app.include_router(journal_router)
# For future: from backend.mood import router as mood_router
# For future: app.include_router(mood_router)
