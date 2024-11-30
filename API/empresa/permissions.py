# permiso para que solo el usuario en el grupo "gerencia operativa" pueda modificar la empresa

from rest_framework.permissions import BasePermission


class IsGerenciaOperativa(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="gerencia operativa").exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="gerencia operativa").exists()
