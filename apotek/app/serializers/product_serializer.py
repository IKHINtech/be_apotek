from apotek.app.models import Product
from rest_framework import serializers

from apotek.app.serializers.product_category_serializer import ProductCategorySerializer

class ProducSerializers(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    class Meta:
        model = Product
        fields =['id','name','category', 'created_at', 'updated_at']