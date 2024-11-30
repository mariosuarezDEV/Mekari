from django.db import models

# Create your models here.

# Opciones
GENERO = (
    ("M", "Masculino"),
    ("F", "Femenino"),
    ("O", "Otro"),
)

ESTADO_CIVIL = (
    ("S", "Soltero"),
    ("C", "Casado"),
    ("D", "Divorciado"),
    ("V", "Viudo"),
)

# Modelos


class Persona(models.Model):
    # Informacion del empleado
    nombre = models.CharField(
        max_length=25, null=False, blank=False, verbose_name="Nombre(s)"
    )
    apellidos = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Apellidos"
    )
    fecha_nacimiento = models.DateField(
        null=False, blank=False, verbose_name="Fecha de nacimiento"
    )

    # Informacion de contacto
    email = models.EmailField(
        null=False, blank=False, verbose_name="Correo electrónico"
    )
    telefono = models.CharField(
        max_length=15, null=False, blank=False, verbose_name="Número de teléfono"
    )

    # Información de la dirección
    calle = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Calle"
    )
    numero = models.IntegerField(null=False, blank=False, verbose_name="Número")
    cp = models.CharField(
        max_length=5, null=False, blank=False, verbose_name="Código Postal"
    )
    colonia = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Colonia"
    )
    ciudad = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Ciudad"
    )
    estado = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Estado"
    )

    # Genero
    genero = models.CharField(
        max_length=1, choices=GENERO, null=False, blank=False, verbose_name="Género"
    )

    # Información personal
    rfc = models.CharField(max_length=13, null=True, blank=True, verbose_name="RFC")
    curp = models.CharField(max_length=18, null=True, blank=True, verbose_name="CURP")
    nss = models.CharField(
        max_length=11, null=True, blank=True, verbose_name="Número de Seguro Social"
    )
    estado_civil = models.CharField(
        max_length=1,
        choices=ESTADO_CIVIL,
        null=True,
        blank=True,
        verbose_name="Estado Civil",
    )

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
