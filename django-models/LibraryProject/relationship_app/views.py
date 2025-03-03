from .models import Book
from django.shortcuts import render
from django.views.generic import TemplateView





# Create your views here.
def ListView(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, "relationship_app/list_books.html", {"books":books} ) 

#Create a class-based view 
def BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/library_detail.html"
