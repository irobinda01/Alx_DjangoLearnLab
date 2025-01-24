from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetches all Book instances
    serializer_class = BookSerializer  # Specifies the serializer for the data
