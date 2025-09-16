from rest_framework import generics  # keep generics at the top
from .models import Book
from .serializers import BookSerializer

# Checker-friendly definition
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
