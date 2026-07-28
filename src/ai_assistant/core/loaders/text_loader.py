from pathlib import Path
from ..models.document import Document
from .base_loader import BaseLoader


class TextLoader(BaseLoader):

    def load(self, path: str | Path) -> Document:

        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(
                f"File not found: {path}"
            )
            
        if path.suffix.lower() != ".txt":
            raise ValueError("Expected a text file.")

        with path.open("r",encoding="utf-8",) as f:
            content = f.read()

        return Document(
            text=content,
            source=str(path),
            title=path.stem,
        )