from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Permiso personalizado para verificar si el usuario autenticado es el propietario de la cuenta.
    """

    def has_object_permission(self, request, view, obj):
        # Permite acceso solo si el usuario autenticado es el propietario de la cuenta
        return obj.usr == request.user
