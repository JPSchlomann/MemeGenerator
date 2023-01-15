"""Ingest .pdf files.

The PDFIngestor class utilizes the subprocess module to call the
pdftotext CLI utility—creating a pipeline that converts PDFs to
text and then ingests the text.
"""

from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Ingestor for .pdf documents."""

    compatible_files = ['pdf']

    @classmethod
    def parse(cls, path: str):
        """Extract quotes from .pdf documents.

        : return: Quotes.
        """
        if not cls.can_ingest(path):
            raise Exception('Cannot load file: Unsupported file type')

        tmp = f'./tmp_{random.randint(0,1000000)}.txt'
        call = subprocess.call(r"pdftotext -layout {} {}".format(path, tmp),
                               shell=True)

        quotes = []
        file_ref = open(tmp, "r")
        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)

        return quotes
