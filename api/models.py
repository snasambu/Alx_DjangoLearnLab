from django.db import models

# ----------------------------------------
# Author Model
# ----------------------------------------
# Represents a book author. 
# Fields:
# - name: stores the author's full name.
# Relationships:
# - One-to-many with Book (an author can have multiple books)
class Author(models.Model):
    name = models.CharField(max_length=255)  # Author's name

    def __str__(self):
        return self.name


# ----------------------------------------
# Book Model
# ----------------------------------------
# Represents a book written by an author.
# Fields:
# - title: the title of the book.
# - publication_year: year the book was published.
# - author: foreign key linking to an Author object.
# Relationships:
# - Many books can belong to one author.
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year of publication
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE,      # Delete all books if the author is deleted
        related_name='books'          # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
