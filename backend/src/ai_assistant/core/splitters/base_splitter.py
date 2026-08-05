from abc import ABC, abstractmethod

from ..models import Chunk, Document


class BaseSplitter(ABC):

    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        pass