from django.shortcuts import render
from .models import Book
from django.http import HttpResponse

# Create your views here.
# Groups: Viewers, Editors, Admins
# Permissions: can_view, can_create, can_edit, can_delete
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookForm, ExampleForm

@permission_required('your_app.can_view', raise_exception=True)
def book_list(request):
    book = Book.objects.all()
    return render(request, 'books/view_books.html', {'books': book})

@permission_required('your_app.can_create', raise_exception=True)
def create_article(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm()
    return render(request, 'books/create_book.html', {'form': form})

@permission_required('your_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/edit_book.html', {'form': form, 'book': book})

@permission_required('your_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('view_books')
    return render(request, 'books/delete_book.html', {'book': book})


def search_books(request):
    form = ExampleForm(request.GET)
    books = []
    if form.is_valid():
        title = form.cleaned_data.get('title')
        books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'books': books, 'form': form})


def custom_view(request):
    response = HttpResponse("Hello, world!")
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self'; style-src 'self'"
    return response
