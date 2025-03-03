from .models import Book
from .models import relationship
from .models import Library
from django.shortcuts import render
from django.views.generic.detail import DetailView





# Create your views here.
def ListView(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, "relationship_app/list_books.html", {"books":books} ) 

def list_books(request):
    books = Book.objects.all()
    book_list = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(book_list, content_type="text/plain")

#Create a class-based view 
def BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/library_detail.html"
