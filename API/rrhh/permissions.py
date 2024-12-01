from rest_framework.permissions import BasePermission

# Permiso para que solo los usuarios en el grupo "rrhh" puedan modificar los datos de recursos humanos


class IsRRHH(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="rrhh").exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name="rrhh").exists()
