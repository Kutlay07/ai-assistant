from fastapi import APIRouter

from .chat import router as chat_router
from .rag import router as rag_router
from .health import router as health_router


router = APIRouter(prefix="/api/v1")

router.include_router(chat_router)
router.include_router(rag_router)
router.include_router(health_router)