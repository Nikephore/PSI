from django.http import request
from orders.forms import CartAddBookForm, OrderCreateForm
from orders.tests_services import FIRSTNAME
from .cart import Cart
from catalog.models import Book
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


def BaseCart(request):
    context = None
    return render(request, 'orders/cart.html', context=context)

def cart_add(request, slug):
    cart = Cart(request)
    if request.method == 'POST':
    # Procesar el formulario para obtener la unidades y anyadirlas
        form = CartAddBookForm(request.POST)
        if form.is_valid():
            units = form.cleaned_data.get('quantity')
            sl = Book.objects.get(slug=slug)
            cart.add(sl, units)
    return redirect('cart_list')

def cart_remove(request, slug):
    cart = Cart(request)
    if request.method == 'GET':
    # Procesar el formulario para obtener la unidades y anyadirlas
        sl = Book.objects.get(slug=slug)
        cart.remove(sl)
    return redirect('cart_list')

def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            form.save()
            render(request, 'orders/created.html', context=None)
    # Cambiar aqui por lo que sea necesario
    return redirect('cart_list')