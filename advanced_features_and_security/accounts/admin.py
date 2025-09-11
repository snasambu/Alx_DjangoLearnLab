from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")

    # Fields available when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

    # Fields available when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )

# Register the model and the custom admin
admin.site.register(CustomUser, CustomUserAdmin)
