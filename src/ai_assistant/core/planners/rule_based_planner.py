from ..models import Plan, Request
from .base_planner import BasePlanner


class RuleBasedPlanner(BasePlanner):
    """Creates execution plans using simple rule-based heuristics."""
    
    SEARCH_KEYWORDS = (
        "search",
        "find",
        "lookup",
        "rag",
    )
    
    CALCULATION_KEYWORDS = (
        "calculate",
        "math",
        "solve",
    )
    
    def create_plan(
        self,
        request: Request,
    ) -> Plan:
        
        message = request.input.lower()
        
        steps: list[str] = []
        
        if self._requires_search(message):
            steps.append(
                "Search relevant information"
            )
            
        if self._requires_calculation(message):
            steps.append(
                "Perform calculation"
            )
            
        steps.append(
            "Generate final response"
        )
        
        return Plan(
            steps=steps,
        )
        
    def _requires_search(
        self,
        message: str,
    ) -> bool:
        
        return any(
            keyword in message
            for keyword in self.SEARCH_KEYWORDS
        )
        
    def _requires_calculation(
        self,
        message: str,
    ) -> bool:
        
        return any(
            keyword in message
            for keyword in self.CALCULATION_KEYWORDS
        )