from .models import Book
from django.shortcuts import render

# Create your views here.
def ListView(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, "relationship_app/list_books.html", {"books":books} ) 
