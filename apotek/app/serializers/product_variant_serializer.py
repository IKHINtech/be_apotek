from apotek.app.models import ProductVariant
from rest_framework.serializers import ModelSerializer

class ProductVariantSerializer(ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = '__all__'
