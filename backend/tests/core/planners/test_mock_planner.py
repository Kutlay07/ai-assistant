from ai_assistant.core.models import Request, Plan
from ai_assistant.core.planners import MockPlanner


def test_mock_planner_returns_plan():
    planner = MockPlanner()

    plan = planner.create_plan(
        Request(input="Hello")
    )

    assert isinstance(plan, Plan)


def test_mock_planner_contains_single_step():
    planner = MockPlanner()

    plan = planner.create_plan(
        Request(input="Hello")
    )

    assert len(plan.steps) == 1


def test_mock_planner_uses_request_input():
    planner = MockPlanner()

    plan = planner.create_plan(
        Request(input="Hello")
    )

    assert plan.steps[0] == "Process request: Hello"