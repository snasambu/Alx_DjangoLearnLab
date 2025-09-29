# check_installation.py
import os
import django

# Setup Django environment for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'advanced_api_project.settings')
django.setup()

from django.conf import settings

print("Django version:", django.get_version())
print("INSTALLED_APPS:", settings.INSTALLED_APPS)
