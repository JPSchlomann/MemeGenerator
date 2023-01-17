# Motivational Meme Generator

## Overview of the project
In this project a 'meme generator' is built – a multimedia application to
dynamically generate memes, including an image with an overlaid quote.

The 'meme generator' loads quotes from a variety of filetypes (PDF,
Word Documents, CSVs, Text files) and generates memes by loading, manipulating
and saving images. Dynamic user input through a command-line tool and a web
service is possible.

## Seeting up and running the program
### Preconditions
- All dependencies are listed in the file 'requirements.txt'

### Generate Memes from CLI
- In order to generate memes from the command line, please run 'main.py'
- Three optional arguments are possible:
  - '--path': The path to the picture on which a quote should be drawn
  - '--body': The text body of the quote
  - '--author' The author of the quote
- When no arguments are provided, random choices of pictures and quotes are used
which can be found in the '_data' folder
- After the meme is generated, the path to the meme is printed in the CLI

### Generate Memes via Flask app
- In order to generate memes by interaction in a browser please run 'app.py'
- The server address will be shown in the CLI
- This address is used to start the meme generator in a browser
- The 'Random' button generates random memes based on the pictures and quotes
in the '_data' folder
- The 'Creator' button leads to another menu where pictures from the Internet
can be used for memes (url needed). The individual body and the author of the
quote can be provided by the user
- After the meme is generated, the path to the meme is printed in the CLI

## Roles-and-responsibilities
The project is based on two modules:
- The QuoteEngine for extracting and preparing quotes from different filetypes
- The MemeEngine for image captioning

### QuoteEngine
Several Ingestors are needed to extract quotes from different data-types:
- .docx: DOCXIngetor.py
- .csv: CSVIngestor.py
- .pdf: PDFIngestor.py
- .txt: TXTIngestor

The absract class 'IngestorInterface' provides the blueprint for each ingestor. The class 'Ingestor' realizes the IngestorInterface and the correct ingestor for each filetype is used to generate quotes, which are defined in the class 'QuoteModel'.

### MemeEngine
This module is used to generate a meme using the quotes from the QuoteEngine. An image is loaded, transformed and a caption is added.
After this, the generated meme is saved. Inside './MemeEngine/fonts' the relevant data for the font of the text is stored.

### Dependencies
Both the CLI (main.py) and the Flask server (app.py) are using the QuoteEngine and the MemeEngine.
First a quote is generated via the QuoteModel (called by the main.py or app.py) and then this quote is forwarded (again by main.py or app.py) to the MemeEngine.
