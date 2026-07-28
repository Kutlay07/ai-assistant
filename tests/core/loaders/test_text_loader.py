from pathlib import Path

import pytest

from ai_assistant.core.loaders import TextLoader
from ai_assistant.core.models import Document


def test_load_text_file(tmp_path):

    file = tmp_path / "sample.txt"
    file.write_text("Hello World", encoding="utf-8")

    loader = TextLoader()

    document = loader.load(file)

    assert isinstance(document, Document)
    assert document.text == "Hello World"
    assert document.source == str(file)
    assert document.title == "sample"


def test_load_missing_file():

    loader = TextLoader()

    with pytest.raises(FileNotFoundError):
        loader.load("missing.txt")


def test_load_non_text_file(tmp_path):

    file = tmp_path / "sample.pdf"
    file.write_text("dummy", encoding="utf-8")

    loader = TextLoader()

    with pytest.raises(ValueError):
        loader.load(file)