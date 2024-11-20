from django.db import models

from cuentas.models import CuentasModel
from categorias.models import CategoriasCuentasModel
from django.contrib.auth.models import User

TIPO_TRANSACCION = (
    ("GASTO", "Gasto"),
    ("INGRESO", "Ingreso"),
    ("TRANSFERENCIA", "Transferencia"),
    ("OTRO", "Otro"),
)


class TransaccionesModel(models.Model):
    # Relaciones
    # Un usuario puede tener varias transacciones
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    # Una cuenta puede tener varias transacciones
    cuenta = models.ForeignKey(CuentasModel, on_delete=models.CASCADE)
    # Una categoria puede tener varias transacciones
    categoria = models.ForeignKey(CategoriasCuentasModel, on_delete=models.CASCADE)

    # Campos
    tipo_transaccion = models.CharField(
        choices=TIPO_TRANSACCION,
        max_length=15,
        null=False,
        blank=False,
        verbose_name="Tipo de transaccion",
        default="GASTO",
    )
    monto = models.DecimalField(
        verbose_name="Monto de la transaccion",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
    )
    descripcion = models.CharField(
        max_length=100,
        verbose_name="Descripcion de la transaccion",
        null=True,
        blank=True,
    )
    fecha_movimiento = models.DateField(
        verbose_name="Fecha de la transaccion", null=False, blank=False
    )

    # Campos de auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_creacion_transacciones",
        null=True,
        blank=True,
    )
    usuario_modificacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_modificacion_transacciones",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"

    def __str__(self):
        return f"{self.tipo_transaccion} - {self.monto} - {self.descripcion} - {self.usr.username}"
