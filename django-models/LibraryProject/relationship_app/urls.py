from django.urls import path
from . import views

urlpatterns = [
    path("books/", views.book_list, name="book_list"),  # Function-based view
    path("library/<int:pk>/", views.LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
]
