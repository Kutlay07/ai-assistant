# ADR-0002: Provider Independence

## Status

Accepted

---

## Context

The assistant must support different infrastructure providers without requiring changes to the core application logic.

Language model providers may differ in:

- API design
- Authentication mechanisms
- Deployment strategies
- Available capabilities
- Operational requirements

Direct dependency on provider-specific implementations would tightly couple workflows to external infrastructure and make future integrations more difficult.

To avoid this coupling, the system introduces abstraction layers that define stable contracts between the core architecture and external providers.

For language models, `BaseLLM` defines the common interface through a shared generation contract.

Workflows interact only with these abstractions and remain unaware of concrete provider implementations.

---

## Decision

The system depends on abstractions rather than concrete provider implementations.

For language models:

- Workflows depend on `BaseLLM`.
- Providers implement the `BaseLLM` contract.
- Provider-specific logic remains isolated inside implementations.

Current implementations include:

- `MockLLM` — Testing and development
- `GroqProvider` — Hosted inference provider
- `LocalProvider` — Local model inference foundation

Future integrations may include:

- OpenAI
- Anthropic
- Ollama
- Other compatible providers

The same architectural principle is expected to apply to other external systems such as:

- Embedding providers
- Vector databases
- Memory backends
- Tool providers

---

## Consequences

### Advantages

- Provider independence
- Reduced coupling between core logic and infrastructure
- Easier testing through mock implementations
- Simpler provider replacement
- Better long-term maintainability

### Trade-offs

- Additional abstraction layers
- Slight increase in initial implementation complexity
- More interfaces require maintenance over time