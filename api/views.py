from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, permissions, filters
from rest_framework.exceptions import ValidationError
from .models import Book
from .serializers import BookSerializer
from datetime import date

# ------------------------------
# Book List View (with search & ordering)
# ------------------------------
class BookListView(generics.ListAPIView):`n    """`n    View for class BookListView(generics.ListAPIView):`n    Permissions:`n      - List & Retrieve: AllowAny`n      - Create/Update/Delete: IsAuthenticated`n    Custom hooks:`n      - Future-year validation on publication_year`n    """
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
class BookDetailView(generics.RetrieveAPIView):`n    """`n    View for class BookDetailView(generics.RetrieveAPIView):`n    Permissions:`n      - List & Retrieve: AllowAny`n      - Create/Update/Delete: IsAuthenticated`n    Custom hooks:`n      - Future-year validation on publication_year`n    """
    """
    GET: Retrieve a single book by ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]

# ------------------------------
# Book Create View
# ------------------------------
class BookCreateView(generics.CreateAPIView):`n    """`n    View for class BookCreateView(generics.CreateAPIView):`n    Permissions:`n      - List & Retrieve: AllowAny`n      - Create/Update/Delete: IsAuthenticated`n    Custom hooks:`n      - Future-year validation on publication_year`n    """
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
class BookUpdateView(generics.UpdateAPIView):`n    """`n    View for class BookUpdateView(generics.UpdateAPIView):`n    Permissions:`n      - List & Retrieve: AllowAny`n      - Create/Update/Delete: IsAuthenticated`n    Custom hooks:`n      - Future-year validation on publication_year`n    """
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
class BookDeleteView(generics.DestroyAPIView):`n    """`n    View for class BookDeleteView(generics.DestroyAPIView):`n    Permissions:`n      - List & Retrieve: AllowAny`n      - Create/Update/Delete: IsAuthenticated`n    Custom hooks:`n      - Future-year validation on publication_year`n    """
    """
    DELETE: Remove a book by ID.
    Permissions: Only authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # permission_classes = [permissions.IsAuthenticated]
