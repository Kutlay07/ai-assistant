# Memory

## Overview

Memory is responsible for storing and retrieving conversation history independently from workflow logic.

Workflows communicate exclusively through the `BaseMemory` abstraction, allowing memory implementations to be replaced without affecting application behavior.

The assistant remains completely independent from the underlying storage mechanism.



## BaseMemory

`BaseMemory` defines the common interface implemented by all memory providers.

Every implementation is responsible for:

- Persisting conversation history.
- Loading previous messages.
- Appending new messages.
- Returning conversation history.



## Current Implementations

- `MockMemory`
- `FileMemory`



## MockMemory

`MockMemory` is a lightweight in-memory implementation intended for development and testing.

Characteristics:

- Stores messages only in memory.
- No persistence.
- Fast and deterministic.
- Ideal for unit tests.

Conversation history is discarded when the application stops.



## FileMemory

`FileMemory` provides persistent conversation storage using a JSON file.

Characteristics:

- Loads conversation history on startup.
- Saves every new message automatically.
- Persists across application restarts.
- Storage location is configurable through `MEMORY_PATH`.

Conversation history is stored as a JSON array of messages.

Example:

```json
[
    "Hello, I'm Kutlay",
    "Hello Kutlay!",
    "What's my name?",
    "Your name is Kutlay."
]
```

The storage location can be configured through:

```text
MEMORY_PATH=data/conversation.json
```



## Planned Implementations

Future memory providers may include:

- `SQLiteMemory`
- `RedisMemory`

These implementations will continue to expose the same `BaseMemory` interface.