from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .TXTIngestor import TXTIngestor
from .CSVIngestor import CSVIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor

class Ingestor(IngestorInterface):
    ingestors = [TXTIngestor, CSVIngestor, DOCXIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
