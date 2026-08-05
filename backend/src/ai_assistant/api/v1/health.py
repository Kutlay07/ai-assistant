from fastapi import APIRouter

from ..schemas import HealthResponse

router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    tags=["System"],
)
def health():
    return HealthResponse(
        status="ok"
    )