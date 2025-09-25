from rest_framework import serializers
<<<<<<< HEAD
from datetime import date
from .models import Author, Book

# ----------------------------------------
# BookSerializer
# ----------------------------------------
# Serializes all fields of the Book model.
# Includes custom validation:
# - Ensures publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom field validation
=======
from .models import Author, Book
from datetime import date

# Serializer for the Book model
# Serializes all fields of the Book model.
# Adds custom validation to ensure publication_year is not in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validator for publication_year
>>>>>>> 161c6cb (Initial commit: Django project with api app, models, and serializers)
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

<<<<<<< HEAD

# ----------------------------------------
# AuthorSerializer
# ----------------------------------------
# Serializes Author model fields.
# Includes nested BookSerializer to show all books related to an author.
# Relationship handling:
# - The 'books' field uses related_name='books' from the Book model.
# - 'many=True' indicates multiple related books.
# - 'read_only=True' means nested books are displayed but not directly writable here.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
=======
# Serializer for the Author model
# Includes:
# - name field
# - nested BookSerializer to show all books written by the author
# The nested serializer handles the one-to-many relationship defined by Book.author
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serialization

    class Meta:
        model = Author
        fields = ['name', 'books']
>>>>>>> 161c6cb (Initial commit: Django project with api app, models, and serializers)
