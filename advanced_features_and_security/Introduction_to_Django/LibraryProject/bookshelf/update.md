from bookshelf.models import Book

# Retrieve the book first
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>

> ✅ Note: Keep the triple backticks and “python” for syntax highlighting.
