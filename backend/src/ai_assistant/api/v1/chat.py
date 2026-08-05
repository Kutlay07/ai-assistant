from fastapi import APIRouter, Depends
from fastapi import Request as FastAPIRequest
from fastapi.responses import StreamingResponse

from ai_assistant.core.assistant import Assistant
from ai_assistant.core.models import Request
from ai_assistant.core.memory import FileMemory

from ..schemas import (
    ChatRequest, 
    ChatResponse, 
    MessageResponse
    )
from ..dependencies import (
    get_assistant, 
    get_memory
    )

router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse,
    tags=["Chat"],
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


@router.post(
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


@router.get(
    "/chat/history",
    tags=["Chat"],
    response_model=list[MessageResponse],
)
def chat_history(
    memory: FileMemory = Depends(get_memory),
):
    return memory.get_messages()