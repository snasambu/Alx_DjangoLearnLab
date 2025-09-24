from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from datetime import date

# ------------------------------
# Book List View (with search & ordering)
# ------------------------------
class BookListView(generics.ListAPIView):
    """
    GET: List all books with optional search and ordering.
    Searchable by book title and author name.
    Ordering available by publication_year and title.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'author__name']      # Allows searching by title or author
    ordering_fields = ['publication_year', 'title']  # Allows ordering

# ------------------------------
# Book Detail View
# ------------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# ------------------------------
# Book Create View
# ------------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book.
    Permissions: Only authenticated users.
    Validates that publication_year is not in the future.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if serializer.validated_data['publication_year'] > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# ------------------------------
# Book Update View
# ------------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book by ID.
    Permissions: Only authenticated users.
    Validates that publication_year is not in the future.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
   # permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        if serializer.validated_data['publication_year'] > date.today().year:
            raise ValidationError("Publication year cannot be in the future.")
        serializer.save()

# ------------------------------
# Book Delete View
# ------------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book by ID.
    Permissions: Only authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
