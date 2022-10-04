from apotek.app.views.customer_views import CustomerViewSet

from django.urls import include, re_path
from rest_framework import routers
from apotek.app.views.product_category_viewset import ProductCategoryViewSet
from apotek.app.views.product_detail_viewset import ProductDetailViewSet
from apotek.app.views.product_variant_viewset import ProductVariantViewSet
from apotek.app.views.product_views import ProductViewSet
from apotek.app.views.role_views import RoleViewSet
from apotek.app.views.supplier_serializer import SupplierViewSet
from apotek.app.views.unit_viewsets import ProductUnitViewSet

from apotek.app.views.worker_views import WorkerViewSet

router = routers.DefaultRouter()

router.register('customer', CustomerViewSet)
router.register('product', ProductViewSet)
router.register('product-category', ProductCategoryViewSet)
router.register('product-detail', ProductDetailViewSet)
router.register('product-unit', ProductUnitViewSet)
router.register('product-variant', ProductVariantViewSet)
router.register('supplier', SupplierViewSet)
router.register('role', RoleViewSet)


router.register('worker', WorkerViewSet)


urlpatterns = [
    re_path('', include('apotek.app.views.auth.urls')),
    re_path('', include(router.urls)),
]
