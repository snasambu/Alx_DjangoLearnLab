from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from .managers import CustomUserManager  # Import the custom manager


class CustomUser(AbstractUser):
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='bookshelf_user_set',  # Changed related name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='bookshelf_user_permissions_set',  # Changed related name
        blank=True
    )

    objects = CustomUserManager()
    

