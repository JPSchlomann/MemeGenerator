

class QuoteModel():
    def __init__(self, body, author):
        # remove extra quotation marks
        body = body.replace('"','')
        author = author.replace('"','')

        self.body = str(body)
        self.author = str(author)

    def __repr__(self):
        return f' "{self.body}" - {self.author}'
