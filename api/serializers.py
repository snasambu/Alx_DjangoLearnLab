from rest_framework import serializers
from .models import Author, Book
from datetime import date
# -----------------------------
# Serializer for Book model
# -----------------------------
# Serializes all fields of the Book model.
# Includes custom validation:
# - publication_year cannot be in the future.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author with nested books
# -----------------------------
# Serializer for Author model
# -----------------------------
# Serializes the 'name' field of Author.
# Includes nested BookSerializer for all related books.
# Relationships:
# - Nested serialization uses the 'books' related_name in Book model.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
