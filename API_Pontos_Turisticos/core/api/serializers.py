from rest_framework.serializers import ModelSerializer
from core.models import ponto_turisticos

class PontoTuristicoSerializer(ModelSerializer):
    class Meta:
        model = ponto_turisticos
        fields = ['id','nome', 'descricao']