from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from .views import is_member

# Member view
@user_passes_test(is_member)
def member_view(request):
    return HttpResponse("Welcome, Member!")