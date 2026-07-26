# AI Assistant Architecture

## Overview

This project is a production-ready, provider-independent AI Assistant platform.

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

The Assistant intentionally contains no business logic.tentionally contains no business logic.

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

Chat Workflow is the first concrete workflow implementation.

It processes chat-based requests through the workflow interface and produces responses using the shared Request and Response domain models.

The current implementation prepares the architecture for future LLM integration.


### Responsibilities

- Receive a request from the Assistant.
- Coordinate the execution flow.
- Use the required services.
- Produce a response.

### Workflow Dependencies

Each workflow only depends on the services it requires.

Examples include:

- LLM
- Prompt Builder
- Memory
- Retriever
- Planner
- Tool Manager


## Request & Response

The system communicates using two shared domain models.

### Request

Represents the user's input together with any metadata required to process it.

### Response

Represents the final output produced by the workflow.

Keeping Request and Response as shared models provides a consistent interface across all workflows.


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
- ADR-0002 LLM Abstraction
- ADR-0003 Tool Architecture

## Current Status

This document represents the initial high-level architecture and will evolve as the project grows.