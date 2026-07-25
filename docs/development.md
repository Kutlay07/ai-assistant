# Development Workflow

## Overview

This document describes the development workflow followed throughout the AI Assistant project.

The goal is to keep development incremental, well-documented, and architecture-driven while maintaining production-quality engineering practices.

---

## Development Process

Every feature should follow the same development cycle.

```text
Issue
   ↓
Architecture Discussion
   ↓
Implementation
   ↓
Testing
   ↓
Documentation
   ↓
Commit
   ↓
Close Issue
```

This process encourages thoughtful design before implementation and keeps the repository organized as it grows.

---

## Git Workflow

Development follows a simple and consistent Git workflow.

- Work on one logical task at a time.
- Keep commits small and focused.
- Write meaningful commit messages.
- Push changes frequently.
- Close issues only after implementation, testing, and documentation are complete.

---

## Commit Convention

The project follows the Conventional Commits specification.

Common commit types include:

- `feat` – New features
- `fix` – Bug fixes
- `docs` – Documentation
- `refactor` – Code improvements without changing behavior
- `test` – Tests
- `chore` – Maintenance and project configuration

Examples:

```text
feat(llm): add Groq provider
docs: add architecture overview
refactor(memory): simplify conversation storage
test(tools): add calculator tests
```

---

## Documentation

Documentation is treated as part of the project, not as an afterthought.

Guidelines:

- Keep documentation synchronized with implementation.
- Record important architectural decisions as ADRs.
- Update architecture documents whenever the system evolves.
- Prefer explaining why a decision was made, not only what was implemented.

---

## Testing

Testing is introduced incrementally as the project grows.

General principles:

- Prefer small and isolated unit tests.
- Test public behavior rather than implementation details.
- Add tests whenever practical for new functionality.

---

## Releases

Releases are milestone-based rather than commit-based.

Each release should represent a meaningful stage in the project's evolution instead of a collection of unrelated commits.

---

## Project Philosophy

The project's engineering philosophy is documented separately.

See:

- ADR-0001 — Project Philosophy