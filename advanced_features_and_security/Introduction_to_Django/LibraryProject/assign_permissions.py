import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User, Permission

# Make migrations and migrate
call_command('makemigrations', 'relationship_app')
call_command('migrate', 'relationship_app')

# Create or get user
user, created = User.objects.get_or_create(username='normaluser')
if created:
    user.set_password('password123')
    user.save()

# Get custom permissions
perm_add = Permission.objects.get(codename='can_add_book')
perm_change = Permission.objects.get(codename='can_change_book')
perm_delete = Permission.objects.get(codename='can_delete_book')

# Assign permissions to user
user.user_permissions.add(perm_add, perm_change, perm_delete)
user.save()

print("User 'normaluser' created/updated with book permissions successfully!")
