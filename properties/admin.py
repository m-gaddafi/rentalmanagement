from django.contrib import admin
from properties.models import Property, Unit

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1
    fields = ('unit_number', 'rent_amount', 'bedrooms', 'bathrooms', 'square_feet', 'is_available')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [UnitInline]
    list_display = ('name', 'address', 'city', 'owner', 'property_type', 'total_units', 'created_at')
    list_filter = ('property_type', 'city', 'created_at', 'owner')
    search_fields = ('name', 'address', 'city', 'owner__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('owner', 'name', 'property_type', 'total_units')
        }),
        ('Location', {
            'fields': ('address', 'city', 'state', 'zip_code')
        }),
        ('Details', {
            'fields': ('description', 'amenities')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ('unit_number', 'property', 'rent_amount', 'bedrooms', 'bathrooms', 'is_available')
    list_filter = ('is_available', 'property', 'bedrooms', 'bathrooms')
    search_fields = ('unit_number', 'property__name')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Property & Unit Info', {
            'fields': ('property', 'unit_number')
        }),
        ('Details', {
            'fields': ('bedrooms', 'bathrooms', 'square_feet', 'features')
        }),
        ('Rent & Availability', {
            'fields': ('rent_amount', 'is_available')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

