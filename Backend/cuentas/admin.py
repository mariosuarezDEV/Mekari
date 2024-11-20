from django.contrib import admin

from .models import CuentasModel


@admin.register(CuentasModel)
class CuentasAmin(admin.ModelAdmin):
    list_display = ["usr__username", "nombre", "tipo_cuenta", "saldo_actual"]
    search_fields = ["nombre", "usr__username"]
    list_filter = ["tipo_cuenta"]
