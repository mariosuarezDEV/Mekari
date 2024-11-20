from rest_framework.routers import DefaultRouter

from .viewsets import TransaccionesViewSet

router = DefaultRouter()
router.register(r"categorias", TransaccionesViewSet)

urlpatterns = router.urls
