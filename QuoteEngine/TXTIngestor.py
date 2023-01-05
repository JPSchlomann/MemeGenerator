

from .IngestorInterface import IngestorInterface
from .QuoteModel import Quote

class TXTIngestor(IngestorInterface):
    compatible_files = ['txt']

    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quotes = []
        infile = open(path, 'r')
        for line in infile.readlines():
            body, author = line.split(' - ')
            new_quote = Quote(body, author)
            quotes.append(new_quote)

        return quotes
