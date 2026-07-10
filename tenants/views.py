from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from tenants.models import Tenant
from tenants.serializers import TenantSerializer, TenantDetailSerializer

class TenantViewSet(viewsets.ModelViewSet):
    """ViewSet for Tenant model"""
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__first_name', 'user__last_name', 'property__name']
    ordering_fields = ['lease_start_date', 'status', 'created_at']

    def get_serializer_class(self):
        """Use detailed serializer for retrieve"""
        if self.action == 'retrieve':
            return TenantDetailSerializer
        return TenantSerializer

    def get_queryset(self):
        """Filter based on user role"""
        if self.request.user.role == 'tenant':
            return Tenant.objects.filter(user=self.request.user)
        elif self.request.user.role == 'landlord':
            return Tenant.objects.filter(property__owner=self.request.user)
        return Tenant.objects.all()

    @action(detail=False, methods=['get'])
    def active(self, request):
        """Get all active tenants"""
        tenants = self.get_queryset().filter(status='active')
        serializer = self.get_serializer(tenants, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def move_out(self, request, pk=None):
        """Mark tenant as moved out"""
        tenant = self.get_object()
        tenant.status = 'moved_out'
        if tenant.unit:
            tenant.unit.is_available = True
            tenant.unit.save()
        tenant.save()
        serializer = self.get_serializer(tenant)
        return Response(serializer.data)

