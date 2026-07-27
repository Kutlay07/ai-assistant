from ai_assistant.core.models import Document


def test_document_stores_content():

    document = Document(content="Hello")

    assert document.content == "Hello"