from django.db import models
# -----------------------------
# Author model: stores author names
# -----------------------------
# Each Author instance represents a unique author.
# Fields:
# - name: a string field to store the author's full name.
# Relationships:
# - One-to-many relationship with Book.
#   Access all books of an author via `author.books.all()`.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# -----------------------------
# Book model: stores book details and links to an author
# -----------------------------
# Each Book instance represents a single book.
# Fields:
# - title: a string field for the book's title.
# - publication_year: integer field for the year of publication.
# - author: ForeignKey linking to the Author model.
# Relationships:
# - Many books can belong to one author (one-to-many).
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        related_name='books',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
