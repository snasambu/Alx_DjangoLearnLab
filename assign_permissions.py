import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User, Permission

# Make migrations and migrate
call_command('makemigrations', 'relationship_app')
call_command('migrate', 'relationship_app')

# Create normal user if it doesn't exist
user, created = User.objects.get_or_create(username='normaluser')
if created:
    user.set_password('password123')
    user.save()

# Assign permissions
try:
    perm_add = Permission.objects.get(codename='can_add_book')
    perm_change = Permission.objects.get(codename='can_change_book')
    perm_delete = Permission.objects.get(codename='can_delete_book')
except Permission.DoesNotExist:
    raise SystemExit("Error: Book permissions do not exist. Check your Book model Meta permissions.")

user.user_permissions.add(perm_add, perm_change, perm_delete)
user.save()

print("User 'normaluser' created/updated with book permissions successfully!")
