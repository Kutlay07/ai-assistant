# Language Models

## Overview

Language models are responsible for generating responses from prompts.

The assistant communicates with language model providers exclusively through the `BaseLLM` abstraction, making the system provider-independent.

This allows providers to be replaced without changing workflow implementations.



## BaseLLM

`BaseLLM` defines the common interface implemented by every language model provider.

All providers expose the same contract while hiding provider-specific implementation details.

The assistant depends only on this abstraction.



## Current Implementations

- `GroqProvider`
- `MockLLM`
- `LocalProvider`



## GroqProvider

`GroqProvider` connects the assistant to Groq's OpenAI-compatible API.

Characteristics:

- Production-ready
- Supports text generation
- Supports streaming responses
- Compatible with OpenAI-style APIs



## MockLLM

`MockLLM` is a lightweight implementation intended for development and testing.

Characteristics:

- Deterministic responses
- No external dependencies
- Fast execution
- Ideal for unit tests



## LocalProvider

`LocalProvider` is reserved for future support of locally hosted language models.

Potential future integrations include:

- Ollama
- vLLM
- llama.cpp
- Hugging Face Transformers

All local providers will continue to implement the `BaseLLM` interface.