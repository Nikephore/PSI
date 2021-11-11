import datetime
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
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML home.html con los datos en la variable contexto
    return render(request, 'home.html', context=None)


def BookDetailView(request, slug):
    sl=(get_object_or_404(Book, slug=slug))
    return render(request, "catalog/book_detail.html", {"book" : sl})

  
class BookListView(generic.ListView):
    model = Book
    paginate_by = 5


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5