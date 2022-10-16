from apotek.app.models import Product, ProductDetail, ProductUnit, ProductVariant, Supplier
from rest_framework import serializers
from apotek.app.serializers.product_serializer import ProducSerializers
from apotek.app.serializers.supplier_serializer import SupplierSerializer
from apotek.app.serializers.unit_serializer import ProductUnitSerializer
from django.db.transaction import atomic


class ProductVariantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetail
        exclude = ['product_variant']


class ProductVariantSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(), write_only=True, source='supplier')
    unit_id = serializers.PrimaryKeyRelatedField(queryset=ProductUnit.objects.all(), write_only=True, source='unit')
    details = ProductVariantDetailSerializer(many=True, write_only=True)

    product = ProducSerializers(read_only=True, required=False)
    supplier = SupplierSerializer(read_only=True, required=False)
    unit = ProductUnitSerializer(read_only=True, required=False)

    class Meta:
        model = ProductVariant
        fields = ['id', 'name', 'product', 'supplier', 'unit', 'product_id',
                  'supplier_id', 'unit_id', 'created_at', 'updated_at', 'details']

    @atomic
    def create(self, validated_data):
        details_data = validated_data.pop('details', None)
        variant = ProductVariant.objects.create(**validated_data)

        for detail in details_data:
            ProductDetail.objects.create(product_variant=variant, **detail)

        return variant


class ProductVariantListSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(read_only=True, source='product.name')
    category = serializers.CharField(read_only=True, source='product.category.name')
    unit_name = serializers.CharField(read_only=True, source='unit.name')
    supplier_name = serializers.CharField(read_only=True, source='supplier.name')

    class Meta:
        model = ProductVariant
        exclude = ['product', 'supplier', 'unit']
