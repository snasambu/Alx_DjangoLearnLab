from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Author, Book

# Inline admin for Books inside Author
class BookInline(admin.TabularInline):
    model = Book
    extra = 1

# Admin for Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [BookInline]

# Admin for Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'publication_year', 'author')
    list_filter = ('publication_year', 'author')
    search_fields = ('title',)
