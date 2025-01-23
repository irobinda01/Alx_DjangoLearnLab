from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .views import is_librarian

# Librarian view
@user_passes_test(is_librarian)
def librarian_view(request):
    return HttpResponse("Welcome, Librarian!")