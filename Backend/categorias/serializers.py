from rest_framework import serializers

from .models import CategoriasCuentasModel


class CategoriasCuentasSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriasCuentasModel
        fields = [
            "id",
            "usr",
            "nombre",
            "descripcion",
            "tipo_categoria",
            "persupuesto",
        ]
        read_only_fields = ["usr"]

    # Validar que el usuario que crea la categoria sea el mismo que esta logueado
    def validate_usr(self, value):
        if value != self.context["request"].user:
            raise serializers.ValidationError(
                "No puedes crear una categoria para otro usuario"
            )
        return value

    def validate_presupuesto(self, value):
        tipo_cuenta = self.initial_data.get("tipo_cuenta")
        # Si el tipo de cuenta es "GASTO" o "AHORRO" el presupuesto no puede ser nulo
        if tipo_cuenta in ["GASTO", "AHORRO"] and value is None:
            raise serializers.ValidationError(
                "El presupuesto no puede ser nulo para cuentas de tipo GASTO o AHORRO"
            )
        # Si el tipo de cuenta es "INGRESO" o "OTRO" el presupuesto debe ser nulo
        if tipo_cuenta in ["INGRESO", "OTRO"] and value is not None:
            raise serializers.ValidationError(
                "El presupuesto debe ser nulo para cuentas de tipo INGRESO u OTRO"
            )
        return value
