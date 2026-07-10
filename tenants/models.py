from django.db import models
from django.core.validators import MinValueValidator
from user.models import CustomUser
from properties.models import Property, Unit

class Tenant(models.Model):
    """Tenant rental information"""
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('evicted', 'Evicted'),
        ('moved_out', 'Moved Out'),
    )
    
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='tenant_profile')
    property = models.ForeignKey(Property, on_delete=models.SET_NULL, null=True, related_name='tenants')
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True, related_name='tenants')
    lease_start_date = models.DateField()
    lease_end_date = models.DateField()
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    security_deposit = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    emergency_contact_name = models.CharField(max_length=255, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.unit}"
