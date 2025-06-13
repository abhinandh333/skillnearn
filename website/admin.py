from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.actions import delete_selected
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Columns shown in the list
    list_display = ('id', 'full_name', 'phone_number', 'is_staff', 'is_active')

    # Make full_name clickable
    list_display_links = ('full_name',)

    # Enable delete action
    actions = [delete_selected]

    # Add filters (right side of admin)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')

    # Add search functionality
    search_fields = ('phone_number', 'full_name')

    # Ordering
    ordering = ('id',)

    # Fields shown on edit form
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    # Fields shown when creating a new user via admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'full_name', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

# Register your custom user model and admin
admin.site.register(CustomUser, CustomUserAdmin)
