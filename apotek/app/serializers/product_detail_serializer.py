from apotek.app.models import ProductDetail, ProductVariant
from rest_framework import serializers

from apotek.app.serializers.product_variant_serializer import ProductVariantSerializer

class ProductDetailSerializer(serializers.ModelSerializer):
    product_variant= ProductVariantSerializer(read_only=True)
    class Meta:
        model = ProductDetail
        fields =['id', 'product_variant', 'exp_date', 'stock', 'price','ppn', 'dicount', 'barcode', 'final_price', 'created_at', 'updated_at']

class ProductDetailListSerializer(serializers.ModelSerializer):
    product_variant_name= serializers.CharField(read_only=True, source = 'product_variant.name')
    product_variant_id = serializers.PrimaryKeyRelatedField(queryset=ProductVariant.objects.all(), write_only=True, source='product_variant')
    class Meta:
        model = ProductDetail
        fields =['id', 'product_variant_name', 'product_variant_id', 'exp_date', 'stock', 'price','ppn', 'dicount', 'barcode', 'final_price', 'created_at', 'updated_at']
    