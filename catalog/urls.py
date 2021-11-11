from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path(r'book/<slug:slug>', views.BookDetailView, name='book-detail'),

]

urlpatterns +=[
]