from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models_userprofile import UserProfile

def check_role(role):
    return lambda u: hasattr(u, 'userprofile') and u.userprofile.role == role

@user_passes_test(check_role('Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')

@user_passes_test(check_role('Librarian'))
def librarian_view(request):
    return render(request, 'librarian_view.html')

@user_passes_test(check_role('Member'))
def member_view(request):
    return render(request, 'member_view.html')

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
