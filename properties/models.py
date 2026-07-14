from django.db import models
from django.core.validators import MinValueValidator
from user.models import CustomUser

class Property(models.Model):
    """Rental property/building model"""
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='properties')
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10,blank=True, null=True)
    total_units = models.IntegerField(validators=[MinValueValidator(1)], blank=True, null=True)
    description = models.TextField(blank=True)
    amenities = models.TextField(blank=True, help_text="Comma-separated list of amenities")
    property_type = models.CharField(max_length=50, choices=(
        ('apartment', 'Apartment'),
        ('house', 'House'),
        ('condo', 'Condo'),
        ('townhouse', 'Townhouse'),
    ), default='apartment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self):
        return f"{self.name} - {self.address}"


class Unit(models.Model):
    """Individual rental unit within a property"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='units')
    unit_number = models.CharField(max_length=50)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bedrooms = models.IntegerField(validators=[MinValueValidator(0)])
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0)])
    square_feet = models.IntegerField(validators=[MinValueValidator(1)])
    is_available = models.BooleanField(default=True)
    features = models.TextField(blank=True, help_text="Unit features and descriptions")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['unit_number']
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'
        unique_together = ('property', 'unit_number')

    def __str__(self):
        return f"{self.property.name} - Unit {self.unit_number}"
