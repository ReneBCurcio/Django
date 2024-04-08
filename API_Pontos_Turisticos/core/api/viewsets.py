from rest_framework.viewsets import ModelViewSet
from core.models import ponto_turisticos
from .serializers import PontoTuristicoSerializer

# ViewSets define the view behavior.
class PontoTuristicoViewSet(ModelViewSet):
    queryset = ponto_turisticos.objects.all()
    serializer_class = PontoTuristicoSerializer