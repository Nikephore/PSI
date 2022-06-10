from django.shortcuts import redirect, render
from django.views import generic
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

from catalog.forms import VoteAddToBook

# Create your views here.
from .models import Book, Author, Vote


def home(request):
    score_order = Book.objects.all().order_by('-score')[:5]
    date_order = Book.objects.all().order_by('-date')[:5]
    vote_order = Book.objects.all().order_by('-n_votes')[:5]

    context = {'score_order': score_order, 'date_order': date_order, 'vote_order': vote_order}

    # Renderiza la plantilla HTML home.html con los datos en la variable contexto
    return render(request, 'home.html', context=context)


class Search(generic.ListView):
    model = Book
    template_name = 'search.html'
    paginate_by = 9

    query_name = ''

    def get_queryset(self):
        query = self.request.GET.get('q')

        self.query_name = query

        book_search_list = Book.objects.filter(title__icontains=query)

        author_search = Author.objects.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query)
        )

        book_author = Book.objects.filter(
            author__in=author_search
        )

        search_list = (book_author | book_search_list).distinct()

        return search_list

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context.update({'result': self.query_name})
        return context


def BookDetailView(request, slug):
    sl = (get_object_or_404(Book, slug=slug))
    return render(request, "catalog/book_detail.html", {"book": sl})


class BookListView(generic.ListView):
    model = Book
    template_name = 'book_list.html'
    paginate_by = 9


def UserVote(request, slug):
    vote = Vote(request)
    if request.method == 'POST':
        form = VoteAddToBook(request.POST)
        if form.is_valid():
            rate = int(form.cleaned_data.get('rate'))
            user = request.user
            book = Book.objects.get(slug=slug)
            Vote.create_rate(book, user, rate)
        return redirect('home')
    return redirect('home')
