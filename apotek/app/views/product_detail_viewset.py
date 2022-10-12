from apotek.app.models import ProductDetail
from apotek.app.serializers.product_detail_serializer import ProductDetailListSerializer, ProductDetailSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


class ProductDetailViewSet(BaseModelViewSet):
    queryset = ProductDetail.objects.all()
    serializer_class = ProductDetailListSerializer

    def list(self, request, *args, **kwargs):
        data = self
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action.lower() == 'retrieve':
            self.serializer_class = ProductDetailSerializer
        return self.serializer_class

    def destroy(self, request, *args, **kwargs):
        instance: ProductDetail = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
