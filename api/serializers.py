from rest_framework import serializers
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
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


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
