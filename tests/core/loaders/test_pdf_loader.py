from pathlib import Path

import pytest

from ai_assistant.core.loaders import PDFLoader
from ai_assistant.core.models import Document


def test_load_pdf_file():

    loader = PDFLoader()

    pdf = Path(__file__).parent / "sample.pdf"

    document = loader.load(pdf)

    assert isinstance(document, Document)
    assert document.source == str(pdf)
    assert document.title == "sample"


def test_load_missing_pdf():

    loader = PDFLoader()

    with pytest.raises(FileNotFoundError):
        loader.load("missing.pdf")


def test_load_non_pdf_file(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello")

    loader = PDFLoader()

    with pytest.raises(ValueError):
        loader.load(file)