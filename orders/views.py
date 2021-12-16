from orders.forms import CartAddBookForm
from .cart import Cart
from catalog.models import Book
from django.shortcuts import render, redirect


class BaseCart():
    template_name = 'cart.html'

def cart_add(request, book_slug):
    cart = Cart(request)
    # Procesar el formulario para obtener la unidades y anyadirlas
    form = CartAddBookForm(request)
    if form.is_valid():
        form.save()
        units = form.units
        book = Book.objects.get(book_slug=book_slug)
        cart.add(book, quantity=units)
        return redirect('cart_list')
    return redirect('cart_list')

def cart_remove(request, book_slug):
    cart = Cart(request)
    book = Book.objects.get(book_slug=book_slug)
    cart.remove(book)
    return redirect("cart_list")