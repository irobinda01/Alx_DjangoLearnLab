from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .views import is_admin

@user_passes_test(is_admin)
def admin_view(request):
    return HttpResponse("Welcome, Admin!")