# ---- Admin Role-Based View ----
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def admin_required(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

@user_passes_test(admin_required)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
