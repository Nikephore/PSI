from django.http import request
from orders.forms import CartAddBookForm, OrderCreateForm
from django.views import generic
from orders.tests_services import FIRSTNAME
from .cart import Cart
from catalog.models import Book
from django.conf import settings
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404


class BaseCart(generic.ListView):
    context_object_name = 'cart_list'
    template_name = 'orders/cart.html'

    def get_queryset(self):
        cart_list = self.request.session[settings.CART_SESSION_ID]
        return cart_list

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
    print('order create')
    if request.method == 'POST':
        print('is post')
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            return render(request, 'orders/created.html', context=None)
    # Cambiar aqui por lo que sea necesario
    return redirect('cart_list')