from django.urls import path
from . import views
from .views import list_books, LibraryDetailView, LoginView, LogoutView

urlpatterns = [
    path("books/", list_books, name="book_list"),  # Function-based view
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),  # Class-based view
    path("register/", views.register, name="register"),
    path("login/", LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
