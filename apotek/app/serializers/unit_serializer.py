from apotek.app.models import ProductUnit
from rest_framework.serializers import  ModelSerializer

class ProductUnitSerializer(ModelSerializer):
    class Meta:
        model = ProductUnit
        fields = '__all__'
