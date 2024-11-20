from datetime import timezone
from rest_framework import viewsets

from .models import TransaccionesModel

from .serializers import TransaccionesSerializers

from rest_framework.permissions import IsAuthenticated
from cuentas.permisions import IsOwner


class TransaccionesViewSet(viewsets.ModelViewSet):
    queryset = TransaccionesModel.objects.all()
    serializer_class = TransaccionesSerializers

    # Solo usuarios autenticados pueden ver las transacciones
    permission_classes = [IsAuthenticated, IsOwner]

    # Solo se pueden ver las transacciones del usuario logueado
    def get_queryset(self):
        return self.queryset.filter(usr=self.request.user)

    # Solo se pueden crear transacciones para el usuario logueado
    def perform_create(self, serializer):
        serializer.save(
            usr=self.request.user,
            usuario_creacion=self.request.user,
            usuario_modificacion=self.request.user,
        )

    # Actualización de datos
    def perform_update(self, serializer):
        serializer.save(
            usuario_modificacion=self.request.user, fecha_modificacion=timezone.now()
        )
