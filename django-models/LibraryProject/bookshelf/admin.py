from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
  # Display these fields in the admin list view
  list_display = ('title', 'author', 'publication_year')

  # Add search capabilities for title and author
  search_fields = ('title', 'author')

  # Add filter options for the publication year
  list_filter = ('publication_year',)

admin.site.register(Book, BookAdmin)