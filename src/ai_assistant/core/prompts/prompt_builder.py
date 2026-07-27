from ..models.request import Request
from collections.abc import Sequence
from pathlib import Path



TEMPLATE_DIR = Path(__file__).parent / "templates"
class PromptBuilder:
    
    def _load_template(self, name: str) -> str:
        template_path = TEMPLATE_DIR / f"{name}.txt"
    
        with template_path.open(encoding="utf-8") as f:
            return f.read()
    
    def build(self, request: Request, history: Sequence[str]) -> str:
        template = self._load_template("chat")
        
        history_text = "\n".join(history)
        
        return template.format(
            history=history_text,
            input=request.input,
        )