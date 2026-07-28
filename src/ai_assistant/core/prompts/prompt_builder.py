from collections.abc import Sequence
from pathlib import Path

from ..models.request import Request
from ..models import Chunk


TEMPLATE_DIR = Path(__file__).parent / "templates"


class PromptBuilder:
    def _load_template(self, name: str) -> str:
        template_path = TEMPLATE_DIR / f"{name}.txt"

        with template_path.open(encoding="utf-8") as f:
            return f.read()

    def build(
        self,
        request: Request,
        history: Sequence[str],
        template: str = "chat",
        context: list[Chunk] | None = None
    ) -> str:
        template_text = self._load_template(template)

        history_text = "\n".join(history)
        
        context_text = ""

        if context:
            context_text = "\n".join(
                chunk.content for chunk in context
            )

        return template_text.format(
            history=history_text,
            input=request.input,
            context=context_text,
        )