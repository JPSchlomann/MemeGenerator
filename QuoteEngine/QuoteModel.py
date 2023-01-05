

class Quote():
    def __init__(self, body, author):
        self.body = str(body)
        self.author = str(author)

    def __repr__(self):
        return f' "{self.body}" - {self.author}'
