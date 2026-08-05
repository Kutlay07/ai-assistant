from ..models import Plan, Request
from .base_planner import BasePlanner


class MockPlanner(BasePlanner):

    def create_plan(self, request: Request) -> Plan:
        return Plan(
            steps=[
                f"Process request: {request.input}",
            ]
        )