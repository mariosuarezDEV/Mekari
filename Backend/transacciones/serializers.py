from rest_framework import serializers

from .models import TransaccionesModel


class TransaccionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransaccionesModel
        fields = [
            "id",
            "usr",
            "cuenta",
            "categoria",
            "tipo_transaccion",
            "monto",
            "descripcion",
            "fecha_movimiento",
        ]
        read_only_fields = ["usr"]

    def validate_usr(self, value):
        # Validar que el usuario autenticado sea el propietario de la cuenta
        if self.context["request"].user != value:
            raise serializers.ValidationError(
                "Este no es el usuario autenticado, no puedes crear transacciones para otros usuarios."
            )
        return value

    # Validar que la cuenta pertenezca al usuario autenticado
    def validate_cuenta(self, value):
        if value.usr != self.context["request"].user:
            raise serializers.ValidationError(
                "El usuario no tiene esta cuenta registrada."
            )
        return value

    # Validar que la categoria pertenezca al usuario autenticado
    def validate_categoria(self, value):
        if value.usr != self.context["request"].user:
            raise serializers.ValidationError(
                "El usuario no tiene esta categoria registrada."
            )
        return value
