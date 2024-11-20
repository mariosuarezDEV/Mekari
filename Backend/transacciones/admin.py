from django.contrib import admin

from .models import TransaccionesModel


@admin.register(TransaccionesModel)
class TransaccionesModelAdmin(admin.ModelAdmin):
    list_display = [
        "usr",
        "cuenta",
        "categoria",
        "tipo_transaccion",
        "monto",
        "descripcion",
        "fecha_movimiento",
    ]
    search_fields = ["usr", "descripcion"]
    list_filter = ["tipo_transaccion"]
    date_hierarchy = "fecha_movimiento"
