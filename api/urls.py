from django.urls import path
from .views import BookList
from django.http import JsonResponse

# Simple root view
def home(request):
    return JsonResponse({"message": "Welcome to the Book API"})

urlpatterns = [
    path('', home, name='home'),                # Root URL
    path('books/', BookList.as_view(), name='book-list'),  # API endpoint
]

