from apotek.app.views.customer_views import CustomerViewSet

from django.urls import include, re_path
from rest_framework import routers

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)


urlpatterns = [
    re_path('', include(router.urls)),
]
