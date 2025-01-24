from django.db import models

# Create your models here.
class Author(models.Model):
    """
    Represents an author in the system.
    Fields:
    - name: The name of the author.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book in the system.
    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: The author of the book (one-to-many relationship with Author).
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
