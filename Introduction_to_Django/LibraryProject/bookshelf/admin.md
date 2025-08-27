# Django Admin Integration for Book Model

This document explains how to register the `Book` model with the Django admin interface and customize its display for better management.

---

## 1️⃣ Register the Book Model

Edit `bookshelf/admin.py` and add the following:

```python
from django.contrib import admin
from .models import Book

# Register the Book model
admin.site.register(Book)
