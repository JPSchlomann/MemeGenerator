"""Implements an abstract base class for all specific Ingestors."""

from abc import ABC, abstractmethod

from .QuoteModel import QuoteModel


class IngestorInterface(ABC):
    """An Abstract base class for all specific Ingestors."""

    compatible_files = []

    @classmethod
    def can_ingest(cls, path: str):
        """verify if the file type is compatible with the ingestor class"""
        ext = path.split('.')[-1]
        return ext in cls.compatible_files

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> [QuoteModel]:
        """parsing the file content and outputting it to a Quote object"""
        pass
