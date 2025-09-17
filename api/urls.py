from django.urls import path, include  # <-- include added
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView (for checker)
    path('books/', BookList.as_view(), name='book-list'),

    # Router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),  # include must be explicitly imported
]


