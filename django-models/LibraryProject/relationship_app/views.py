from .models import Book
from .models import relationship
from .models import Library
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout, registration
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



# Create your views here.
def ListView(request):
    books = Book.objects.all()
    context = {'list_books':books}
    return render(request, "relationship_app/list_books.html", {"books":books} )

#Create a class-based view 
def BookDetailView(DetailView):
    model = Book
    template_name = "relationship_app/library_detail.html"




""" Utilize Django’s built-in views and forms for handling user authentication. You will need to create views for user login, logout, and registration.
 user  login, logout , registeration: """

# create new user:
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

#logins and registration:
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

