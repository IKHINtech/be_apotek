from apotek.app.models import Product, ProductUnit, ProductVariant, Supplier
from rest_framework import serializers

from apotek.app.serializers.product_serializer import ProducSerializers
from apotek.app.serializers.supplier_serializer import SupplierSerializer
from apotek.app.serializers.unit_serializer import ProductUnitSerializer

class ProductVariantSerializer(serializers.ModelSerializer):
    product_id= serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source = 'product')
    supplier_id = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all(), write_only=True, source = 'supplier')
    unit_id = serializers.PrimaryKeyRelatedField(queryset=ProductUnit.objects.all(), write_only=True, source= 'unit')

    product = ProducSerializers(read_only=True)
    supplier = SupplierSerializer(read_only=True)
    unit = ProductUnitSerializer(read_only=True)
    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'product', 'supplier', 'unit', 'product_id','supplier_id', 'unit_id', 'created_at', 'updated_at']
