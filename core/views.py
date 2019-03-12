from django.shortcuts import render, get_object_or_404
from core.models import Book, Topic
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""

    # counts number of posted books
    books = Book.objects.all()
    context = {
        'books': books,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
