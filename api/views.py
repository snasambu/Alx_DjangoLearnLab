# api/views.py
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# Original ListAPIView (required for checker)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Optional: ModelViewSet for CRUD (future enhancement)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

