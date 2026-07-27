import pytest

from ai_assistant.core.models import Document, Chunk
from ai_assistant.core.splitters import TextSplitter


def test_split_returns_chunks():

    splitter = TextSplitter()

    document = Document(content="Hello World")

    chunks = splitter.split(document)

    assert isinstance(chunks, list)
    assert isinstance(chunks[0], Chunk)

    assert len(chunks) == 1
    assert chunks[0].content == document.content


def test_split_creates_multiple_chunks():

    splitter = TextSplitter(
        chunk_size=5,
        overlap=0,
    )

    document = Document(content="Hello World")

    chunks = splitter.split(document)

    assert len(chunks) == 3


def test_split_applies_overlap():

    splitter = TextSplitter(
        chunk_size=4,
        overlap=2,
    )

    document = Document(content="abcdef")

    chunks = splitter.split(document)

    assert chunks[0].content == "abcd"
    assert chunks[1].content == "cdef"
    assert chunks[2].content == "ef"


def test_invalid_chunk_parameters():

    with pytest.raises(ValueError):
        TextSplitter(chunk_size=0)

    with pytest.raises(ValueError):
        TextSplitter(
            chunk_size=10,
            overlap=10,
        )

    with pytest.raises(ValueError):
        TextSplitter(
            chunk_size=10,
            overlap=-1,
        )

    with pytest.raises(ValueError):
        TextSplitter(
            chunk_size=10,
            overlap=11,
        )


def test_split_empty_document_returns_no_chunks():

    splitter = TextSplitter()

    document = Document(content="")

    chunks = splitter.split(document)

    assert chunks == []


def test_split_short_document_returns_single_chunk():

    splitter = TextSplitter(chunk_size=100)

    document = Document(content="Hello")

    chunks = splitter.split(document)

    assert len(chunks) == 1
    assert chunks[0].content == "Hello"