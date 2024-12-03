from rest_framework import viewsets

# Modelos
from .models import (
    Contrato,
    Puesto,
    Persona,
    Entrevista,
    Empleado,
    Gerente,
    Incidencia,
    Nomina,
)

# Serializadores
from .serializers import (
    ContratoSerializer,
    PuestoSerializer,
    PersonaSerializer,
    EntrevistaSerializer,
    EmpleadoSerializer,
    GerenteSerializer,
    IncidenciaSerializer,
    NominaSerializer,
)

from rest_framework.permissions import IsAuthenticated
from .permissions import IsRRHH


class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class PuestoViewSet(viewsets.ModelViewSet):
    queryset = Puesto.objects.all()
    serializer_class = PuestoSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class EntrevistaViewSet(viewsets.ModelViewSet):
    queryset = Entrevista.objects.all()
    serializer_class = EntrevistaSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class GerenteViewSet(viewsets.ModelViewSet):
    queryset = Gerente.objects.all()
    serializer_class = GerenteSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer
    permission_classes = [IsAuthenticated, IsRRHH]


class NominaViewSet(viewsets.ModelViewSet):
    queryset = Nomina.objects.all()
    serializer_class = NominaSerializer
    permission_classes = [IsAuthenticated, IsRRHH]
