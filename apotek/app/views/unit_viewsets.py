from apotek.app.serializers.unit_serializer import ProductUnitSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from apotek.app.models import ProductUnit
from rest_framework.response import Response


class ProductUnitViewSet(BaseModelViewSet):
    queryset = ProductUnit.objects.filter(is_active=True)
    serializer_class = ProductUnitSerializer

    def destroy(self, request, *args, **kwargs):
        instance: ProductUnit = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)

        return Response(serializer.data)
