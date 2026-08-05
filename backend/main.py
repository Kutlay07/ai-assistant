from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ai_assistant.api.v1 import router as v1_router

app = FastAPI(
    title="AI Assistant",
    summary="Production-ready AI assistant",
    description=(
    "A production-ready AI assistant built from scratch with a modular "
    "architecture, supporting chat, RAG, agent workflows, tool calling, "
    "and modern LLM integrations."),
    version="1.0.0",
    contact={
        "name": "Kutlay",
    },
    license_info={
        "name": "MIT",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(v1_router)