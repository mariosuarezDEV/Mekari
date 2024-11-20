from rest_framework import viewsets

from .models import CuentasModel
from .serializers import CuentasSerializers

from rest_framework.permissions import IsAuthenticated
from .permisions import IsOwner

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication

# Crear viewsets para las cuentas


class CuentasViewSet(viewsets.ModelViewSet):
    queryset = CuentasModel.objects.all()
    serializer_class = CuentasSerializers

    # Permisos
    permission_classes = [
        IsAuthenticated,
        IsOwner,
    ]

    # Filtrar cuentas por usuario autenticado
    def get_queryset(self):
        return self.queryset.filter(usr=self.request.user)

    # Personalizar la creación de cuentas
    def perform_create(self, serializer):
        # Asignar el usuario autenticado como propietario de la cuenta
        serializer.save(
            usr=self.request.user,
            usuario_creacion=self.request.user,
        )

    # Personalizar la actualización de cuentas
    def perform_update(self, serializer):
        # Asignar el usuario autenticado como propietario de la cuenta
        serializer.save(
            usuario_modificacion=self.request.user,
        )

    # Personalizar accion de actualizar saldo
    @action(detail=True, methods=["patch"], url_path="actualizar-saldo")
    def actualizar_saldo(self, request, pk):
        # Mostar error de no permitido
        return Response(
            {
                "alerta": "Si deseas actualizar tu saldo actual, recomiendo que lo ajustes usando transcciones/moviemiento financieros"
            },
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )
