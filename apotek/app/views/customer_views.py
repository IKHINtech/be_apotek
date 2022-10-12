from apotek.app.serializers.customer_serializer import CustomerSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework.response import Response


from apotek.app.models import Customer


class CustomerViewSet(BaseModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance: Customer = self.get_object()
        instance.is_active = False
        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
