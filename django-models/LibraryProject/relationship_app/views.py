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


# create new user:
user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")

#logins and registration:
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'logout.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


