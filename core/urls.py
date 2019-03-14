from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('book/<slug:slug>/',views.book_detail_view, name='book_detail'),
    path('topic/<int:pk>/',views.topic_list_view, name='topic_list'),
]
