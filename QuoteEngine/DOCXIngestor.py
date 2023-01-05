from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import Quote

class DOCXIngestor(IngestorInterface):
    compatible_files = ['docx']

    @classmethod
    def parse(cls, path: str):
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = Quote(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
