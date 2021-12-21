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
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # If there is no cart create an empty one
            # and save it in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
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
        {'quantity ': 0,
        'price': str(book.price)}
        Store 'price' as a string because a Decimal
        object may not be properlly serialized
        """
        book_id = str(book.id)
        # your code goes here
        if book_id not in self.cart:
            self.cart[book_id] = {'book_id': book_id, 'title': str(book.title), 'slug': str(book.slug), 'quantity': 0, 'price': str(book.price)}
        if update_quantity:
            self.cart[book_id]['quantity'] = int(quantity)
        else:
            self.cart[book_id]['quantity'] += int(quantity)
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, book):
        book_id = str(book.id)
        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    def __iter__(self):
        book_ids = self.cart.keys()
        books = Book.objects.filter(id__in=book_ids)
        for book in books:
            self.cart[str(book.id)]['book'] = book

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_number_items(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
