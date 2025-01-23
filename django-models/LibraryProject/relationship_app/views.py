from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.views.generic import DetailView
from .models import Library

# Create your views here.

def book_list(request):
    books = Book.objects.all()  # Query all books
    # Create a simple text response
    response = "\n".join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(response, content_type="text/plain")


class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"  # Use this template for structured output
    context_object_name = "library"  # Context variable for the library instance
