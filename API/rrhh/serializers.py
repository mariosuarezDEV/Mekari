from rest_framework import serializers
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


class ContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contrato
        fields = "__all__"


class PuestoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Puesto
        fields = ["nombre", "descripcion"]


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = "__all__"


class EntrevistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrevista
        fields = "__all__"


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = "__all__"


class GerenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerente
        fields = "__all__"


class IncidenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidencia
        fields = "__all__"


class NominaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nomina
        fields = "__all__"
