from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone', 'address', 'city', 'state', 'zip_code', 'role', 'profile_picture')}),
    )
    list_display = ('username', 'email', 'get_full_name', 'role', 'phone', 'created_at')
    list_filter = BaseUserAdmin.list_filter + ('role', 'created_at')
    search_fields = BaseUserAdmin.search_fields + ('phone', 'city', 'role')

