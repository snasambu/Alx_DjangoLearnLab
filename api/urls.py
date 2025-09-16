from django.urls import path
from .views import BookList  # make sure this matches your class name exactly

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]
