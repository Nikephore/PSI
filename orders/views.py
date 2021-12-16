from orders.forms import CartAddBookForm
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
            print("ubidades en views a anyadir " + str(units))
            sl = Book.objects.get(slug=slug)
            print(str(sl.id))
            cart.add(sl, units)
    return redirect('cart_list')

def cart_remove(request, slug):
    cart = Cart(request)
    if request.method == 'GET':
    # Procesar el formulario para obtener la unidades y anyadirlas
        form = CartAddBookForm(request.GET)
        if form.is_valid():
            units = form.cleaned_data.get('quantity')
            sl = (get_object_or_404(Book, slug=slug))
            print(str(sl.id))
            cart.remove(sl, quantity=units)
    return redirect('cart_list')