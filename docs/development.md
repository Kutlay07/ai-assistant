# Development Workflow

## Overview

This document describes the development workflow followed throughout the AI Assistant project.

The goal is to keep development incremental, architecture-driven, and production-oriented while maintaining clear documentation and engineering discipline.

---

# Development Process

Every feature follows the same development cycle.

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
Pull Request
   ↓
Review
   ↓
Merge
```

This process encourages thoughtful design before implementation and keeps the repository organized as the system evolves.

---

# Git Workflow

Development follows a simple GitHub-based workflow.

Guidelines:

- Work on one logical task at a time.
- Create issues before implementing features.
- Use dedicated branches for changes.
- Keep commits small and focused.
- Write meaningful commit messages.
- Submit pull requests for review.
- Merge only after tests and documentation are complete.

---

# Branch Naming

Branches should describe the purpose of the change.

Examples:

```text
feature/persistent-memory
feature/agent-workflow
docs/reorganize-documentation
fix/memory-loading-error
```

---

# Commit Convention

The project follows the Conventional Commits specification.

Common commit types:

- `feat` – New features
- `fix` – Bug fixes
- `docs` – Documentation changes
- `refactor` – Code improvements without behavior changes
- `test` – Test additions or improvements
- `chore` – Maintenance and configuration

Examples:

```text
feat(memory): add persistent file storage

docs: reorganize architecture documentation

test(agent): add workflow integration tests
```

---

# Documentation

Documentation is treated as part of the implementation process.

Guidelines:

- Keep documentation synchronized with code changes.
- Record architectural decisions using ADRs.
- Update architecture documents when responsibilities change.
- Explain why decisions were made, not only what was implemented.

---

# Testing

Testing is introduced incrementally as the project grows.

Principles:

- Prefer isolated unit tests.
- Test public behavior instead of internal implementation details.
- Add integration tests for workflows and major features.
- Ensure tests pass before merging changes.

---

# Running the API

The project includes a FastAPI application for local development.

Start the development server:

```bash
python -m fastapi dev src/ai_assistant/api/main.py
```

API documentation:

```
http://127.0.0.1:8000/docs
```

ReDoc documentation:

```
http://127.0.0.1:8000/redoc
```

---

# Releases

Releases are milestone-based rather than commit-based.

Each release represents a meaningful stage in the project's evolution.

A release should include:

- Completed features
- Updated documentation
- Passing tests
- Stable architecture

---

# Project Philosophy

The project's engineering principles are documented separately.

See:

- ADR-0001 — Project Philosophy
- ADR-0002 — Provider Independence