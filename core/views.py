from django.shortcuts import render, get_object_or_404, redirect
from core.models import Book, Topic, User
from django.views import generic
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages
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
    book = topic.book_set
    return render(request, 'core/topic_list.html', {'topic': topic, 'book': book})

@require_http_methods(['POST'])
@login_required
def book_favorite_view(request, slug):
    book = get_object_or_404(Book, slug=slug)

    favorite, created = request.user.favorite_set.get_or_create(book=book)

    if created:
        messages.info(request, f"You have favorited {book.title}.")
    else:
        messages.info(request, f"You have unfavorited {book.title}.")
        favorite.delete()

    return redirect(book.get_absolute_url())
