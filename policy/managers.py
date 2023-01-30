from datetime import datetime
from django.db.models import Manager, Q

from .exceptions import InvalidArgumentError, QuoteAlreadyArchivedError

from .status import Status
from . import models

class QuoteManager(Manager):
    def set_status(self, quote, status):
        if status is None or not isinstance(status, Status):
            raise InvalidArgumentError('status')

        if quote is None or not isinstance(quote, models.Quote):
            raise InvalidArgumentError('quote')

        if quote.status is Status.Archived.value:
            raise QuoteAlreadyArchivedError()

        quote.status = status.value
        quote.save()

    
    def accept_quote(self, quote):
        if quote is None or not isinstance(quote, models.Quote):
            raise InvalidArgumentError('quote')

        if quote.status == Status.Archived.value:
            raise QuoteAlreadyArchivedError()

        self.set_status(quote, Status.Accepted)

    def pay_quote(self, quote):
        if quote is None or not isinstance(quote, models.Quote):
            raise InvalidArgumentError('quote')

        if quote.status == Status.Archived.value:
            raise QuoteAlreadyArchivedError()

        quote.paid = True
        self.set_status(quote, Status.Active)