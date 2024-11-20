from rest_framework import serializers

from .models import CuentasModel


class CuentasSerializers(serializers.ModelSerializer):
    class Meta:
        model = CuentasModel
        fields = ["id", "usr", "nombre", "tipo_cuenta", "saldo_actual"]
        read_only_fields = ["usr"]

    def validate_usr(self, value):
        # Validar que el usuario autenticado sea el propietario de la cuenta
        if self.context["request"].user != value:
            raise serializers.ValidationError(
                "Este no es el usuario autenticado, no puedes crear cuentas para otros usuarios."
            )
        return value
