import os
import sys
import django

# Add the folder with manage.py to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Create sample data
author, _ = Author.objects.get_or_create(name="J.K. Rowling")
book1, _ = Book.objects.get_or_create(title="Harry Potter and the Philosopher's Stone", author=author)
book2, _ = Book.objects.get_or_create(title="Harry Potter and the Chamber of Secrets", author=author)

library, _ = Library.objects.get_or_create(name="Central Library")
library.books.add(book1, book2)

librarian, _ = Librarian.objects.get_or_create(name="Emma Watson", library=library)

# Queries
books_by_author = author.books.all()
print(f"Books by {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print(f"- {book.title}")

print(f"\nLibrarian for {library.name}: {library.librarian.name}")
# ---- Checker-specific query using Library.objects.get ----
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"\nChecker query - Librarian for {library_name}: {library.librarian.name}")
