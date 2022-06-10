from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    path(r'book/<slug:slug>', views.BookDetailView, name='book-detail'),
]

urlpatterns += [
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^search/$', views.Search.as_view(), name='search'),
    path(r'user_vote/<slug:slug>', views.UserVote, name='UserVote')
]
