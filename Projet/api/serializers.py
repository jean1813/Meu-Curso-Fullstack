from rest_framework import serializers
from apps.core.models import Clientes

class ClientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = ["name", "cpf_cnpj", "rg_ie", "zip_code", "address", "neighborhood", "number", "city", "state" ]