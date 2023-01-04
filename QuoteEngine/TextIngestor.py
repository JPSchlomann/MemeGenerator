

from .IngestorInterface import IngestorInterface
from .QuoteMode import Quote

class TextIngestor(IngestorInterface):
    compatible_files = ['txt']

    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quote = []


        return quote
