from fastapi import FastAPI, Depends
from fastapi.responses import StreamingResponse
from fastapi import Request as FastAPIRequest

from ai_assistant.core.models import Request
from ai_assistant.core.assistant import Assistant

from .schemas import ChatRequest, ChatResponse
from .dependencies import get_assistant


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


@app.post(
    "/chat",
    tags=["Chat"],
    response_model=ChatResponse,
)
def chat(
    request: ChatRequest,
    assistant: Assistant = Depends(get_assistant),
    ):
    
    core_request = Request(
        input=request.message,
    )
    
    response = assistant.handle(core_request)
    
    return ChatResponse(
        response=response.output,
    )


@app.post(
    "/chat/stream",
    tags=["Chat"],
    summary="Stream chat responses",
)

async def stream_chat(
    request: ChatRequest,
    http_request: FastAPIRequest,
    assistant: Assistant = Depends(get_assistant),
    ):
    
    core_request = Request(
        input=request.message,
    )
    
    async def stream_response():
        for chunk in assistant.stream(core_request):
            if await http_request.is_disconnected():
                return
            
            yield chunk
    
    return StreamingResponse(
        stream_response(),
        media_type="text/plain",
    )