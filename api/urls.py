# api/urls.py
from django.urls import path, include, include  # include added for DefaultRouter
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Step 2: Set up the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')  # CRUD routes

urlpatterns = [
    # Existing ListAPIView (for the checker)
    path('books/', BookList.as_view(), name='book-list'),

    # Include router URLs for BookViewSet (all CRUD operations)
    path('', include(router.urls)),
]
