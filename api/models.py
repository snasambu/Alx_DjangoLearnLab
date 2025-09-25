from django.db import models

<<<<<<< HEAD
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
=======
# The Author model represents an author of books.
# Each author has a 'name' field to store their full name.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        # Returns the author's name when the object is printed
        return self.name

# The Book model represents a book written by an author.
# Fields:
# - title: the book's title
# - publication_year: the year the book was published
# - author: foreign key linking to the Author model
#   This establishes a one-to-many relationship: one author can have multiple books.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,   # Delete all books if the author is deleted
        related_name="books"        # Allows reverse access: author.books.all()
    )

    def __str__(self):
        # Returns a string showing the book title and year
>>>>>>> 161c6cb (Initial commit: Django project with api app, models, and serializers)
        return f"{self.title} ({self.publication_year})"
