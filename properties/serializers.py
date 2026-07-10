from rest_framework import serializers
from properties.models import Property, Unit

class UnitSerializer(serializers.ModelSerializer):
    """Serializer for Unit model"""
    property_name = serializers.CharField(source='property.name', read_only=True)
    
    class Meta:
        model = Unit
        fields = [
            'id', 'property', 'property_name', 'unit_number', 'rent_amount',
            'bedrooms', 'bathrooms', 'square_feet', 'is_available', 'features',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PropertySerializer(serializers.ModelSerializer):
    """Serializer for Property model"""
    owner_name = serializers.CharField(source='owner.get_full_name', read_only=True)
    units = UnitSerializer(many=True, read_only=True)
    
    class Meta:
        model = Property
        fields = [
            'id', 'owner', 'owner_name', 'name', 'address', 'city', 'state',
            'zip_code', 'total_units', 'description', 'amenities', 'property_type',
            'units', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PropertyDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Property with full unit data"""
    owner_name = serializers.CharField(source='owner.get_full_name', read_only=True)
    units = UnitSerializer(many=True, read_only=True)
    available_units_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Property
        fields = [
            'id', 'owner', 'owner_name', 'name', 'address', 'city', 'state',
            'zip_code', 'total_units', 'available_units_count', 'description',
            'amenities', 'property_type', 'units', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_available_units_count(self, obj):
        return obj.units.filter(is_available=True).count()
