from rest_framework.routers import DefaultRouter
from .viewsets import CategoriasCuentasViewSet
from django.urls import path

router = DefaultRouter()
router.register(r"categorias", CategoriasCuentasViewSet)

urlpatterns = router.urls
