from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', list_booksView.as_view, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
        ]



