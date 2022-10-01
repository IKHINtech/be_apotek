from apotek.app.views.customer_views import CustomerViewSet

from django.urls import include, re_path
from rest_framework import routers

from apotek.app.views.worker_views import WorkerViewSet

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)
router.register('worker', WorkerViewSet)


urlpatterns = [
    re_path('', include('apotek.app.views.auth.urls')),
       re_path('', include(router.urls)),
]
