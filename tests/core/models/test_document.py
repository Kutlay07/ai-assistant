from ai_assistant.core.models import Document


def test_document_stores_content():

    document = Document(
        text="Hello",
        source="test",)

    assert document.text == "Hello"