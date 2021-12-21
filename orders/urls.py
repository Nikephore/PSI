from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns = [
    url(r'^$', views.BaseCart.as_view(), name='cart_list'),
    url(r'^checkout/$', views.order_process, name='checkout'),
    url(r'^order_created/$', views.order_created, name='order_created'),
    path(r'cart_add/<slug:slug>', views.cart_add, name='cart_add'),
    path(r'cart_remove/<slug:slug>', views.cart_remove, name='cart_remove'),
    path(r'cart_clear/', views.cart_clear, name='cart_clear'),
    path(r'order_create/', views.order_create, name='order_create'),
    path(r'order_process/', views.order_process, name='order_process'),

]
