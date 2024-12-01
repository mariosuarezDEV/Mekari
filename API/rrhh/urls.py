from django.urls import path
from rest_framework.routers import DefaultRouter

# Viewsets
from .viewsets import (
    ContratoViewSet,
    PuestoViewSet,
    PersonaViewSet,
    EntrevistaViewSet,
    EmpleadoViewSet,
    GerenteViewSet,
    IncidenciaViewSet,
    NominaViewSet,
)

router = DefaultRouter()
router.register(r"contrato", ContratoViewSet)
router.register(r"puesto", PuestoViewSet)
router.register(r"persona", PersonaViewSet)
router.register(r"entrevista", EntrevistaViewSet)
router.register(r"empleado", EmpleadoViewSet)
router.register(r"gerente", GerenteViewSet)
router.register(r"incidencia", IncidenciaViewSet)
router.register(r"nomina", NominaViewSet)

urlpatterns = router.urls
