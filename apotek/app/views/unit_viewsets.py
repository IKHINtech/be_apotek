from apotek.app.serializers.unit_serializer import ProductUnitSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from apotek.app.models import ProductUnit


class ProductUnitViewSet(BaseModelViewSet):
    queryset = ProductUnit.objects.all()
    serializer_class = ProductUnitSerializer
    