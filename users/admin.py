from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin dla rozszerzonego modelu użytkownika."""
    
    list_display = ('username', 'email', 'first_name', 'last_name', 'university', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'university')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'university')
    
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Dane studenta', {
            'fields': ('phone', 'university', 'bio', 'avatar'),
        }),
    )
    
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Dane studenta', {
            'fields': ('phone', 'university'),
        }),
    )
