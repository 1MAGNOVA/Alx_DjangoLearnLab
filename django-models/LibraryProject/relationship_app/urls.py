from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('list_books/', list_view, name='list_books'),
    path('library/', LibraryDetailView.as_view(), name='library_detail'),
    path("views.register", "LogoutView.as_view(template_name=", "LoginView.as_view(template_name=")
    ]
