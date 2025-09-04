from bookshelf.models import Book

# Retrieve the book first
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()
# Output: (1, {'bookshelf.Book': 1})

> ✅ Note: Keep the triple backticks and “python” for syntax highlighting.
