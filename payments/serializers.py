from rest_framework import serializers
from payments.models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment model"""
    tenant_name = serializers.CharField(source='tenant.user.get_full_name', read_only=True)
    tenant_unit = serializers.CharField(source='tenant.unit', read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'tenant', 'tenant_name', 'tenant_unit', 'amount', 'due_date',
            'payment_date', 'status', 'payment_method', 'transaction_id', 'notes',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class PaymentDetailSerializer(serializers.ModelSerializer):
    """Detailed serializer for Payment with additional calculations"""
    tenant_name = serializers.CharField(source='tenant.user.get_full_name', read_only=True)
    tenant_unit = serializers.CharField(source='tenant.unit', read_only=True)
    days_overdue = serializers.SerializerMethodField()
    
    class Meta:
        model = Payment
        fields = [
            'id', 'tenant', 'tenant_name', 'tenant_unit', 'amount', 'due_date',
            'payment_date', 'status', 'payment_method', 'transaction_id', 'notes',
            'days_overdue', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_days_overdue(self, obj):
        from datetime import date
        if obj.status == 'overdue':
            return (date.today() - obj.due_date).days
        return 0
