from django.contrib import admin

# Register your models here.
from .models import Empresa, Sucursal


class EmpresaAdmin(admin.ModelAdmin):
    list_display = [
        "nombre",
        "rfc",
        "telefono",
        "email",
        "calle",
        "numero",
        "cp",
        "colonia",
        "ciudad",
        "estado",
        "pais",
    ]


class SucursalAdmin(admin.ModelAdmin):
    list_display = [
        "empresa",
        "nombre",
        "telefono",
        "calle",
        "numero",
        "cp",
        "colonia",
    ]


admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Sucursal, SucursalAdmin)
