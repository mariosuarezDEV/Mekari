from rest_framework import serializers
from .models import Empresa, Sucursal


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            "nombre",
            "rfc",
            "calle",
            "numero",
            "cp",
            "colonia",
            "ciudad",
            "estado",
        ]


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = [
            "nombre",
            "telefono",
            "email",
            "calle",
            "numero",
            "cp",
            "colonia",
            "ciudad",
            "estado",
        ]
