from django.contrib import admin

# Register your models here.
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


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "salario", "tipo"]
    search_fields = ["nombre"]
    list_filter = ["tipo"]
    list_per_page = 10


@admin.register(Puesto)
class PuestoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "descripcion"]
    search_fields = ["nombre"]
    list_per_page = 10


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "apellidos", "curp", "email", "telefono"]
    search_fields = ["nombre", "apellidos", "email", "curp", "telefono"]
    list_per_page = 10


@admin.register(Entrevista)
class EntrevistaAdmin(admin.ModelAdmin):
    list_display = ["id", "fecha", "persona", "puesto", "estado"]
    search_fields = ["persona__nombre", "persona__apellidos", "puesto__nombre"]
    list_per_page = 10
    list_filter = ["estado", "puesto__nombre"]
    date_hierarchy = "fecha"


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ["id", "persona", "puesto", "sucursal", "contrato", "clave"]
    search_fields = ["persona__nombre", "persona__apellidos", "puesto__nombre"]
    list_per_page = 10
    list_filter = ["puesto__nombre"]
    date_hierarchy = "fecha_inicio"


@admin.register(Gerente)
class GerenteAdmin(admin.ModelAdmin):
    list_display = ["id", "empleado", "sucursal"]
    search_fields = ["persona__nombre", "persona__apellidos"]
    list_per_page = 10


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ["empleado", "fecha", "clasificacion", "estado", "tipo", "gerente"]
    search_fields = ["empleado"]
    list_filter = ["estado", "clasificacion", "tipo"]
    date_hierarchy = "fecha"


@admin.register(Nomina)
class NominaAdmin(admin.ModelAdmin):
    list_display = ["id", "empleado", "fecha_inicio", "fecha_fin", "total"]
    search_fields = ["empleado"]
    date_hierarchy = "fecha_inicio"
