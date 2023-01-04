"""Abstract base class."""
from abc import ABC, abstractmethod

from QuoteMode import Quote


class IngestorInterface(ABC):
    compatible_files = []

    @classmethod
    def can_ingest(cls, path: str):
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str):
        pass
