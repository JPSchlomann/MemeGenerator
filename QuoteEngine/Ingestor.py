"""Main ingestor class. Encapsulation of all ingetors."""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """Realize abstract call IngestorInterface.

    Encapsulates all the ingestors to provide one interface
    to load any supported file type.
    """

    ingestors = [TXTIngestor, CSVIngestor, DOCXIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        """Use the correct ingestor fo the provided file type.

        : return: Quotes
        """
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
