"""Generate a random captioned image.

The 'generate_meme' function is used to generate a meme
based on user iputs or based on random parameters
"""

import os
import random
import argparse

from QuoteEngine import (CSVIngestor, DOCXIngestor, TXTIngestor,
                         QuoteModel, Ingestor)
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote.

    If any argument is not defined,
    a random selection is used

    :param path: Path to a picture (.jpg or .png)
    :param body: Text of meme
    :param author: Author of text
    :return: The path to the generated meme
    """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        if not os.path.isfile(path):
            raise Exception("\nRequested file cannot be found. "
                            "\nPlease provide complete path "
                            "using single quotes.")
        else:
            img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./static')

    path = meme.make_meme(img, quote.body, quote.author)

    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Provide path,'
                                                 'body and author.')
    parser.add_argument('--path', type=str, default=None,
                        help='path to picture')
    parser.add_argument('--body', type=str, default=None, help='body')
    parser.add_argument('--author', type=str, default=None, help='author')

    args = parser.parse_args()
    print('\n Path of generated meme: ' + generate_meme(args.path, args.body,
                                                        args.author))
