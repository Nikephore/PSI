from orders.forms import CartAddBookForm
from .cart import Cart
from catalog.models import Book
from django.shortcuts import render, redirect


def baseCart(request):
    context = None
    return render(request, 'orders/cart.html', context=context)

def cart_add(request, slug):
    cart = Cart(request)
    if request.method == 'POST':
    # Procesar el formulario para obtener la unidades y anyadirlas
        form = CartAddBookForm(request.POST)
        if form.is_valid():
            units = form.cleaned_data.get('quantity')
            sl = (get_object_or_404(Book, slug=slug))
            cart.add(sl, quantity=units)
    return redirect('cart_list')

def cart_remove(request, book_slug):
    cart = Cart(request)
    book = Book.objects.get(book_slug=book_slug)
    cart.remove(book)
    return redirect("cart_list")