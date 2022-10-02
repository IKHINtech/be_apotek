from apotek.app.models import Customer
from apotek.app.serializers.base_models_serializer import BaseModelSerializer


class CustomerSerializer(BaseModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
