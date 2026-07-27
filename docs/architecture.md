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
                  │
                  ▼
            Core Services
                  │
                  ▼
         Infrastructure Layer
```



## Core Components

| Component      | Responsibility                   |
| -------------- | -------------------------------- |
| Assistant Core | Coordinate the request lifecycle |
| LLM Layer      | Provider abstraction             |
| Tool System    | Execute external tools           |
| Memory         | Store conversation context       |
| Prompt Builder | Construct prompts                |
| Planner        | Multi-step execution             |
| RAG            | Knowledge retrieval              |


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



## Chat Workflow

ChatWorkflow is the first concrete workflow implementation.

It processes chat requests by coordinating the interaction between the PromptBuilder and the configured LLM implementation.

The workflow remains focused on orchestration while relying on abstractions for prompt construction and language model generation.

### Responsibilities

- Receive a request.
- Retrieve conversation history from memory.
- Build a prompt using the PromptBuilder.
- Generate a response through the configured LLM.
- Store the conversation in memory.
- Return the generated response.

### Dependencies

- PromptBuilder
- BaseLLM



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



## Prompt Builder

PromptBuilder is responsible for constructing prompts from incoming requests.

Prompt generation is isolated from workflow logic to keep workflows focused on orchestration.

The initial implementation returns the user's input directly and serves as the foundation for future prompt templating and context composition.



## Memory

Memory is responsible for storing and retrieving conversation history independently from workflow logic.

ChatWorkflow interacts with memory through the `BaseMemory` abstraction to retrieve conversation history and store newly generated messages.

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



## Dependency Graph

```text
                Assistant
                     │
                     ▼
                BaseWorkflow
                     │
      ┌──────────────┼──────────────┐
      │              │              │
ChatWorkflow   RAGWorkflow   AgentWorkflow
      │              │              │
      ▼              ▼              ▼
 PromptBuilder  Retriever      Planner
      │              │              │
      └──────┬───────┴───────┬──────┘
             ▼               ▼
          Memory       Tool Manager
                 \      /
                  \    /
                   ▼  ▼
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
   ▼
Response
   │
   ▼
 User
```


## Future Extensions

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