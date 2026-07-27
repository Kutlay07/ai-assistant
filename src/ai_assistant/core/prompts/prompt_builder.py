from ..models.request import Request
from collections.abc import Sequence


class PromptBuilder:

    def build(self, request: Request, history: Sequence[str]) -> str:
        return request.input