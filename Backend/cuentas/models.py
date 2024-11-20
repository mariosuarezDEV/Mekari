from django.db import models

# Usuarios
from django.contrib.auth.models import User

# Tipso de cuentas
Cuentas = (
    ("Ahorro", "Ahorro"),
    ("Inversion", "Inversion"),
    ("Nomina", "Nomina"),
    ("Efectivo", "Efectivo"),
    ("Debito", "Debito"),
    ("Credito", "Credito"),
)


class CuentasModel(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la cuenta", null=False, blank=False
    )
    tipo_cuenta = models.CharField(
        choices=Cuentas,
        max_length=100,
        null=False,
        blank=False,
        verbose_name="Tipo de cuenta",
    )
    saldo_inicial = models.DecimalField(
        verbose_name="Saldo inicial",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )
    saldo_actual = models.DecimalField(
        verbose_name="Saldo actual",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )

    # Campos de auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_creacion_cuentas",
        null=True,
        blank=True,
    )
    usuario_modificacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_modificacion_cuentas",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"

    def __str__(self):
        return f"{self.nombre} - {self.tipo_cuenta} - {self.saldo_actual} - {self.usr.username}"
