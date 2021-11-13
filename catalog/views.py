import datetime
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
from .models import Book, Author


def home(request):
    score_order = Book.objects.all().order_by('-score')[:5]
    date_order = Book.objects.all().order_by('-date')[:5]

    context = {'score_order' : score_order, 'date_order' : date_order}

    # Renderiza la plantilla HTML home.html con los datos en la variable contexto
    return render(request, 'home.html', context=context)


def BookDetailView(request, slug):
    sl=(get_object_or_404(Book, slug=slug))
    return render(request, "catalog/book_detail.html", {"book" : sl})


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5