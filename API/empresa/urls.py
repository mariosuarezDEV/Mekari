from django.urls import path
from .viewsets import EmpresaView, SucursalView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"empresa", EmpresaView)
router.register(r"sucursal", SucursalView)

urlpatterns = router.urls
