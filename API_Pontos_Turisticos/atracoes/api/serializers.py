from rest_framework.serializers import ModelSerializer
from atracoes.models import Atracao

class AtracaoSerializer(ModelSerializer):
    class Meta:
        model = Atracao
        fields = ['id','nome', 'descricao', 'horario_de_funcionamento', 'idade_minima']