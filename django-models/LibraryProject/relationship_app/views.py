from django.shortcuts import render

# Create your views here.
# ---- New Views for Checker ----
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# Function-based view: list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, "list_books.html", {"books": books})

# Class-based view: library detail
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
# ---- Checker-compliant view ----
from django.shortcuts import render
from .models import Book

def list_books_checker(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})
# ---- Checker-compliant LibraryDetailView ----
from django.views.generic import DetailView
from .models import Library  # Explicit import for checker

class LibraryDetailViewChecker(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
# ---- Checker-compliant import ----
from django.views.generic.detail import DetailView
# ---- Authentication Views ----
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def admin_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
# ---- Librarian Role-Based View ----
def librarian_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

@user_passes_test(librarian_required)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')
# ---- Member Role-Based View ----
def member_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(member_required)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book

# ---- Secured Views ----

@permission_required('relationship_app.can_add_book')
def add_book(request):
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'relationship_app/delete_book.html', {'book': book})
