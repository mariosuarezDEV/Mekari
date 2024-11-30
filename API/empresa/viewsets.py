from rest_framework import viewsets
from .models import Empresa, Sucursal
from .serializers import EmpresaSerializer, SucursalSerializer

from rest_framework.permissions import IsAuthenticated
from .permissions import IsGerenciaOperativa

from rest_framework.decorators import action

from rest_framework.response import Response
from rest_framework import status


class EmpresaView(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated, IsGerenciaOperativa]


class SucursalView(viewsets.ModelViewSet):
    queryset = Sucursal.objects.all()
    serializer_class = SucursalSerializer
    permission_classes = [IsAuthenticated, IsGerenciaOperativa]
