from django.shortcuts import render, get_object_or_404
from core.models import Book, Topic
from django.views import generic
from core.forms import TopicSearch
# Create your views here.

def index(request):
    """View function for home page of site."""
    if request.GET:
        form = TopicSearch(request.GET)
        books = form.search()
    else:
        form = TopicSearch()
        books = Book.objects.all()

    response = render(request, 'index.html', {
        "books": books,
        "topic_form": form,
        })

    return response

class BookListView(generic.ListView):
    model = Book


def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'core/book_detail.html', {'book': book})
