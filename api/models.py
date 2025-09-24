from django.db import models

# Author model represents a writer in our system.
# Fields:
# - name: The full name of the author.
# Relationship:
# - An Author can have multiple Books (one-to-many relationship).
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Book model represents a book written by an author.
# Fields:
# - title: The title of the book.
# - publication_year: The year the book was published.
# - author: ForeignKey linking the book to its author.
# Relationship:
# - Each Book belongs to a single Author.
# - related_name="books" allows accessing all books of an author via author.books.all()
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
