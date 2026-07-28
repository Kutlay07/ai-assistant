from pathlib import Path
from pypdf import PdfReader
from ..models.document import Document
from .base_loader import BaseLoader


class PDFLoader(BaseLoader):
    
    def load(self, path: str | Path) -> Document:
        path = Path(path)

        if not path.is_file():
            raise FileNotFoundError(f"File not found:\n {path}")
        
        if path.suffix.lower() != ".pdf":
            raise ValueError("Expected a PDF file.") 
        
        reader = PdfReader(path)
        
        content = "\n".join(
            page.extract_text() or ""
            for page in reader.pages
        )
        
        if not content.strip():
            raise ValueError(
                "The PDF does not contain extractable text.")
            
        
        return Document(
            text = content,
            source = str(path),
            title = path.stem
            )