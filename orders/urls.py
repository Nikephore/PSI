from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    url(r'^$', views.BaseCart.as_view(), name='cart_list'),
    url(r'^checkout/$', views.order_process, name='checkout'),
    path(r'cart_add/<slug:slug>', views.cart_add, name='cart_add'),
    path(r'cart_remove/<slug:slug>', views.cart_remove, name='cart_remove'),
    path(r'order_create/', views.order_create, name='order_create'),
]
