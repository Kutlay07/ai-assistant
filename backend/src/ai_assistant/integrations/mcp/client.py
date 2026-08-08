from collections.abc import Sequence
from contextlib import AsyncExitStack

from mcp import ClientSession
from mcp.client.stdio import (
    StdioServerParameters,
    stdio_client,
)


class MCPClient:

    def __init__(
        self,
        command: str,
        args: Sequence[str] | None = None,
    ):
        self._server = StdioServerParameters(
            command=command,
            args=list(args or []),
        )

        self._stack = AsyncExitStack()
        self._session: ClientSession | None = None

    async def connect(self) -> None:
        read_stream, write_stream = await self._stack.enter_async_context(
            stdio_client(self._server)
        )

        self._session = await self._stack.enter_async_context(
            ClientSession(
                read_stream,
                write_stream,
            )
        )

        await self._session.initialize()

    async def list_tools(self):
        if self._session is None:
            raise RuntimeError(
                "MCP client is not connected."
            )

        result = await self._session.list_tools()

        return result.tools

    async def call_tool(
        self,
        name: str,
        arguments: dict | None = None,
    ):
        if self._session is None:
            raise RuntimeError(
                "MCP client is not connected."
            )

        return await self._session.call_tool(
            name=name,
            arguments=arguments or {},
        )

    async def close(self) -> None:
        await self._stack.aclose()

        self._session = None