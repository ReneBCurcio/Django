from rest_framework.viewsets import ModelViewSet
from enderecos.models import endereco
from enderecos.api.serializers import EnderecoSerializer

class EnderecoViewSet(ModelViewSet):
    queryset = endereco.objects.all()
    serializer_class = EnderecoSerializer