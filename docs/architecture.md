# AI Assistant Architecture

## Overview

This project aims to become a production-ready, provider-independent AI Assistant platform.

RAG is one of many modular capabilities and is not treated as the core of the system.

The goal of the Assistant is to run various LLM providers and tools under a common core.



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

| Component      | Responsibility |
|----------------|----------------|
| Assistant      | Coordinate workflow execution |
| Workflows      | Execute request processing strategies |
| Documents      | Shared retrieval domain models |
| Loaders        | Load documents from different data sources |
| Text Splitter  | Divide documents into overlapping chunks |
| Prompt Builder | Construct reusable prompts |
| Memory         | Store conversation history |
| LLM            | Provider-independent language model interface |
| Embedder       | Generate vector representations |
| Vector Store   | Store and search embeddings |
| Retriever      | Retrieve relevant document chunks |
| Tools          | Execute external capabilities |
| Planner        | Multi-step planning |

## Assistant

The Assistant is the application's orchestration layer and the main entry point of the system.

The Assistant receives a workflow implementation through constructor injection and delegates request execution to the configured workflow.

The Assistant intentionally contains no business logic.

### Responsibilities

- Receive incoming requests.
- Delegate execution to the configured workflow.
- Return the generated response.

### Non-Responsibilities

The Assistant is **not** responsible for:

- Building prompts
- Managing memory
- Executing tools
- Performing retrieval
- Calling LLM providers directly

These responsibilities belong to the workflow and its underlying services.



## Workflow

A workflow defines how a request is processed.

Different workflows may implement different execution strategies while exposing the same public interface.

Examples include:

- Chat Workflow
- RAG Workflow
- Agent Workflow


All workflows coordinate execution by composing shared abstractions such as `PromptBuilder`, `BaseLLM`, `BaseMemory`, and `BaseTool`.

Business logic remains distributed across reusable components rather than inside workflow implementations.


## Chat Workflow

ChatWorkflow is the first concrete workflow implementation.

It coordinates the interaction between memory, prompt construction, and language model generation through shared abstractions.

The workflow remains focused on orchestration while delegating prompt construction, conversation history, and response generation to dedicated components.

### Responsibilities

- Receive a request.
- Retrieve conversation history from memory.
- Build a prompt using the PromptBuilder.
- Generate a response through the configured LLM.
- Store the conversation in memory.
- Return the generated response.

### Dependencies

- `BaseMemory`
- `PromptBuilder`
- `BaseLLM`


## Agent Workflow

AgentWorkflow provides the foundation for future agent-based execution.

It coordinates prompt generation, memory, language model interaction, and external tool execution through shared abstractions.

### Responsibilities

- Receive a request.
- Retrieve conversation history from memory.
- Build a prompt using the PromptBuilder.
- Generate a response through the configured LLM.
- Execute external tools.
- Store the conversation in memory.
- Return the generated response.

### Dependencies

- `PromptBuilder`
- `BaseMemory`
- `BaseLLM`
- `BaseTool`



## RAG Workflow

RAGWorkflow augments user requests with retrieved context before generating a response.

It coordinates retrieval, prompt construction, language model generation, and conversation memory through shared abstractions.

### Responsibilities

- Receive a request.
- Retrieve relevant document chunks.
- Build a retrieval-augmented prompt.
- Generate a response through the configured LLM.
- Store the conversation in memory.
- Return the generated response.

### Dependencies

- BaseRetriever
- PromptBuilder
- BaseLLM
- BaseMemory



## Request & Response

The system communicates using two shared domain models.

### Request

Represents the user's input together with any metadata required to process it.

### Response

Represents the final output produced by the workflow.

Keeping Request and Response as shared models provides a consistent interface across all workflows.


## LLM

The assistant communicates with language models through a shared abstraction.

### BaseLLM

`BaseLLM` defines the common contract implemented by all language model providers.

The core system depends only on this abstraction, allowing providers to be replaced without affecting the application architecture.

### Implementations

Current implementations:

- MockLLM

Future implementations may include:

- LocalLLM
- RemoteLLM

### MockLLM

MockLLM is a lightweight implementation of the BaseLLM interface intended for development and testing.

It provides deterministic responses without relying on external language model providers.



## Embedder

Embedders generate vector representations of text for semantic search and retrieval.

The assistant communicates with embedding providers through the `BaseEmbedder` abstraction.

### Implementations

Current implementations:

- MockEmbedder

Future implementations may include:

- SentenceTransformerEmbedder
- OpenAIEmbedder
- VoyageAIEmbedder

### MockEmbedder

MockEmbedder is a lightweight implementation of the `BaseEmbedder` interface intended for development and testing.

It provides deterministic embeddings without relying on external embedding providers.



## Prompt Builder

The `PromptBuilder` component is responsible for constructing prompts from reusable templates.

Prompt generation is isolated from workflow logic to keep workflows focused on orchestration.

It combines conversation history and user input to produce prompts for language model generation.

Prompt templates are stored separately from application logic, making prompt construction reusable and easier to maintain across workflows.



## Memory

Memory is responsible for storing and retrieving conversation history independently from workflow logic.

Workflows interacts with memory through the `BaseMemory` abstraction to retrieve conversation history and store newly generated messages.

The assistant communicates with memory implementations through the `BaseMemory` abstraction.

### Implementations

Current implementations:

- MockMemory

Future implementations may include:

- FileMemory
- SQLiteMemory
- RedisMemory

### MockMemory

MockMemory is a lightweight in-memory implementation intended for development and testing.

It stores conversation history without relying on external storage systems.



## Text Splitter

TextSplitter is responsible for dividing documents into overlapping chunks before retrieval.

Chunking is isolated from retrieval and embedding logic to keep each component focused on a single responsibility.

The generated chunks become the input for the embedding pipeline.



## Documents

Documents represent shared retrieval models used throughout the assistant.

They provide a provider-independent representation of textual content and serve as the foundation for ingestion, chunking, embedding, and retrieval.

### Models

Current models:

- `Document`
- `Chunk`

Future extensions may include:

- Metadata
- Source information
- Chunk relationships
- Embedding references



## Vector Store

VectorStore provides a common abstraction for storing and searching embeddings independently from retrieval workflows.

The assistant communicates with vector storage implementations through the `BaseVectorStore` abstraction.

### Implementations

Current implementations:

- MockVectorStore

Future implementations may include:

- ChromaVectorStore
- FAISSVectorStore
- PGVectorStore
- PineconeVectorStore

### MockVectorStore

MockVectorStore is a lightweight in-memory implementation intended for development and testing.

It stores chunks and returns deterministic search results without relying on external vector databases.



## Retriever

Retriever is responsible for retrieving the most relevant document chunks for a user query.

It combines embedding generation and vector search through shared abstractions while remaining independent from concrete providers.

The assistant communicates with retrieval implementations through the `BaseRetriever` abstraction.

### Implementations

Current implementations:

- MockRetriever

Future implementations may include:

- SemanticRetriever
- HybridRetriever
- MultiVectorRetriever

### Dependencies

- BaseEmbedder
- BaseVectorStore

### MockRetriever

MockRetriever is a lightweight implementation intended for development and testing.

It retrieves document chunks by combining the configured embedder and vector store without relying on external retrieval systems.



## Tools

Tools provide a common interface for executing external capabilities independently from workflow logic.

Workflows communicate with tools through the `BaseTool` abstraction.

### Implementations

Current implementations:

- MockTool

Future implementations may include:

- CalculatorTool
- SearchTool
- WeatherTool
- FileTool

### MockTool

MockTool is a lightweight implementation of the `BaseTool` interface intended for development and testing.

It provides deterministic responses without relying on external services.



## Dependency Graph

```text
                    Assistant
                         │
                         ▼
                   BaseWorkflow
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
 ChatWorkflow   RAGWorkflow   AgentWorkflow
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
 BaseRetriever    PromptBuilder      BaseMemory
        │                                 │
   ┌────┴────┐                            │
   ▼         ▼                            │
BaseEmbedder BaseVectorStore              │
                                          ▼
                                      BaseLLM
```



## Request Lifecycle

```text
 User
   │
   ▼
Request
   │
   ▼
Assistant
   │
   ▼
Workflow
   │
   ├────────► Memory
   ├────────► Retriever
   ├────────► PromptBuilder
   │               │
   │               ▼
   ├────────► Tools
   └────────► LLM
                 │
                 ▼
             Response
                 │
                 ▼
               User
```



## Document Ingestion Pipeline

The ingestion pipeline prepares external knowledge sources for retrieval.

```text
Document Source
      │
      ▼
Loader
      │
      ▼
Document
      │
      ▼
Text Splitter
      │
      ▼
Chunk
      │
      ▼
Embedder
      │
      ▼
Vector Store
```



## Future Extensions

- Planning
- Function Calling
- MCP
- Multi-Agent
- Voice
- Vision
- Web UI



## Architecture Decisions

- ADR-0001 Project Philosophy
- ADR-0002 Provider Independence

## Current Status

This document represents the initial high-level architecture and will evolve as the project grows.