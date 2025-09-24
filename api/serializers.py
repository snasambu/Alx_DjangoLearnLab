from rest_framework import serializers
from .models import Author, Book
from datetime import date

# Serializer for Book model.
# Serializes all fields and adds custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation: ensures the book's publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


# Serializer for Author model.
# Includes the name field and a nested list of books using BookSerializer.
# The nested 'books' field represents the one-to-many relationship:
#   Each Author can have multiple Books, accessed via author.books.all()
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # Nested serializer for related books

    class Meta:
        model = Author
        fields = ['name', 'books']
