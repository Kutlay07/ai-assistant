from ..models.request import Request


class PromptBuilder:

    def build(self, request: Request, history: list[str]) -> str:
        return request.input