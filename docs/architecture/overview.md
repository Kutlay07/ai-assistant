# Architecture Overview

## Overview

AI Assistant is a production-oriented, provider-independent AI assistant framework built around clean architecture principles.

The project is designed to support multiple workflows such as chat, retrieval-augmented generation (RAG), and autonomous agents while remaining modular and easily extensible.

The assistant communicates exclusively through abstractions, allowing implementations to evolve without affecting the overall architecture.



## Design Principles

- Modular architecture
- Provider independence
- Dependency injection
- Clean interfaces
- Testability
- Incremental development
- Small focused components



## High-Level Architecture

```text
                User
                  │
                  ▼
             Assistant
                  │
                  ▼
            BaseWorkflow
                  │
     ┌────────────┼────────────┐
     │            │            │
     ▼            ▼            ▼
ChatWorkflow RAGWorkflow AgentWorkflow
     │            │            │
     └────────────┼────────────┘
                  ▼
          Shared Components
                  │
 ┌────────┬────────┬────────┬────────┐
 ▼        ▼        ▼        ▼
Prompt  Memory   LLM   Embedder
Builder
                  │
                  ▼
                BaseTool
```



## Core Components

| Component | Responsibility |
|-----------|----------------|
| Assistant | Coordinate workflow execution |
| Workflows | Execute request processing strategies |
| Documents | Shared retrieval domain models |
| Loaders | Load documents from different data sources |
| Text Splitter | Divide documents into overlapping chunks |
| Prompt Builder | Construct reusable prompts |
| Memory | Store conversation history |
| LLM | Provider-independent language model interface |
| Embedder | Generate vector representations |
| Vector Store | Store and search embeddings |
| Retriever | Retrieve relevant document chunks |
| Tools | Execute external capabilities |
| Planner | Multi-step planning |
| API Layer | Handle HTTP requests |



## Future Extensions

- Planning
- Function Calling
- MCP
- Multi-Agent
- Voice
- Vision
- Web UI



## Architecture Decision Records

- ADR-0001 — Project Philosophy
- ADR-0002 — Provider Independence



## Documentation Structure

Detailed architecture documentation is organized into separate modules:

- Assistant
- Workflows
- Memory
- LLM
- Retrieval
- Planner
- Tools
- Lifecycle