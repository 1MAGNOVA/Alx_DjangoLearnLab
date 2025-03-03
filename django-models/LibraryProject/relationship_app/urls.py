from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('books/list_books.html', list_books, name='list_books'),
    path('library/library_detail.html/', LibraryDetailView.as_view(), name='library_detail'),
        ]



