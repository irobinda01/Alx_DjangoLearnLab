from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.
def book_list(request):
    books = Book.objects.all()  # Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})



class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  # Use this template for structured output
    context_object_name = "library"  # Context variable for the library instance
