"""Interface with web resources using flask and requests."""

import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine
from QuoteEngine import CSVIngestor, DOCXIngestor, TXTIngestor, Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources.

    :return: quotes and images
    """
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesCSV.csv',
                   './_data/DogQuotes/DogQuotesPDF.pdf']

    # Ingestor class is used to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        new_quotes = Ingestor.parse(quote_file)
        quotes.extend(new_quotes)

    images_path = "./_data/photos/dog/"
    # Find allvimages within the images_path directory
    img_names = os.listdir(images_path)
    imgs = []
    for img_name in img_names:
        img = images_path + img_name
        imgs.append(img)

    return quotes, imgs


# call setup
quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    # Select a random image from imgs array
    img = imgs[random.randint(0, len(imgs)-1)]
    # Select a random quote from the quotes array
    quote = quotes[random.randint(0, len(quotes)-1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme.

    :return: calling render_template
    """
    # Save the image from the image_url
    # to a temp local file.
    img_url = request.form['image_url']
    img_content = requests.get(img_url, stream=True).content
    tmp_filename = f'./tmp_{random.randint(0,100)}.png'

    with open(tmp_filename, 'wb') as img:
        img.write(img_content)

    # Generate a meme using the temp file and the body
    # and author form paramaters.
    quote_body = request.form['body']
    quote_author = request.form['author']
    path = meme.make_meme(tmp_filename, quote_body, quote_author)

    # Remove the temporary saved image.
    os.remove(tmp_filename)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
