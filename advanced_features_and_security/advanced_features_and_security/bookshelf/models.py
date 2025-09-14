# bookshelf/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class LibraryProject(AbstractUser):
    """
    Custom user model for the bookshelf app.
    Extend this class to add extra fields if needed.
    """
    # Example: add extra fields here if needed
    # favorite_book = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username
