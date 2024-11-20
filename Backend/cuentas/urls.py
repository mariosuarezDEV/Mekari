from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import CuentasViewSet

# Router para las cuentas
router = DefaultRouter()
router.register(r"cuentas", CuentasViewSet)

urlpatterns = router.urls
