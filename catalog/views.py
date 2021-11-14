from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Q

# Create your views here.
from .models import Book, Author


def home(request):
    """
    Función vista para la página inicio del sitio.
    """

    # Renderiza la plantilla HTML home.html con los datos en la variable contexto
    return render(request, 'home.html', context=None)


class Search(generic.ListView):
    model = Book
    template_name = 'search.html'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')

        book_search_list = Book.objects.filter(title__icontains=query)

        author_search = Author.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query)
        )

        book_author = Book.objects.filter(
            author__in=author_search
        )

        search_list = (book_author | book_search_list).distinct()

        return search_list


def BookDetailView(request, slug):
    sl = (get_object_or_404(Book, slug=slug))
    return render(request, "catalog/book_detail.html", {"book": sl})


class AuthorListView(generic.ListView):
    model = 5
    paginate_by = 5


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 5
