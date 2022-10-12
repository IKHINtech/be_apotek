from apotek.app.models import Supplier
from apotek.app.serializers.supplier_serializer import SupplierSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


class SupplierViewSet(BaseModelViewSet):
    queryset = Supplier.objects.filter(is_active=True)
    serializer_class = SupplierSerializer

    def destroy(self, request, *args, **kwargs):
        instance: Supplier = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
