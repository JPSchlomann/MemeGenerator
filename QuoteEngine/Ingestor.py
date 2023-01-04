
from .TextIngestor import TextIngestor

class Ingestor(IngestorInterface):
    ingestors = [TextIngestor]

    @classmethod
    def parse(cls, path):
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
