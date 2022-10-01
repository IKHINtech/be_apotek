from apotek.app.models import ProductCategory
from apotek.app.serializers.product_category_serializer import ProductCategorySerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet


class ProductCategoryViewSet(BaseModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer

