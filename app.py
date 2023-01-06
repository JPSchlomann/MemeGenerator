import random
import os
import requests
from flask import Flask, render_template, abort, request

from MemeEngine import MemeEngine
from QuoteEngine import CSVIngestor, DOCXIngestor, TXTIngestor, Ingestor

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesCSV.csv']
                   #'./_data/DogQuotes/DogQuotesPDF.pdf', !!!!!!!!!!!!!!!!!!!

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []
    for quote_file in quote_files:
        new_quotes = Ingestor.parse(quote_file)
        quotes.extend(new_quotes)

    images_path = "./_data/photos/dog/"
    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    img_names = os.listdir(images_path)
    imgs = []
    for img_name in img_names:
        img = images_path + img_name
        imgs.append(img)

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array
    img = imgs[random.randint(0, len(imgs)-1)]
    quote = quotes[random.randint(0, len(quotes)-1)]
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    from param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    quote_body = request.form['body']
    quote_author = request.form['author']

    img_url = request.form['image_url']
    img_content = requests.get(img_url,stream=True).content
    tmp_filename = f'./tmp_{random.randint(0,100)}.png'

    with open(tmp_filename, 'wb') as img:
       img.write(img_content)

    # Use the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    meme.make_meme(tmp_filename, quote_body, quote_author)

    # Remove the temporary saved image.
    os.remove(tmp_filename)

    path = None

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
