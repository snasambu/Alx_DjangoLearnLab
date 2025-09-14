```python
from bookshelf.models import Book

# Retrieve the book with title "1984"
book = Book.objects.get(title="1984")
book
# Output: <Book: 1984 by George Orwell (1949)>
