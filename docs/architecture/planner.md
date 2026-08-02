# Planner

## Overview

Planners are responsible for determining **what should be done** before execution begins.

Rather than executing tasks directly, planners generate an execution plan that workflows consume step by step.

This separation keeps planning independent from execution and allows different planning strategies to evolve without affecting workflow implementations.



## BasePlanner

`BasePlanner` defines the common interface implemented by every planner.

Each planner receives a request and returns a structured `Plan`.

The assistant communicates exclusively through this abstraction.



## Plan

A `Plan` represents an ordered collection of execution steps.

Each step describes a unit of work that the workflow processes sequentially.

This allows workflows to focus on orchestration while planners remain responsible for decision making.



## Current Implementations

- `MockPlanner`
- `RuleBasedPlanner`



## MockPlanner

`MockPlanner` is intended for development and testing.

Characteristics:

- Deterministic plans
- No decision logic
- Ideal for unit tests



## RuleBasedPlanner

`RuleBasedPlanner` creates execution plans using predefined planning rules.

Characteristics:

- Lightweight planning
- No language model required
- Deterministic behavior
- Easy to extend

Current planning rules include:

- Conversation requests
- Search requests
- Calculation requests



## Planned Implementations

Future planners may include:

- `LLMPlanner`
- `ReActPlanner`
- `TreeOfThoughtPlanner`
- `PlanningAgent`



## Planning Flow

```text
Request
   │
   ▼
BasePlanner
   │
   ▼
Plan
   │
   ▼
Workflow
   │
   ▼
Execution
```