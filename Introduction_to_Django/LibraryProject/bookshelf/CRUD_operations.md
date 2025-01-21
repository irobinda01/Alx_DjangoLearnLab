# Create Operation

## Command:
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Expected Output: 1984 by George Orwell


# Retrieve Operation

## Command:
```python
retrieved_book = Book.objects.get(id=book.id)
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)
# Expected Output: 1984 George Orwell 1949

# Update Operation

## Command:
```python
book.title = "Nineteen Eighty-Four"
book.save()
updated_book = Book.objects.get(id=book.id)
print(updated_book.title) # Expected Output: Nineteen Eighty-Four

# Delete Operation

## Command:
```python
book.delete()
all_books = Book.objects.all()
print(all_books) # Expected Output: <QuerySet []>