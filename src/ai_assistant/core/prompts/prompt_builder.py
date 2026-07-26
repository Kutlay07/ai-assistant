from ..models.request import Request


class PromptBuilder:

    def build(self, request: Request) -> str:
        return request.input