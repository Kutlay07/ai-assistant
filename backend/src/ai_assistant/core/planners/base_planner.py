from abc import ABC, abstractmethod

from ..models import Request, Plan


class BasePlanner(ABC):
    
    @abstractmethod
    def create_plan(self, request: Request) -> Plan:
        """Create an execution plan for the given request"""
        pass