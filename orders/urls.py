from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    url(r'^$', views.BaseCart, name='cart_list'),
    path(r'cart_add/<slug:slug>', views.cart_add, name='cart_add')
]
