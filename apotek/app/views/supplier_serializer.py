from apotek.app.models import Supplier
from apotek.app.serializers.supplier_serializer import SupplierSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet

class SupplierViewSet(BaseModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer