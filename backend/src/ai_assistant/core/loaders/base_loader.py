from abc import ABC, abstractmethod
from pathlib import Path

from ..models import Document


class BaseLoader(ABC):

    @abstractmethod
    def load(self, path: str | Path) -> Document:
        pass