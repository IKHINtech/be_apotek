from apotek.app.models import Product, ProductCategory
from rest_framework import serializers

from apotek.app.serializers.product_category_serializer import ProductCategorySerializer


class ProducSerializers(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=ProductCategory.objects.all(
    ),  write_only=True, source='category')
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
