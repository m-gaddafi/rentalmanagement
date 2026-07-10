from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from properties.models import Property, Unit
from properties.serializers import PropertySerializer, PropertyDetailSerializer, UnitSerializer

class PropertyViewSet(viewsets.ModelViewSet):
    """ViewSet for Property model"""
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'address', 'city']
    ordering_fields = ['created_at', 'name']

    def get_serializer_class(self):
        """Use detailed serializer for retrieve"""
        if self.action == 'retrieve':
            return PropertyDetailSerializer
        return PropertySerializer

    def perform_create(self, serializer):
        """Set owner to current user"""
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """Filter properties by owner"""
        if self.request.user.role == 'landlord':
            return Property.objects.filter(owner=self.request.user)
        return Property.objects.all()

    @action(detail=True, methods=['get'])
    def units_summary(self, request, pk=None):
        """Get units summary for a property"""
        property = self.get_object()
        units = property.units.all()
        available_count = units.filter(is_available=True).count()
        occupied_count = units.filter(is_available=False).count()
        
        return Response({
            'property': property.name,
            'total_units': units.count(),
            'available_units': available_count,
            'occupied_units': occupied_count,
            'occupancy_rate': f"{(occupied_count / units.count() * 100) if units.count() > 0 else 0:.2f}%"
        })


class UnitViewSet(viewsets.ModelViewSet):
    """ViewSet for Unit model"""
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['unit_number', 'property__name']
    ordering_fields = ['rent_amount', 'bedrooms']

    def get_queryset(self):
        """Filter by property if specified"""
        queryset = Unit.objects.all()
        property_id = self.request.query_params.get('property_id')
        if property_id:
            queryset = queryset.filter(property_id=property_id)
        return queryset

    @action(detail=False, methods=['get'])
    def available(self, request):
        """Get all available units"""
        units = self.get_queryset().filter(is_available=True)
        serializer = self.get_serializer(units, many=True)
        return Response(serializer.data)

