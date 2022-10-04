from apotek.app.serializers.role_serializer import RoleSerializer

from apotek.app.views.base_model_viewset import BaseModelViewSet
from apotek.app.models import Role


class RoleViewSet(BaseModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
