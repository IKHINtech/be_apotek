from apotek.app.models import ProductCategory
from rest_framework.serializers import ModelSerializer

class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'
