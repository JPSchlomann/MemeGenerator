# Motivational Meme Generator

## Overview of the project
In this project a "meme generator" is built – a multimedia application to
dynamically generate memes, including an image with an overlaid quote.

The "meme generator" loads quotes from a variety of filetypes (PDF,
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
- if no arguments are provided random choices of pictures and quotes are used
which can be found in the '_data' folder
- After the meme is generated the path to the meme is printed on the CLI

### Generatoe Memes via Flask app
- Run 'app.py'
- The server address will be shown in the CLI
- This address is used to start the meme generator in a browser
- The 'Random' button generates random memes based on the pictures and quotes
in the '_data' folder
- The 'Creator' button leads to another menu where pictures from the Internet
can be used for memes (url needed). The individual body and the author of the
quote can be provided by the user 

## Roles-and-responsibilities of all sub-modules including dependencies
