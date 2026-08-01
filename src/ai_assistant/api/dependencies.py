from ai_assistant.core.assistant import Assistant

from ai_assistant.core.embedders import MockEmbedder
from ai_assistant.core.llms import create_llm
from ai_assistant.core.memory import MockMemory
from ai_assistant.core.models import Chunk
from ai_assistant.core.prompts import PromptBuilder
from ai_assistant.core.retrievers import MockRetriever
from ai_assistant.core.services import SearchService
from ai_assistant.core.vector_stores import MockVectorStore
from ai_assistant.core.workflows import ChatWorkflow, RAGWorkflow


def create_search_service() -> SearchService:
    chunks = [
        Chunk(
            content="FastAPI is a modern Python web framework.",
        ),
        Chunk(
            content="RAG combines retrieval with language models.",
        ),
        Chunk(
            content="Groq provides an OpenAI-compatible API.",
        ),
    ]

    embedder = MockEmbedder()

    vector_store = MockVectorStore(
        chunks=chunks,
    )

    retriever = MockRetriever(
        embedder=embedder,
        vector_store=vector_store,
    )

    return SearchService(
        retriever=retriever,
    )
    


def get_assistant() -> Assistant:
    workflow = ChatWorkflow(
        llm=create_llm(),
        prompt_builder=PromptBuilder(),
        memory=MockMemory(),
    )

    return Assistant(workflow)


def get_rag_assistant() -> Assistant:
    workflow = RAGWorkflow(
        llm=create_llm(),
        prompt_builder=PromptBuilder(),
        search_service=create_search_service(),
        memory=MockMemory(),
    )

    return Assistant(workflow)
