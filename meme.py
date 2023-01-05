import os
import random
import argparse

from QuoteEngine import CSVIngestor, DOCXIngestor, TXTIngestor, QuoteModel
from MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path # original: img = path[0]


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

    meme = MemeEngine('./outfiles')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    body_dflt = 'blablabl'
    author_dflt = 'Goethe'
    parser = argparse.ArgumentParser(description = 'Provide path, body and author.')
    parser.add_argument('--path', type=str, default = None, help = 'path to picture')
    parser.add_argument('--body', type=str, default = body_dflt, help = 'body')
    parser.add_argument('--author', type=str, default = author_dflt, help = 'author')

    args = parser.parse_args()
    #print('input path: ' + args.path)
    print(generate_meme(args.path, args.body, args.author))
    #generate_meme(args.path, args.body, args.author)
