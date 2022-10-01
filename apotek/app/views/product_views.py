from apotek.app.models import Product
from apotek.app.serializers.product_serializer import ProducSerializers
from apotek.app.views.base_model_viewset import BaseModelViewSet

class ProductViewSet(BaseModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProducSerializers