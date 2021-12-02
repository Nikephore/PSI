from orders.forms import CartAddBookForm
from .cart import Cart
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
        cart.add(obtener_libro, quantity=units)
        return redirect('cart_list')
    return redirect('cart_list')
