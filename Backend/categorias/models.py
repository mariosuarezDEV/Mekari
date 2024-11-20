from django.db import models

# Usuarios
from django.contrib.auth.models import User

TIPO_CATEGORIA = (
    ("GASTO", "Gasto"),
    ("INGRESO", "Ingreso"),
    ("AHORRO", "Ahorro"),
    ("DEUDA", "Deuda"),
    ("OTRO", "Otro"),
)


class CategoriasCuentasModel(models.Model):
    usr = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=100, verbose_name="Nombre de la categoria", null=False, blank=False
    )
    descripcion = models.CharField(
        max_length=100,
        verbose_name="Descripcion de la categoria",
        null=True,
        blank=True,
    )
    tipo_categoria = models.CharField(
        choices=TIPO_CATEGORIA,
        max_length=10,
        null=False,
        blank=False,
        verbose_name="Tipo de categoria",
        default="GASTO",
    )
    # En caso de tener gastos asociados a la categoria
    persupuesto = models.DecimalField(
        verbose_name="Presupuesto",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
    )

    # Campos de auditoria
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    usuario_creacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_creacion_categorias",
        null=True,
        blank=True,
    )
    usuario_modificacion = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="usuario_modificacion_categorias",
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "Categoria de cuenta"
        verbose_name_plural = "Categorias de cuentas"

    def __str__(self):
        return f"{self.nombre} - {self.tipo_categoria} - {self.usr.username}"
