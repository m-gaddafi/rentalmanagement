from django.contrib import admin
from payments.models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('tenant', 'amount', 'due_date', 'payment_date', 'status', 'payment_method')
    list_filter = ('status', 'payment_method', 'due_date', 'payment_date')
    search_fields = ('tenant__user__first_name', 'tenant__user__last_name', 'transaction_id')
    readonly_fields = ('created_at', 'updated_at')
    date_hierarchy = 'due_date'
    fieldsets = (
        ('Payment Information', {
            'fields': ('tenant', 'amount', 'status')
        }),
        ('Dates', {
            'fields': ('due_date', 'payment_date')
        }),
        ('Payment Method & Transaction', {
            'fields': ('payment_method', 'transaction_id')
        }),
        ('Notes', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

