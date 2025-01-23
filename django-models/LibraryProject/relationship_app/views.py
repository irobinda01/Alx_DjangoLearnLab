from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    books = Book.objects.all()  # Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Path to the template for library details
    context_object_name = "library"


# Registration view
def register(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)  # Log in the user after registration
      return redirect("book_list")  # Redirect to a specific page after registration
  else:
    form = UserCreationForm()
  return render(request, "relationship_app/register.html", {"form": form})

# Login and Logout views will use Django's built-in views
class LoginView(LoginView):
    template_name = "relationship_app/login.html"

class LogoutView(LogoutView):
    template_name = "relationship_app/logout.html"



# Helper function to check user role
def is_admin(user):
    return user.profile.role == 'Admin'

def is_librarian(user):
    return user.profile.role == 'Librarian'

def is_member(user):
    return user.profile.role == 'Member'