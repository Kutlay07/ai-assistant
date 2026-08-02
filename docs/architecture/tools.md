# Tools

## Overview

Tools provide a common interface for executing external capabilities independently from workflow logic.

Workflows never communicate with concrete tool implementations directly. Instead, they interact through shared abstractions and supporting components responsible for registration, parsing, validation, and execution.

The tool system consists of:

- BaseTool
- ToolRegistry
- ToolCall
- ToolCallParser
- ToolCallValidator



# BaseTool

`BaseTool` defines the common contract implemented by every tool.

Each tool exposes a single execution interface while hiding implementation details from workflows.

The assistant communicates exclusively through this abstraction.



## Current Implementations

- `MockTool`



## Planned Implementations

Future tools may include:

- `CalculatorTool`
- `SearchTool`
- `WeatherTool`
- `FileTool`



## MockTool

`MockTool` is intended for development and testing.

Characteristics:

- Deterministic responses
- No external services
- Fast execution



# ToolRegistry

`ToolRegistry` manages all available tools.

It is responsible for:

- Registering tools
- Looking up tools by name
- Providing tool instances during execution

The assistant depends on the registry instead of individual tool implementations.



# ToolCall

`ToolCall` represents a structured request to execute a tool.

Instead of relying on raw strings, workflows exchange structured tool invocation objects.

Typical fields include:

- Tool name
- Arguments



# ToolCallParser

`ToolCallParser` converts language model output into structured `ToolCall` objects.

Separating parsing from execution allows parsing strategies to evolve independently from workflows.



# ToolCallValidator

`ToolCallValidator` validates parsed tool calls before execution.

Typical validation includes:

- Tool name validation
- Argument validation
- Structural validation

Keeping validation separate improves reliability and simplifies testing.



# Tool Execution Flow

```text
LLM
 │
 ▼
ToolCallParser
 │
 ▼
ToolCall
 │
 ▼
ToolCallValidator
 │
 ▼
ToolRegistry
 │
 ▼
BaseTool
 │
 ▼
Tool Result
```