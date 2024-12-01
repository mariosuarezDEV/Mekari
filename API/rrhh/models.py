from django.db import models

# Create your models here.
from empresa.models import Empresa, Sucursal

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

TIPO_CONTRATO = (
    ("I", "Indefinido"),
    ("D", "Definido"),
    ("P", "Por proyecto"),
    ("H", "Por horas"),
    ("T", "Temporal"),
    ("O", "Otro"),
)

CLASIFICACION_INCIDENCIA = (
    ("J", "Justificada"),
    ("I", "Injustificada"),
    ("P", "Permiso"),
    ("V", "Vacaciones"),
    ("O", "Otro"),
)

TIPO_INCIDENCIA = (("D", "Deducción"), ("A", "Bono"), ("O", "Otro"))

ESTADO_INCIDENCIA = (("A", "Aceptada"), ("R", "Rechazada"), ("P", "Pendiente"))


# Modelos


class Contrato(models.Model):
    nombre = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre del contrato"
    )

    salario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=False,
        verbose_name="Salario Diario",
    )
    tipo = models.CharField(
        max_length=1,
        choices=TIPO_CONTRATO,
        null=False,
        blank=False,
        verbose_name="Tipo de contrato",
    )

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return f"{self.nombre} - {self.tipo} - ${self.salario}"


class Puesto(models.Model):
    # Información del puesto
    nombre = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Nombre del puesto"
    )
    descripcion = models.TextField(
        null=False, blank=False, verbose_name="Descripción del puesto"
    )

    class Meta:
        verbose_name = "Puesto"
        verbose_name_plural = "Puestos"

    def __str__(self):
        return self.nombre


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


# Modelo para personas entrevistadas
class Entrevista(models.Model):
    # Informacion de la entrevista
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, verbose_name="Persona"
    )
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, verbose_name="Puesto")

    # Información de la empresa
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, verbose_name="Sucursal"
    )

    # Información de la entrevista
    fecha = models.DateField(
        null=False, blank=False, verbose_name="Fecha de la entrevista"
    )
    comentarios = models.TextField(
        null=True, blank=True, verbose_name="Comentarios de la entrevista"
    )
    estado = models.BooleanField(
        null=False, blank=False, default=False, verbose_name="Estado de solicitud"
    )

    class Meta:
        verbose_name = "Entrevista"
        verbose_name_plural = "Entrevistas"

    def __str__(self):
        return f"{self.persona} - {self.puesto} - {self.fecha}"


class Empleado(models.Model):
    # Información del empleado
    persona = models.OneToOneField(
        Persona, on_delete=models.CASCADE, verbose_name="Persona"
    )
    puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE, verbose_name="Puesto")

    # Información de la empresa
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, verbose_name="Sucursal"
    )

    # Información del contrato
    contrato = models.OneToOneField(
        Contrato, on_delete=models.CASCADE, verbose_name="Contrato"
    )
    fecha_inicio = models.DateField(
        null=False, blank=False, verbose_name="Fecha de inicio"
    )
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de fin")

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return f"{self.persona} - {self.puesto} - {self.fecha_inicio}"


class Gerente(models.Model):
    # Información del empleado
    empleado = models.OneToOneField(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )

    # Información de la empresa
    empresa = models.ForeignKey(
        Empresa, on_delete=models.CASCADE, verbose_name="Empresa"
    )
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, verbose_name="Sucursal"
    )

    # Información del contrato
    contrato = models.OneToOneField(
        Contrato, on_delete=models.CASCADE, verbose_name="Contrato"
    )
    fecha_inicio = models.DateField(
        null=False, blank=False, verbose_name="Fecha de inicio"
    )
    fecha_fin = models.DateField(null=True, blank=True, verbose_name="Fecha de fin")

    class Meta:
        verbose_name = "Gerente"
        verbose_name_plural = "Gerentes"

    def __str__(self):
        return f"{self.persona} - {self.puesto} - {self.fecha_inicio}"


class Incidencia(models.Model):
    # Información de la incidencia
    empleado = models.ForeignKey(
        Empleado, on_delete=models.CASCADE, verbose_name="Empleado"
    )
    fecha = models.DateField(
        null=False, blank=False, verbose_name="Fecha de la incidencia"
    )
    descripcion = models.TextField(
        null=False, blank=False, verbose_name="Descripción de la incidencia"
    )

    # Información de la incidencia
    clasificacion = models.CharField(
        max_length=1,
        choices=CLASIFICACION_INCIDENCIA,
        null=False,
        blank=False,
        verbose_name="Clasificación de la incidencia",
    )

    estado = models.CharField(
        max_length=1,
        choices=ESTADO_INCIDENCIA,
        null=False,
        blank=False,
        verbose_name="Estado de la incidencia",
        default="P",
    )

    tipo = models.CharField(
        max_length=1,
        choices=TIPO_INCIDENCIA,
        null=False,
        blank=False,
        verbose_name="Tipo de incidencia",
    )

    # Gerente que autoriza la incidencia
    gerente = models.ForeignKey(
        Gerente, on_delete=models.CASCADE, verbose_name="Gerente"
    )

    class Meta:
        verbose_name = "Incidencia"
        verbose_name_plural = "Incidencias"

    def __str__(self):
        return f"{self.empleado} - {self.clasificacion} - {self.fecha}"
