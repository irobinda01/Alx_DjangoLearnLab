from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.
def book_list(request):
    books = Book.objects.all()  # Query all books
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"  # Path to the template for library details
    context_object_name = "library"