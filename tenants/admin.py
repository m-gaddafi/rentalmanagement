from django.contrib import admin
from tenants.models import Tenant

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'unit', 'status', 'lease_start_date', 'lease_end_date', 'monthly_rent')
    list_filter = ('status', 'property', 'lease_start_date', 'lease_end_date')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'property__name', 'unit__unit_number')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Tenant User', {
            'fields': ('user',)
        }),
        ('Lease Information', {
            'fields': ('property', 'unit', 'lease_start_date', 'lease_end_date', 'monthly_rent', 'security_deposit')
        }),
        ('Emergency Contact', {
            'fields': ('emergency_contact_name', 'emergency_contact_phone')
        }),
        ('Status & Notes', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

