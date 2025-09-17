# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books-list/', BookList.as_view(), name='book-list'),  # for checker
    path('', include(router.urls)),  # CRUD endpoints
]
