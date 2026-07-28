from abc import ABC, abstractmethod

from ..models import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, path: str) -> Document:
        pass