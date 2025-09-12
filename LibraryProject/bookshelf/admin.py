from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'date_joined', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active', 'groups']
    search_fields = ['email', 'username']
    ordering = ['date_joined']
    filter_horizontal = ['groups', 'user_permissions']

admin.site.register(CustomUser, CustomUserAdmin)
