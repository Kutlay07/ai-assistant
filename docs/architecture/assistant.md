# Assistant

## Overview

The Assistant is the primary entry point of the application.

It coordinates request execution by delegating work to the configured workflow while remaining independent from workflow implementation details.

The Assistant intentionally contains no business logic. It serves only as the orchestration layer between the API and workflow system.



## Responsibilities

- Receive incoming requests.
- Delegate execution to the configured workflow.
- Return the generated response.
- Validate and execute registered tools through the `ToolRegistry`.



## Non-Responsibilities

The Assistant is **not** responsible for:

- Building prompts
- Managing conversation memory
- Performing document retrieval
- Calling language model providers
- Planning execution steps
- Executing workflow logic

These responsibilities belong to dedicated workflow and service components.



## Dependencies

The Assistant depends on:

- `BaseWorkflow`
- `ToolRegistry`
- `ToolCallValidator`



# Workflows

A workflow defines **how** a request is processed.

Different workflows implement different execution strategies while exposing the same public interface through `BaseWorkflow`.

Current workflow implementations include:

- `ChatWorkflow`
- `RAGWorkflow`
- `AgentWorkflow`

All workflows coordinate reusable components instead of implementing business logic directly.

Shared abstractions include:

- `PromptBuilder`
- `BaseMemory`
- `BaseLLM`
- `BasePlanner`
- `BaseRetriever`
- `BaseTool`



# Request & Response

The assistant communicates internally using two shared domain models.

## Request

Represents the user's input together with any metadata required for execution.

## Response

Represents the final result produced by the workflow.

Keeping these models shared provides a consistent interface across all workflows.