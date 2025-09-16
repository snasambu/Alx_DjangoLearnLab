import os
import sys
import django

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Correct Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')

django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Sample Data Creation ---
Author.objects.all().delete()
Book.objects.all().delete()
Library.objects.all().delete()
Librarian.objects.all().delete()

author1 = Author.objects.create(name="George Orwell")
author2 = Author.objects.create(name="J.K. Rowling")

book1 = Book.objects.create(title="1984", author=author1)
book2 = Book.objects.create(title="Animal Farm", author=author1)
book3 = Book.objects.create(title="Harry Potter", author=author2)

library1 = Library.objects.create(name="Central Library")
library1.books.set([book1, book2, book3])

librarian1 = Librarian.objects.create(name="Alice", library=library1)

# --- Queries ---
print("Books by George Orwell:", list(Book.objects.filter(author__name='George Orwell').values_list('title', flat=True)))
print("Books in Central Library:", list(library1.books.values_list('title', flat=True)))
print("Librarian for Central Library:", Librarian.objects.get(library=library1).name)
