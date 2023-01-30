
class InvalidArgumentError(Exception):
    def __init__(self, argument_name):
        message = f'The argument {argument_name} is invalid'
        super().__init__(message)


class QuoteAlreadyArchivedError(Exception):
    def __init__(self, quote):
        message = f'The quote with ID: {quote.id} is already archived.'
        super().__init__(message)

