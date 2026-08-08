from ..core.models import Request
from ..core.services import SearchService
from ..core.workflows import RAGWorkflow


def register_tools(
    mcp,
    search_service: SearchService,
    rag_workflow: RAGWorkflow,
):

    @mcp.tool()
    def hello() -> str:
        """Simple health check tool."""
        return "Hello from AI Assistant MCP Server!"

    @mcp.tool()
    def search_documents(query: str) -> list[str]:
        """Search indexed documents."""
        chunks = search_service.search(query)

        return [
            chunk.content
            for chunk in chunks
        ]

    @mcp.tool()
    def ask(question: str) -> str:
        """Ask the AI Assistant using the RAG workflow."""
        request = Request(input=question)

        response = rag_workflow.run(request)

        return response.output