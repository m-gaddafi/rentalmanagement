from rest_framework import serializers
from tenants.models import Tenant
from user.serializers import UserDetailSerializer
from properties.serializers import UnitSerializer

class TenantSerializer(serializers.ModelSerializer):
    """Serializer for Tenant model"""
    user_details = UserDetailSerializer(source='user', read_only=True)
    unit_info = UnitSerializer(source='unit', read_only=True)
    property_name = serializers.CharField(source='property.name', read_only=True)
    
    class Meta:
        model = Tenant
        fields = [
            'id', 'user', 'user_details', 'property', 'property_name', 'unit',
            'unit_info', 'lease_start_date', 'lease_end_date', 'monthly_rent',
            'security_deposit', 'emergency_contact_name', 'emergency_contact_phone',
            'status', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TenantDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Tenant"""
    user_details = UserDetailSerializer(source='user', read_only=True)
    unit_info = UnitSerializer(source='unit', read_only=True)
    property_name = serializers.CharField(source='property.name', read_only=True)
    
    class Meta:
        model = Tenant
        fields = [
            'id', 'user', 'user_details', 'property', 'property_name', 'unit',
            'unit_info', 'lease_start_date', 'lease_end_date', 'monthly_rent',
            'security_deposit', 'emergency_contact_name', 'emergency_contact_phone',
            'status', 'notes', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
