# ADR-0002 Provider Independence

## Status

Accepted

## Context

The assistant must support multiple language model providers without changing the core application.

Different providers expose different APIs, authentication mechanisms, deployment models, and capabilities.

Depending directly on provider-specific implementations would tightly couple the workflow layer to infrastructure and make future provider replacements more difficult.

## Decision

The system depends only on the `BaseLLM` abstraction rather than concrete provider implementations.

Concrete implementations are responsible for communicating with individual providers.

Examples include:

- MockLLM
- LocalLLM
- RemoteLLM

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