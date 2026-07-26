# ADR-0002 Provider Independence

## Status

Accepted


## Context

The assistant must support multiple language model providers without changing the core application.

Different providers expose different APIs, authentication mechanisms, deployment models, and capabilities.

Depending directly on provider-specific implementations would tightly couple the workflow layer to infrastructure and make future provider replacements more difficult.

`BaseLLM` defines the common interface for language model providers through a shared generation contract.

Workflows interact only with this interface and never with provider-specific implementations.


## Decision

The system depends only on the `BaseLLM` abstraction rather than concrete provider implementations.

Concrete implementations are responsible for communicating with individual providers.

Examples of implementations include:

- MockLLM (testing)
- LocalLLM (local inference)
- RemoteLLM (hosted providers)

Provider-specific implementations such as OpenAI, Anthropic, or Ollama can be implemented behind these abstractions.

Workflows interact only with the abstraction and remain unaware of provider-specific details.

## Consequences

### Advantages

- Provider independence
- Dependency inversion
- Easier testing through MockLLM
- Improved maintainability
- Easier future integrations

### Trade-offs

- Additional abstraction layer
- Slight increase in implementation complexity