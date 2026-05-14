from rest_framework import serializers
from .models import Invoice, InvoiceItem

class InvoiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceItem
        fields = ['id', 'description', 'amount', 'category']

class InvoiceSerializer(serializers.ModelSerializer):
    items = InvoiceItemSerializer(many=True, read_only=True)
    family_name = serializers.CharField(source='family.primary_guardian.get_full_name', read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Invoice
        fields = [
            'id', 'family', 'family_name', 'invoice_number', 'amount_due',
            'amount_paid', 'due_date', 'status', 'status_display',
            'notes', 'items', 'created_at'
        ]
