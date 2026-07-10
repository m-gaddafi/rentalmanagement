from django.contrib import admin
from maintenance.models import MaintenanceRequest

@admin.register(MaintenanceRequest)
class MaintenanceRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'property', 'priority', 'status', 'reported_by', 'assigned_to', 'created_at')
    list_filter = ('status', 'priority', 'property', 'created_at', 'assigned_to')
    search_fields = ('title', 'description', 'property__name', 'unit_number')
    readonly_fields = ('created_at', 'started_at', 'completed_at')
    fieldsets = (
        ('Request Information', {
            'fields': ('property', 'unit_number', 'title', 'description')
        }),
        ('Priority & Status', {
            'fields': ('priority', 'status')
        }),
        ('Assignment', {
            'fields': ('reported_by', 'assigned_to')
        }),
        ('Costs', {
            'fields': ('estimated_cost', 'actual_cost')
        }),
        ('Completion', {
            'fields': ('completion_notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'started_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )
    date_hierarchy = 'created_at'

