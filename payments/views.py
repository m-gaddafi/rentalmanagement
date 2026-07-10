from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from payments.models import Payment
from payments.serializers import PaymentSerializer, PaymentDetailSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for Payment model"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['tenant__user__first_name', 'tenant__user__last_name']
    ordering_fields = ['due_date', 'status', 'created_at']

    def get_serializer_class(self):
        """Use detailed serializer for retrieve"""
        if self.action == 'retrieve':
            return PaymentDetailSerializer
        return PaymentSerializer

    def get_queryset(self):
        """Filter based on user role"""
        if self.request.user.role == 'tenant':
            return Payment.objects.filter(tenant__user=self.request.user)
        elif self.request.user.role == 'landlord':
            return Payment.objects.filter(tenant__property__owner=self.request.user)
        return Payment.objects.all()

    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """Get all overdue payments"""
        payments = self.get_queryset().filter(status='overdue')
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending payments"""
        payments = self.get_queryset().filter(status='pending')
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def mark_paid(self, request, pk=None):
        """Mark payment as paid"""
        from datetime import date
        payment = self.get_object()
        payment.status = 'paid'
        payment.payment_date = date.today()
        payment.save()
        serializer = self.get_serializer(payment)
        return Response(serializer.data)

