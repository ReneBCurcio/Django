from rest_framework.serializers import ModelSerializer
from enderecos.models import endereco

class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = endereco
        fields = ['id', 'linha1', 'linha2', 'cidade', 'estado','pais']