from django.shortcuts import render
from core.models import Book, Author, Category
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""

    # counts number of posted books
    num_books = Book.objects.all().count()

    # counts number of authors
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'top_books'


# class Book_view()
