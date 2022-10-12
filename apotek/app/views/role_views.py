from apotek.app.serializers.role_serializer import RoleSerializer

from apotek.app.views.base_model_viewset import BaseModelViewSet
from apotek.app.models import Role


class RoleViewSet(BaseModelViewSet):
    queryset = Role.objects.filter(is_active=True)
    serializer_class = RoleSerializer
