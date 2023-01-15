"""The class depends on the python-docx library to complete the
defined, abstract method signatures to parse DOCX files.
"""

from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """Ingestor for .docx documents."""

    compatible_files = ['docx']

    @classmethod
    def parse(cls, path: str):
        """Extracts quotes from .docx documents.

        : return: Quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
