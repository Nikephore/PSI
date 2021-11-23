from decimal import Decimal
from django.conf import settings
from catalog.models import Book


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        if request.session[settings.CART_SESSION_ID]
        does not exist create one
        Important: Make a copy of request.session[
        settings.CART_SESSION_ID]
        do not manipulate it directly
        request.session is not a proper
        dictionary and
        direct manipulation will produce
        weird results
        """
        # request session is the only variable
        # that persists between two http accesses
        # from the same client

        self.session = request.session
        cart = self.session.get(settings.
                                CART_SESSION_ID)
        if not cart:
            # If there is no cart create an empty one
            # and save it in the session
            cart = self.session[settings.
                                CART_SESSION_ID] = {}
            self.cart = cart

    def add(self, book, quantity=1, update_quantity=False):
        """
        Add a book to the cart or update quantity if
        book exists. Note , use strings as keys of the
        dictionary since session use JSON module
        to serialize dictionaries and JSON
        many not supports keys that are not strings ,
        For each book store only the ID (as key)
        and a dictionary
        with the price and quantity as value
        {’quantity ’: 0,
        ’price ’: str(book.price)}
        Store ’price’ as a string because a Decimal
        object may not be properlly serialized
        """
        book_id = str(book.id)
        # your code goes here
