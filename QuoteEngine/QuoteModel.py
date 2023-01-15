"""Class for creating quuotes.

The QuoteModel class contains text fields for body and
author of the Quotes which will be used for the memes.
"""


class QuoteModel():
    """Represent a quote consisting of: Body, Author."""

    def __init__(self, body, author):
        """Crete a new quote.

        :param body: text of quote
        :param author: author of text
        """
        # remove extra quotation marks
        body = body.replace('"', '')
        author = author.replace('"', '')

        self.body = str(body)
        self.author = str(author)

    def __repr__(self):
        """Return a computer-readable string representation of this object."""
        return f' "{self.body}" - {self.author}'
