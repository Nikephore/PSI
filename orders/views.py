import datetime

from orders.forms import CartAddBookForm, OrderCreateForm
from django.views import generic
from .cart import Cart
from catalog.models import Book
from django.conf import settings
from django.shortcuts import render, redirect
from .models import Order, OrderItem


class BaseCart(generic.ListView):
    context_object_name = 'cart_list'
    template_name = 'orders/cart.html'

    def get_queryset(self):
        cart_list = self.request.session[settings.CART_SESSION_ID]
        return cart_list


def order_created(request):
    return render(request, "orders/checkout.html", context=None)


def cart_add(request, slug):
    cart = Cart(request)
    if request.method == 'POST':
        # Procesar el formulario para obtener la unidades y anyadirlas
        form = CartAddBookForm(request.POST)
        if form.is_valid():
            units = int(form.cleaned_data.get('quantity'))
            item = Book.objects.get(slug=slug)
            cart.add(item, units)
        return redirect('cart_list')
    return redirect('cart_list')


def cart_remove(request, slug):
    cart = Cart(request)
    if request.method == 'GET':
        # Procesar el formulario para obtener la unidades y anyadirlas
        sl = Book.objects.get(slug=slug)
        cart.remove(sl)
    return redirect('cart_list')


def cart_clear(request):
    cart = Cart(request)
    cart.clear()

    return redirect('home')


def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        return render(request, 'orders/checkoutform.html', context={'form': form})


def order_process(request):
    fn = request.POST['first_name']
    ln = request.POST['last_name']
    e = request.POST['email']
    a = request.POST['address']
    c = request.POST['city']
    pc = request.POST['postal_code']

    orde = Order.objects.create(
        first_name=fn,
        last_name=ln,
        email=e,
        address=a,
        city=c,
        postal_code=pc,
        created=datetime.date.today(),
        updated=datetime.date.today(),
        paid=True
    )
    orde.save()

    cart = Cart(request)

    for item in cart.__iter__():

        bo = Book.objects.get(id=item['book_id'])
        order = Order.objects.get(id=orde.id)
        q = item['quantity']
        p = item['price']
        oi = OrderItem.objects.create(
            book=bo,
            order=order,
            quantity=q,
            price=p
        )
        oi.save()

    cart.clear()

    return redirect('order_created')
