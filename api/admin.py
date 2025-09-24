from django.contrib import admin
from .models import Author, Book

# Register Author and Book models to make them manageable via Django admin
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display name in the admin list

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_year', 'author')  # Display fields in list
    list_filter = ('publication_year', 'author')  # Filter options in admin
