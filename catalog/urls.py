from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home')
]

urlpatterns +=[
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail')
]