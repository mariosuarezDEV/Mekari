from django.db import models

# Create your models here.


class Empresa(models.Model):
    nombre = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre de la empresa"
    )

    # Información fiscal
    rfc = models.CharField(
        max_length=13, null=True, blank=True, verbose_name="RFC de la empresa"
    )

    # Contacto
    telefono = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="Número de teléfono"
    )
    email = models.EmailField(null=True, blank=True, verbose_name="Correo electrónico")

    # Dirección
    calle = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Calle"
    )
    numero = models.IntegerField(
        null=False, blank=False, verbose_name="Número exterior"
    )
    cp = models.IntegerField(null=False, blank=False, verbose_name="Código Postal")
    colonia = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Colonia"
    )
    ciudad = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Ciudad"
    )
    estado = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Estado"
    )
    pais = models.CharField(max_length=50, null=False, blank=False, verbose_name="País")

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nombre


class Sucursal(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre de la sucursal"
    )

    # Contacto
    telefono = models.CharField(
        max_length=15, null=False, blank=False, verbose_name="Número de teléfono"
    )
    email = models.EmailField(
        null=False, blank=False, verbose_name="Correo electrónico"
    )

    # Dirección
    calle = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Calle"
    )
    numero = models.IntegerField(
        null=False, blank=False, verbose_name="Número exterior"
    )
    cp = models.IntegerField(null=False, blank=False, verbose_name="Código Postal")
    colonia = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Colonia"
    )
    ciudad = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Ciudad"
    )
    estado = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Estado"
    )
    pais = models.CharField(max_length=50, null=False, blank=False, verbose_name="País")

    class Meta:
        verbose_name = "Sucursal"
        verbose_name_plural = "Sucursales"

    def __str__(self):
        return self.nombre
