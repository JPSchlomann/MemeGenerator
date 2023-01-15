"""Ingest .csv files.

The class depends on the pandas library to complete the defined,
abstract method signatures to parse CSV files.
"""

from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Ingestor for .csv documents."""

    compatible_files = ['csv']

    @classmethod
    def parse(cls, path: str):
        """Extract quotes from .csv documents.

        : return: Quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for idx, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
