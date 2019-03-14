from django.shortcuts import render, get_object_or_404
from core.models import Book, Topic
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""
    books = Book.objects.all()
    topics = Topic.objects.all()
    context = {
        'books': books,
        'topics': topics
    }
    return render(request, 'index.html', context=context)


# class TopicListView(generic.ListView):
#     model = Topic


def book_detail_view(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'core/book_detail.html', {'book': book})

def topic_list_view(request, slug):
    topic = get_object_or_404(Topic, slug=slug)
    return render(request, 'core/topic_list.html', {'topic': topic})
