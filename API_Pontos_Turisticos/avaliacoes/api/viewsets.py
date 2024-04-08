from rest_framework.viewsets import ModelViewSet
from avaliacoes.models import avaliacoes
from avaliacoes.api.serializers import AvaliacoesSerializer

class AvaliacoesViewSets(ModelViewSet):
    queryset = avaliacoes.objects.all()
    serializer_class = AvaliacoesSerializer