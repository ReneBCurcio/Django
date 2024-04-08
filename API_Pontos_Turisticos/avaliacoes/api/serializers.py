from rest_framework.serializers import ModelSerializer
from avaliacoes.models import avaliacoes

class AvaliacoesSerializer(ModelSerializer):
    class Meta:
        model = avaliacoes
        fields = ['id', 'usuario', 'nota', 'data']