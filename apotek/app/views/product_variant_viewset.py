from apotek.app.models import ProductVariant
from apotek.app.serializers.product_variant_serializer import ProductVariantSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet


class ProductVariantViewSet(BaseModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantSerializer

