"""The class does not depend on any 3rd party library to complete
the defined, abstract method signatures to parse Text files.
"""

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    """Ingestor for .txt documents."""
    
    compatible_files = ['txt']

    @classmethod
    def parse(cls, path: str):
        """Extracts quotes from .txt documents.

        : return: Quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quotes = []
        infile = open(path, 'r', encoding='utf-8-sig')
        for line in infile.readlines():
            body, author = line.split(' - ')
            new_quote = QuoteModel(body, author)
            quotes.append(new_quote)

        return quotes
