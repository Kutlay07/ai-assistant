from abc import ABC, abstractmethod


class BaseTool(ABC):

    @abstractmethod
    def execute(self, query: str) -> str:
        pass