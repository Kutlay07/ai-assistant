from fastapi import FastAPI

app = FastAPI(
    title="AI Assistant",
    summary="Production-ready AI assistant",
    description=(
    "A production-ready AI assistant built from scratch with a modular "
    "architecture, supporting chat, RAG, agent workflows, tool calling, "
    "and modern LLM integrations."),
    version="0.9.0",
    contact={
        "name": "Kutlay",
    },
    license_info={
        "name": "MIT",
    },
)


@app.get(
    "/health",
    tags=["System"],
    summary="Health check",
)
def health():
    return {
        "status": "ok",
    }