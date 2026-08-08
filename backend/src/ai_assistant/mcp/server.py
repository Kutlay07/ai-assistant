from mcp.server import MCPServer

from .dependencies import (
    rag_workflow,
    search_service,
)
from .tools import register_tools


mcp = MCPServer("AI Assistant")

register_tools(
    mcp=mcp,
    search_service=search_service,
    rag_workflow=rag_workflow,
)


if __name__ == "__main__":
    mcp.run()