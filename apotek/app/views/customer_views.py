from apotek.app.serializers.customer_serializer import CustomerSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet


from apotek.app.models import Customer


class CustomerViewSet(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
