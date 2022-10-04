from apotek.app.models import Worker
from apotek.app.serializers.worker_serializer import WorkerSerializer
from apotek.app.views.base_model_viewset import BaseModelViewSet
from rest_framework import viewsets


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer
