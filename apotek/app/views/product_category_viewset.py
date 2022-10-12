from apotek.app.models import ProductCategory
from apotek.app.serializers.product_category_serializer import ProductCategorySerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


class ProductCategoryViewSet(BaseModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance: ProductCategory = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
