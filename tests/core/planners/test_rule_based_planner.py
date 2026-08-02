from ai_assistant.core.models import Request
from ai_assistant.core.planners import RuleBasedPlanner


def test_search_request_creates_search_plan():
    planner = RuleBasedPlanner()

    plan = planner.create_plan(
        Request(input="Search FastAPI documentation")
    )

    assert plan.steps == [
        "Search relevant information",
        "Generate final response",
    ]


def test_calculation_request_creates_calculation_plan():
    planner = RuleBasedPlanner()

    plan = planner.create_plan(
        Request(input="Calculate 2 + 2")
    )

    assert plan.steps == [
        "Perform calculation",
        "Generate final response",
    ]


def test_search_and_calculation_request():
    planner = RuleBasedPlanner()

    plan = planner.create_plan(
        Request(input="Search and calculate")
    )

    assert plan.steps == [
        "Search relevant information",
        "Perform calculation",
        "Generate final response",
    ]


def test_regular_chat_creates_response_only_plan():
    planner = RuleBasedPlanner()

    plan = planner.create_plan(
        Request(input="Hello")
    )

    assert plan.steps == [
        "Generate final response",
    ]