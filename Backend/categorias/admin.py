from django.contrib import admin

from .models import CategoriasCuentasModel


@admin.register(CategoriasCuentasModel)
class CategoriasCuentasAdmin(admin.ModelAdmin):
    list_display = ["usr", "nombre", "descripcion", "tipo_categoria", "persupuesto"]
    search_fields = [
        "nombre",
    ]
    list_filter = ["tipo_categoria"]
