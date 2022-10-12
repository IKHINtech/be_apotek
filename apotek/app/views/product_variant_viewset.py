from apotek.app.models import ProductVariant
from apotek.app.serializers.product_variant_serializer import ProductVariantSerializer, ProductVariantListSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet


class ProductVariantViewSet(BaseModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer

    def get_serializer_class(self):
        if self.action.lower() == 'retrieve':
            self.serializer_class = ProductVariantSerializer
        return self.serializer_class
