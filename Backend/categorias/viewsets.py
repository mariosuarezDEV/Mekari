from rest_framework import viewsets

# Modelos
from .models import CategoriasCuentasModel

# Serializers
from .serializers import CategoriasCuentasSerializer

# Permisos
from rest_framework.permissions import IsAuthenticated
from cuentas.permisions import IsOwner


class CategoriasCuentasViewSet(viewsets.ModelViewSet):
    queryset = CategoriasCuentasModel.objects.all()
    serializer_class = CategoriasCuentasSerializer

    # Solo usuarios autenticados pueden ver las categorias
    permission_classes = [IsAuthenticated, IsOwner]

    # Solo se pueden ver las categorias del usuario logueado
    def get_queryset(self):
        return self.queryset.filter(usr=self.request.user)

    # Solo se pueden crear categorias para el usuario logueado
    def perform_create(self, serializer):
        serializer.save(
            usr=self.request.user,
            usuario_creacion=self.request.user,
            usuario_modificacion=self.request.user,
        )

    # Solo se pueden actualizar categorias del usuario logueado
    def perform_update(self, serializer):
        serializer.save(usuario_modificacion=self.request.user)
