from fastapi import APIRouter, Depends
from fastapi import Request as FastAPIRequest
from fastapi.responses import StreamingResponse

from ai_assistant.core.assistant import Assistant
from ai_assistant.core.models import Request

from ..dependencies import get_rag_assistant
from ..schemas import ChatRequest, ChatResponse

router = APIRouter()


@router.post(
    "/rag",
    response_model=ChatResponse,
    tags=["RAG"],
)
def rag(
    request: ChatRequest,
    assistant: Assistant = Depends(get_rag_assistant),
):

    core_request = Request(
        input=request.message,
    )

    response = assistant.handle(core_request)

    return ChatResponse(
        response=response.output,
    )


@router.post(
    "/rag/stream",
    tags=["RAG"],
    summary="Stream RAG responses",
)
async def stream_rag(
    request: ChatRequest,
    http_request: FastAPIRequest,
    assistant: Assistant = Depends(get_rag_assistant),
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