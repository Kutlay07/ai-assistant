from fastapi import FastAPI

from ai_assistant.api.chat import router as chat_router

app = FastAPI(
    title="AI Assistant",
    version="0.1.0",
)

app.include_router(chat_router)