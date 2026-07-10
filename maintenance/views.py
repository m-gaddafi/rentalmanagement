from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from maintenance.models import MaintenanceRequest
from maintenance.serializers import MaintenanceRequestSerializer, MaintenanceRequestDetailSerializer

class MaintenanceRequestViewSet(viewsets.ModelViewSet):
    """ViewSet for MaintenanceRequest model"""
    queryset = MaintenanceRequest.objects.all()
    serializer_class = MaintenanceRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'property__name']
    ordering_fields = ['priority', 'status', 'created_at']

    def get_serializer_class(self):
        """Use detailed serializer for retrieve"""
        if self.action == 'retrieve':
            return MaintenanceRequestDetailSerializer
        return MaintenanceRequestSerializer

    def get_queryset(self):
        """Filter based on user role"""
        if self.request.user.role == 'maintenance':
            return MaintenanceRequest.objects.filter(assigned_to=self.request.user)
        elif self.request.user.role == 'landlord':
            return MaintenanceRequest.objects.filter(property__owner=self.request.user)
        return MaintenanceRequest.objects.all()

    def perform_create(self, serializer):
        """Set reported_by to current user"""
        serializer.save(reported_by=self.request.user)

    @action(detail=False, methods=['get'])
    def open(self, request):
        """Get all open maintenance requests"""
        requests = self.get_queryset().filter(status__in=['open', 'in_progress'])
        serializer = self.get_serializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def urgent(self, request):
        """Get all urgent maintenance requests"""
        requests = self.get_queryset().filter(priority='urgent', status__in=['open', 'in_progress'])
        serializer = self.get_serializer(requests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def start_work(self, request, pk=None):
        """Mark request as in progress"""
        from django.utils import timezone
        request_obj = self.get_object()
        request_obj.status = 'in_progress'
        request_obj.started_at = timezone.now()
        request_obj.save()
        serializer = self.get_serializer(request_obj)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def complete(self, request, pk=None):
        """Mark request as completed"""
        from django.utils import timezone
        request_obj = self.get_object()
        request_obj.status = 'completed'
        request_obj.completed_at = timezone.now()
        request_obj.save()
        serializer = self.get_serializer(request_obj)
        return Response(serializer.data)

