from apotek.app.models import Supplier
from apotek.app.serializers.base_models_serializer import BaseModelSerializer


class SupplierSerializer(BaseModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
