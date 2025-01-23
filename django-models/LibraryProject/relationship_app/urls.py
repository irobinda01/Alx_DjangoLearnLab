from django.urls import path
from .views import list_books, LibraryDetailView, register, CustomLoginView, CustomLogoutView

urlpatterns = [
    path("books/", list_books, name="book_list"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("register/", register, name="register"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
]
