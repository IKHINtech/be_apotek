from apotek.app.models import Product
from apotek.app.serializers.product_serializer import ProducSerializers
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProducSerializers

    def destroy(self, request, *args, **kwargs):
        instance: Product = self.get_object()
        instance.is_active = False
        instance.save()

        serializers = self.get_serializer(instance)
        return Response(serializers.data)
