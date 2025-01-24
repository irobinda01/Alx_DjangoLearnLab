from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics 
from .models import Book
from .serializers import BookSerializer

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetches all Book instances
    serializer_class = BookSerializer  # Specifies the serializer for the data


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()  # All Book objects
    serializer_class = BookSerializer  # Serializer for the Book model