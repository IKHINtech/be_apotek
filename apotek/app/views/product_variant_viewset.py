from apotek.app.models import ProductVariant
from apotek.app.serializers.product_variant_serializer import ProductVariantSerializer, ProductVariantListSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


class ProductVariantViewSet(BaseModelViewSet):
    queryset = ProductVariant.objects.all()
    serializer_class = ProductVariantListSerializer

    def get_serializer_class(self):
        if self.action.lower() in ['retrieve', 'create']:
            self.serializer_class = ProductVariantSerializer
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        instance: ProductVariant = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
