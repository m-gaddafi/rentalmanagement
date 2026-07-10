from rest_framework import serializers
from maintenance.models import MaintenanceRequest

class MaintenanceRequestSerializer(serializers.ModelSerializer):
    """Serializer for MaintenanceRequest model"""
    property_name = serializers.CharField(source='property.name', read_only=True)
    reported_by_name = serializers.CharField(source='reported_by.get_full_name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.get_full_name', read_only=True, allow_null=True)
    
    class Meta:
        model = MaintenanceRequest
        fields = [
            'id', 'property', 'property_name', 'unit_number', 'reported_by',
            'reported_by_name', 'assigned_to', 'assigned_to_name', 'title',
            'description', 'priority', 'status', 'estimated_cost', 'actual_cost',
            'completion_notes', 'created_at', 'started_at', 'completed_at'
        ]
        read_only_fields = ['id', 'created_at']


class MaintenanceRequestDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for MaintenanceRequest"""
    property_name = serializers.CharField(source='property.name', read_only=True)
    reported_by_name = serializers.CharField(source='reported_by.get_full_name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.get_full_name', read_only=True, allow_null=True)
    days_open = serializers.SerializerMethodField()
    
    class Meta:
        model = MaintenanceRequest
        fields = [
            'id', 'property', 'property_name', 'unit_number', 'reported_by',
            'reported_by_name', 'assigned_to', 'assigned_to_name', 'title',
            'description', 'priority', 'status', 'estimated_cost', 'actual_cost',
            'completion_notes', 'days_open', 'created_at', 'started_at', 'completed_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_days_open(self, obj):
        from datetime import datetime
        from django.utils.timezone import now
        if obj.status == 'completed' and obj.completed_at:
            return (obj.completed_at - obj.created_at).days
        return (now() - obj.created_at).days
